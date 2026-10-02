\# AWS Cloud Automation using Python and Boto3



\## 1. Project Overview



This project automates common AWS resource management tasks using Python and Boto3 (AWS SDK for Python).



The application provides a simple command-line interface (CLI) to perform S3 and EC2 operations without manually performing every operation through the AWS Management Console.



\---



\## 2. Objective



The objectives of this project are:



\- Automate AWS resource management using Python.

\- Learn how to use Boto3 with AWS services.

\- Automate Amazon S3 bucket and file operations.

\- Automate Amazon EC2 instance operations.

\- Reduce repetitive manual work.

\- Understand how Python applications communicate with AWS APIs.



\---



\## 3. AWS Services Used



\- Amazon S3

\- Amazon EC2

\- AWS IAM

\- AWS CLI



\---



\## 4. Technologies Used



\- Python 3.14

\- Boto3

\- PowerShell

\- Visual Studio Code

\- AWS CLI



\---



\## 5. Project Features



The application provides the following menu options:



1\. Create S3 Bucket

2\. Upload File to S3

3\. List S3 Buckets

4\. Launch EC2 Instance

5\. List EC2 Instances

6\. Stop EC2 Instance

7\. Terminate EC2 Instance

8\. Exit



\---



\## 6. Project Architecture



```text

&#x20;               Python Application

&#x20;                      |

&#x20;                      | Boto3

&#x20;                      |

&#x20;               AWS API Services

&#x20;                /            \\

&#x20;               /              \\

&#x20;         Amazon S3          Amazon EC2

&#x20;            |                   |

&#x20;      Bucket/File          EC2 Instances

&#x20;      Operations            Operations

