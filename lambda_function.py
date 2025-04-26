import json
import boto3
import os
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')
comprehend = boto3.client('comprehend')

# Environment variables (set these in your Lambda function environment settings)
TABLE_NAME = os.environ['TABLE_NAME']  # DynamoDB table name
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']  # SNS Topic ARN

# DynamoDB table object
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    # Get HTTP method from the event
    http_method = event['httpMethod']
    logger.info(f"Received {http_method} request for {event['path']}")

    if http_method == 'GET':
        # Serve the feedback form page or records page
        if event['path'] == "/feedback":
            return serve_feedback_submission_page()
        elif event['path'] == "/feedback/records":
            return serve_feedback_records_page()
        else:
            logger.error("Path not found: %s", event['path'])
            return {
                "statusCode": 404,
                "body": json.dumps({"message": "Not Found"})
            }

    elif http_method == 'POST' and event['path'] == "/feedback":
        return handle_post_request(event)
    else:
        logger.error("Method not allowed: %s", http_method)
        return {
            "statusCode": 405,
            "body": json.dumps({"message": "Method not allowed"})
        }

def handle_post_request(event):
    try:
        logger.info("Handling POST request to submit feedback.")
        
        # Parse request body
        body = json.loads(event['body'])
        first_name = body['first_name']
        last_name = body['last_name']
        email = body['email']
        message = body['message']
        logger.info(f"Received feedback from {first_name} {last_name} ({email}): {message}")

        # Analyze sentiment using Comprehend
        sentiment_response = comprehend.detect_sentiment(
            Text=message,
            LanguageCode='en'
        )
        sentiment = sentiment_response['Sentiment']
        logger.info(f"Sentiment detected: {sentiment}")

        # Store feedback in DynamoDB
        logger.info("Storing feedback in DynamoDB...")
        table.put_item(
            Item={
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'message': message,
                'sentiment': sentiment
            }
        )
        logger.info(f"Feedback successfully stored for {first_name} {last_name}.")

        # Notify stakeholders via SNS
        logger.info("Publishing notification to SNS...")
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="New Feedback Received",
            Message=(
                f"New feedback received:\n\n"
                f"Name: {first_name} {last_name}\n"
                f"Email: {email}\n"
                f"Message: {message}\n"
                f"Sentiment: {sentiment}"
            )
        )
        logger.info("Notification sent to SNS.")

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Feedback submitted successfully!"})
        }
    except Exception as e:
        logger.error(f"Error processing feedback: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Failed to process feedback", "error": str(e)})
        }

def serve_feedback_submission_page():
    try:
        logger.info("Serving feedback submission page...")
        
        # Attempt to open the feedback_submission.html file
        file_path = '/var/task/feedback_submission.html'
        logger.info(f"Attempting to open file at: {file_path}")
        
        with open(file_path, 'r') as file:
            html_content = file.read()
        
        logger.info("Feedback submission page served successfully.")
        
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/html"},
            "body": html_content
        }
    except Exception as e:
        logger.error(f"Error serving feedback submission page: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Error serving feedback form", "error": str(e)})
        }

def serve_feedback_records_page():
    try:
        # Retrieve all feedback records from DynamoDB with pagination handling
        feedbacks = []
        last_evaluated_key = None

        # Loop to handle pagination
        while True:
            if last_evaluated_key:
                response = table.scan(ExclusiveStartKey=last_evaluated_key)
            else:
                response = table.scan()

            feedbacks.extend(response.get('Items', []))
            last_evaluated_key = response.get('LastEvaluatedKey')
            if not last_evaluated_key:
                break

        # Create HTML content to display feedback records
        feedback_html = ""
        for feedback in feedbacks:
            sentiment = feedback.get('sentiment', 'N/A') 
            feedback_html += f"""
            <div class="feedback-card">
                <h3>{feedback['first_name']} {feedback['last_name']}</h3>
                <p><strong>Email:</strong> {feedback['email']}</p>
                <p><strong>Message:</strong> {feedback['message']}</p>
                <p><strong>Sentiment:</strong> {sentiment}</p>
            </div>
            """

        # Load the feedback records template
        with open('/var/task/feedback_records.html', 'r') as file:
            html_content = file.read()

        # Inject the feedback records into the HTML template
        html_content = html_content.replace("{{feedback_records}}", feedback_html)

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "text/html"},
            "body": html_content
        }
    except Exception as e:
        logger.error(f"Error retrieving feedback records: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Error retrieving feedback records", "error": str(e)})
        }

