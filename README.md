# Feedback Analysis System using AWS
A fully serverless cloud-native application designed to collect, analyze, and notify customer feedback in real time using AWS services. Built for scalability, low maintenance, and AI-powered insights using sentiment analysis.

---

## 💡 Features

- 📥 Collect feedback via a web form
- 🧠 Analyze message sentiment (Positive, Negative, Neutral)
- 📩 Notify team members based on sentiment
- 🗂 Store structured feedback in DynamoDB
- 📊 Monitor logs using CloudWatch
- ⚡️ Completely serverless — scales on demand

---

## 🧱 Architecture Diagram
![diagram-export-4-26-2025-10_51_31-PM](https://github.com/user-attachments/assets/450524cd-119c-465f-91fd-a1b0341ef3c3)


---

## 🛠️ Tech Stack & AWS Services Used

- **Frontend**: HTML + HTTP form
- **Backend**: AWS Lambda (Python)
- **Database**: Amazon DynamoDB
- **Sentiment Analysis**: Amazon Comprehend
- **Notifications**: Amazon SNS (Email)
- **Monitoring**: Amazon CloudWatch
- **API Gateway**: To expose Lambda as an endpoint

---

## 🚀 How to Set It Up

### 1. 🔧 Prerequisites

- AWS account with access to Lambda, DynamoDB, Comprehend, SNS, and CloudWatch
- IAM roles with proper permissions

---

### 2. 🏗️ Set Up AWS Resources

You can set up the services manually or via CloudFormation/SAM. Minimum setup includes:

- **DynamoDB Table**:  
  - Table name: `FeedbackTable`  
  - Primary key: `email`  
  - Attributes: `message`, `sentiment`, `timestamp`

- **SNS Topic**:  
  - Create an email subscription to receive sentiment alerts

- **IAM Role**:  
  - Give Lambda permissions to use DynamoDB, SNS, Comprehend, and CloudWatch

---

### 3. 🧠 Lambda Function Logic

The Lambda function should:

1. Receive feedback via API Gateway (POST request)
2. Run sentiment analysis using Amazon Comprehend
3. Store feedback + sentiment in DynamoDB
4. Trigger an SNS email with the message + sentiment
5. Log all actions to CloudWatch

---

### 4. 🌐 Deploy with API Gateway

Use API Gateway to expose your Lambda as an HTTP endpoint:

- Method: `POST`
- Integration: Lambda Proxy Integration
- Enable CORS if using a frontend HTML form

---

### 5. 🧪 Testing

- Submit the `form.html`
- Check:
  - DynamoDB: Feedback saved with sentiment
  - SNS: Email alert received
  - CloudWatch: Lambda logs generated

---

## 📌 Sample Output

Feedback form (before submission):
![image](https://github.com/user-attachments/assets/59a93a19-6003-4fa6-bde7-5c8fad9b42f8)



Feedback form (after submission):
![image](https://github.com/user-attachments/assets/09126a88-1348-4dfb-921a-2b6bf31ff36e)



Feedback records (viewing all responses):
![image](https://github.com/user-attachments/assets/6ae30489-fe42-48bb-8fdf-bd8597e97c4e)



Email notification for every feedback:
![image](https://github.com/user-attachments/assets/bcddd968-d161-4d09-85d3-e37da69ab536)




---

## 🚧 Future Enhancements

- Add a React dashboard for sentiment trends
- Implement AWS Cognito for user authentication
- Use Step Functions for more complex workflows
- Add multi-language sentiment support

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork.

---

Created by Faiza Reza


