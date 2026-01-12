# 🚀 Stop and Start EC2 Instances Using AWS Lambda & EventBridge

This project demonstrates how to **automatically start and stop multiple EC2 instances** using **AWS Lambda (Python)** and **Amazon EventBridge scheduled rules**.  
It helps in **cost optimization** by running instances only during required time periods.

---

## 📌 Project Objective
- Automate **start and stop operations** for EC2 instances
- Schedule actions using **cron expressions**
- Reduce AWS cost for non-production environments

---

## 🛠️ AWS Services Used
- Amazon EC2
- AWS Lambda
- Amazon EventBridge
- AWS IAM

---

## 🧩 Architecture Overview
1. EC2 instances are created
2. Lambda function manages start/stop logic
3. EventBridge triggers Lambda using scheduled rules
4. IAM Role provides EC2 permissions to Lambda

---

## 🪜 Step-by-Step Implementation

### Step 1: Create EC2 Instances
- Launch **3 EC2 instances**
- Configure instance type, key pair, and security group as required

---

### Step 2: Create IAM Role for Lambda
- Create an IAM Role
- Attach policy: **AmazonEC2FullAccess**
- This role will be used by the Lambda function

---

### Step 3: Create Lambda Function
- Go to **AWS Lambda → Create function**
- Select:
  - Runtime: **Python 3.14**
  - Execution role: **Use existing role**
  - Select the IAM role created earlier

---

### Step 4: Add Lambda Code
- Paste the Python code to:
  - Start EC2 instances
  - Stop EC2 instances
- Update:
  - **Region**
  - **Instance IDs**
  - **Timing logic**

---

### Step 5: Deploy & Test Lambda
- Click **Deploy**
- Create a **Test Event**
- Run the test to verify instance start/stop behavior

---

### Step 6: Create EventBridge Scheduled Rule (Start)
- Go to **Amazon EventBridge**
- Create a **Scheduled Rule**
- Enter rule name (example: `start-ec2-rule`)
- Add cron expression for start time

⚠️ Note: Use `?` in either **Day-of-month** or **Day-of-week**

---

### Step 7: Select Target
- Target: **Lambda function**
- Select Lambda ARN
- Create a new execution role for EventBridge

---

### Step 8: Create Stop Rule
- Repeat EventBridge steps
- Create another scheduled rule to **stop EC2 instances**
- Use appropriate cron timing

---

### Step 9: Add Rules as Triggers
- Open Lambda function
- Go to **Configuration → Triggers**
- Add EventBridge rules (start & stop)
- Repeat for all instance schedules

---

### Step 10: Update Lambda Configuration
- Increase **Timeout** from `3 sec` to `30 sec`
- Save changes

---

### Step 11: Add Environment Variable
- Go to **Environment Variables**
- Add:
  - Key: `TZ`
  - Value: `UTC`

---

## ✅ Final Output
- EC2 instances **stop automatically**
- EC2 instances **start automatically at scheduled time**
- Fully automated and serverless solution

---

## 📈 Use Case
- Development environments
- Testing servers
- Office-hours-based EC2 usage

---

## 👨‍💻 Author
**Arya Kadam**

---

## 📎 Notes
- Ensure correct region and instance IDs
- Cron timings must be in **UTC**
- Permissions are critical for Lambda execution

## 📂 Source Code
The complete AWS Lambda function code used in this project is available in the repository as:

[`lambda_func_code.py`](./lambda_func_code.py)
