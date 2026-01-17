# AWS Serverless API (Lambda + API Gateway + Terraform)

A simple serverless HTTP API built with **AWS Lambda**, **API Gateway**, and **Terraform**.  
The project demonstrates how to deploy a real backend endpoint on AWS using Infrastructure as Code.

---

## 🚀 Features

- Serverless API endpoint: `GET /hello?name=Jonas`
- Python Lambda function (AWS Lambda)
- HTTP API (API Gateway v2)
- IAM execution role with least privileges
- Full deployment using Terraform
- Logs and debugging via CloudWatch

---

## 📐 Architecture

```
Client → API Gateway → Lambda → CloudWatch Logs
```

---

## 🧪 Test the API

Example request:

```
curl "https://your-api-url/hello?name=Jonas"
```

Response:

```
Hello, Jonas! Your serverless API is running.
```

---

## 🛠 Deployment (Terraform)

```
terraform init
terraform apply
```

Destroy:

```
terraform destroy
```

---

## 🔧 Tech Stack

- AWS Lambda (Python 3.12)
- Amazon API Gateway (HTTP API)
- AWS IAM
- Terraform

---

## 📚 What I Learned

- Deploying serverless APIs using Terraform  
- IAM roles & permissions  
- Lambda debugging with CloudWatch  
- Handling request parameters in API Gateway  
- Fixing region mismatches (eu-north-1 vs us-east-1)  
- Keeping Terraform repos clean (.terraform, tfstate, zip files ignored)

---

## 👤 Author

**Andrius Zemaitis**  
Junior Cloud / Platform Engineer (Oslo)
