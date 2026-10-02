import boto3

s3 = boto3.client("s3")
ec2 = boto3.client("ec2")


def create_bucket():
    bucket_name = input("Enter unique S3 bucket name: ")

    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                "LocationConstraint": "ap-south-1"
            }
        )
        print("Bucket created successfully!")

    except Exception as e:
        print("Error:", e)


def upload_file():
    bucket_name = input("Enter S3 bucket name: ")
    file_name = input("Enter file name: ")

    try:
        s3.upload_file(file_name, bucket_name, file_name)
        print("File uploaded successfully!")

    except Exception as e:
        print("Error:", e)


def list_buckets():
    try:
        response = s3.list_buckets()

        print("\nS3 Buckets:")
        for bucket in response["Buckets"]:
            print(bucket["Name"])

    except Exception as e:
        print("Error:", e)


def list_instances():
    try:
        response = ec2.describe_instances()

        print("\nEC2 Instances:")

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                print("Instance ID:", instance["InstanceId"])
                print("State:", instance["State"]["Name"])
                print("Type:", instance["InstanceType"])
                print("--------------------")

    except Exception as e:
        print("Error:", e)


def launch_instance():
    ami_id = input("Enter AMI ID: ")
    instance_type = input("Enter instance type: ")

    try:
        response = ec2.run_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            MinCount=1,
            MaxCount=1
        )

        instance_id = response["Instances"][0]["InstanceId"]

        print("EC2 launched successfully!")
        print("Instance ID:", instance_id)

    except Exception as e:
        print("Error:", e)


def stop_instance():
    instance_id = input("Enter EC2 Instance ID: ")

    try:
        ec2.stop_instances(
            InstanceIds=[instance_id]
        )

        print("Stop request sent successfully!")

    except Exception as e:
        print("Error:", e)


def terminate_instance():
    instance_id = input("Enter EC2 Instance ID: ")

    confirmation = input("Type YES to confirm termination: ")

    if confirmation == "YES":

        try:
            ec2.terminate_instances(
                InstanceIds=[instance_id]
            )

            print("Termination request sent successfully!")

        except Exception as e:
            print("Error:", e)

    else:
        print("Termination cancelled.")


while True:

    print()
    print("==============================")
    print("      AWS CLOUD AUTOMATION")
    print("==============================")
    print("1. Create S3 Bucket")
    print("2. Upload File to S3")
    print("3. List S3 Buckets")
    print("4. Launch EC2 Instance")
    print("5. List EC2 Instances")
    print("6. Stop EC2 Instance")
    print("7. Terminate EC2 Instance")
    print("8. Exit")
    print("==============================")

    choice = input("Choice: ")

    if choice == "1":
        create_bucket()

    elif choice == "2":
        upload_file()

    elif choice == "3":
        list_buckets()

    elif choice == "4":
        launch_instance()

    elif choice == "5":
        list_instances()

    elif choice == "6":
        stop_instance()

    elif choice == "7":
        terminate_instance()

    elif choice == "8":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")