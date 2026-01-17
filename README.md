📌 Project Overview (What This Project Is About)

This project demonstrates how to build a real-world serverless API on AWS using:
AWS Lambda (Python backend logic)
API Gateway HTTP API (public endpoint)
IAM (execution role with least privileges)
Terraform (Infrastructure as Code)
The API exposes a /hello endpoint that returns a personalized greeting.
This is a production-grade architecture pattern used across companies for building:
lightweight backend APIs
microservices mobile app backends

internal automation tools

AI endpoints (Bedrock/OpenAI integrations)

event-driven serverless services

The purpose of this project is to demonstrate:

cloud fundamentals

serverless architecture

Infrastructure as Code

debugging AWS services

how to build & deploy a working API using Terraform

                  +-----------------------+
                  |     Client Request    |
                  |  curl / browser / app |
                  +-----------+-----------+
                              |
                              v
                   +----------+-----------+
                   |     API Gateway      |
                   |   HTTP API (/hello)  |
                   +----------+-----------+
                              |
                              v
                      +-------+--------+
                      |    Lambda      |
                      |  Python 3.12   |
                      | app.handler    |
                      +-------+--------+
                              |
                              v
                   +----------+-----------+
                   |      CloudWatch      |
                   |   Logs & Monitoring  |
                   +----------------------+

             (all infrastructure defined with Terraform)

🧠 Common Mistakes & Debugging Lessons

(Real learning from real problems)

This project intentionally documents several real-world mistakes and how they were diagnosed and fixed — this is extremely valuable for junior cloud engineers.

❌ 1. AWS Region Mismatch

Problem:
Resources were deployed to eu-north-1, but the AWS console was opened in us-east-1.

Symptoms:

Lambda appeared "missing"

CloudWatch logs empty

API worked but seemed strange

Fix:
Always match:

Terraform region == AWS Console region


This is one of the most common mistakes in cloud engineering.

❌ 2. Lambda Error: NoneType has no attribute get

Cause:
API Gateway triggered Lambda without query parameters.
event object was None.

Fix:
Add safe fallback:

params = event.get("queryStringParameters") or {}


Lesson:
When Lambda returns Internal Server Error,
→ always check CloudWatch logs first.

❌ 3. GitHub Push Failed Because of .terraform/providers

Cause:
The .terraform/ directory (with a 685MB AWS provider) was accidentally added to Git commit history.

GitHub rejected the push:

GH001: Large files detected


Fix:

Delete local .git

Reinitialize the repo

Push clean history

Lesson:
.gitignore does NOT work retroactively.
If a large file enters commit history → you must rewrite the repo.

❌ 4. Missing .gitignore Entries

Added proper ignore rules:

terraform/.terraform/
terraform.tfstate
terraform.tfstate.backup
lambda.zip
__pycache__/


Lesson:
A clean repo = a professional repo.
Terraform projects must NEVER include state or provider binaries.