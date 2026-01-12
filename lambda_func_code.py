import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2', region_name='ap-south-1')

def lambda_handler(event, context):

    # Get current IST time
    now_utc = datetime.utcnow()
    now_ist = now_utc + timedelta(hours=5, minutes=30)
    current_time = now_ist.strftime("%H:%M")

    # INSTANCE 1
    if "08:00" <= current_time <= "08:05":
        ec2.start_instances(InstanceIds=["i-0123456789abcdef0"])
        print("Started instance i-0123456789abcdef0")

    elif "21:00" <= current_time <= "21:05":
        ec2.stop_instances(InstanceIds=["i-0123456789abcdef0"])
        print("Stopped instance i-0123456789abcdef0")

    # INSTANCE 2
    elif "09:00" <= current_time <= "09:05":
        ec2.start_instances(InstanceIds=["i-0abcdef1234567890"])
        print("Started instance i-0abcdef1234567890")

    elif "22:00" <= current_time <= "22:05":
        ec2.stop_instances(InstanceIds=["i-0abcdef1234567890"])
        print("Stopped instance i-0abcdef1234567890")

    # INSTANCE 3
    elif "10:30" <= current_time <= "10:35":
        ec2.start_instances(InstanceIds=["i-0fedcba9876543210"])
        print("Started instance i-0fedcba9876543210")

    elif "23:30" <= current_time <= "23:35":
        ec2.stop_instances(InstanceIds=["i-0fedcba9876543210"])
        print("Stopped instance i-0fedcba9876543210")

    else:
        print("No action required at this time")

    return {
        "status": "Executed",
        "current_time_ist": current_time
    }
