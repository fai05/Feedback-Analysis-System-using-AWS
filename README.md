# Sentiment-analysis-with-AWS
# 📨 AWS Serverless Feedback Analysis System

A fully serverless cloud-native application designed to collect, analyze, and notify customer feedback in real time using AWS services. Built for scalability, low maintenance, and AI-powered insights using sentiment analysis.

---

## 📌 Overview

This project enables users to submit feedback via a simple HTML form. The feedback is processed by an AWS Lambda backend, analyzed for sentiment using Amazon Comprehend, stored in DynamoDB, and relevant stakeholders are notified through Amazon SNS. All activity is logged using Amazon CloudWatch for monitoring and debugging.

---

## 💡 Features

- 📥 Collect feedback via a web form
- 🧠 Analyze message sentiment (Positive, Negative, Neutral, Mixed)
- 📩 Notify team members based on sentiment
- 🗂 Store structured feedback in DynamoDB
- 📊 Monitor logs using CloudWatch
- ⚡️ Completely serverless — scales on demand

---

## 🧱 Architecture Diagram

![Architecture](architecture.png)

---

## 🛠️ Tech Stack & AWS Services Used

- **Frontend**: HTML + HTTP form
- **Backend**: AWS Lambda (Python)
- **Database**: Amazon DynamoDB
- **Sentiment Analysis**: Amazon Comprehend
- **Notifications**: Amazon SNS (Email)
- **Monitoring**: Amazon CloudWatch
- **API Gateway** *(optional)*: To expose Lambda as an endpoint

---


---

## 🚀 How to Set It Up

### 1. 🔧 Prerequisites

- AWS account with access to Lambda, DynamoDB, Comprehend, SNS, and CloudWatch
- IAM roles with proper permissions
- AWS CLI configured locally *(optional for deployment)*

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

### 4. 🌐 Optional: Deploy with API Gateway

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

## 📌 Example Feedback Flow

1. User fills form and submits feedback  
2. Lambda receives it, triggers sentiment analysis  
3. Stores: `{ email, message, sentiment, timestamp }` in DynamoDB  
4. Sends SNS email to stakeholders with:  
   `"User abc@example.com said: 'Loved the product!' — Sentiment: Positive"`  
5. Logs entire process in CloudWatch

---

## 🚧 Future Enhancements

- Add a React dashboard for sentiment trends
- Implement AWS Cognito for user authentication
- Use Step Functions for more complex workflows
- Add multi-language sentiment support

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork and submit a PR.

---

## 📬 Contact

Created by Faiza Reza

