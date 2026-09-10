# AI Self-Adaptive VPC Health Report

An AWS-based cloud monitoring and infrastructure health reporting project that analyzes Amazon CloudWatch metrics and generates rule-based recommendations for infrastructure adaptation.

## Project Overview

Cloud environments require continuous monitoring to identify performance and resource-related issues. This project was developed to monitor the health of an AWS VPC environment by collecting infrastructure metrics through Amazon CloudWatch and evaluating them using a Python-based monitoring engine.

The system analyzes infrastructure conditions and generates recommendations such as:

* Scale Out
* Scale In
* Increase Storage
* High-Traffic Investigation

The generated infrastructure health reports are stored in Amazon S3 for centralized access.

## Main Objective

The main objective of this project is to provide an automated **infrastructure health visibility and recommendation layer** that evaluates AWS monitoring data and helps identify conditions where infrastructure adaptation may be required.

The project focuses on monitoring and recommendation rather than replacing AWS Auto Scaling itself.

## Architecture

```text
AWS Infrastructure
       |
       v
Amazon CloudWatch
       |
       v
Python Monitoring Engine
       |
       +----------------------+
       |                      |
       v                      v
Metric Analysis        Health Evaluation
       |                      |
       +----------+-----------+
                  |
                  v
        Adaptation Recommendation
                  |
       +----------+----------+-------------+
       |                     |             |
       v                     v             v
   Scale Out             Scale In    Storage Alert
                                  |
                                  v
                         Health Report
                                  |
                                  v
                             Amazon S3
```

## Technologies Used

| Technology        | Purpose                               |
| ----------------- | ------------------------------------- |
| Amazon EC2        | Compute infrastructure                |
| Amazon VPC        | Network environment                   |
| Amazon CloudWatch | Infrastructure monitoring and metrics |
| Amazon S3         | Storage for generated health reports  |
| Python            | Monitoring and decision engine        |
| Boto3             | Python integration with AWS services  |

## Key Features

### 1. CloudWatch Metric Analysis

The Python monitoring engine retrieves infrastructure metrics from Amazon CloudWatch and evaluates the health of the AWS environment.

The monitoring logic considers metrics such as:

* CPU utilization
* Memory utilization
* Disk utilization
* Network activity

### 2. Infrastructure Health Evaluation

The collected metrics are evaluated against predefined rules to determine the current infrastructure condition.

### 3. Adaptation Recommendations

Based on the evaluated conditions, the system generates recommendations including:

* Scale Out
* Scale In
* Increase Storage
* High-Traffic Investigation

### 4. Automated Health Reports

The monitoring engine generates infrastructure health reports containing the evaluated conditions and corresponding recommendations.

### 5. Amazon S3 Storage

Generated reports are stored in Amazon S3, providing centralized access to the monitoring results.

## Project Workflow

1. AWS infrastructure generates operational metrics.
2. Amazon CloudWatch collects monitoring data.
3. The Python monitoring engine retrieves the required metrics using Boto3.
4. The collected metrics are evaluated using predefined rules.
5. The system determines the infrastructure health condition.
6. An adaptation recommendation is generated.
7. A health report is created.
8. The generated report is stored in Amazon S3.

## Project Screenshots

### AWS Infrastructure

![AWS Infrastructure](screenshots/aws-vpc.png)

### CloudWatch Metrics

![CloudWatch Metrics](screenshots/cloudwatch-metrics.png)

### Infrastructure Recommendation

![Scale Out Recommendation](screenshots/scale-out.png)

### Generated Health Report

![Health Report](screenshots/health-report.png)

### Amazon S3 Report Storage

![S3 Report](screenshots/s3-report.png)

## Project Outcomes

This project provided practical experience with:

* AWS cloud infrastructure monitoring
* Amazon CloudWatch metrics
* Amazon EC2
* Amazon VPC
* Amazon S3
* Python-based AWS automation
* Boto3
* Rule-based infrastructure evaluation
* Cloud resource monitoring
* Automated reporting

## Repository Structure

```text
AI-Self-Adaptive-VPC-Health-Report/
│
├── README.md
├── src/
├── config/
├── screenshots/
├── reports/
├── requirements.txt
└── .gitignore
```

## Disclaimer

This project was developed as a cloud computing project for learning and practical implementation of AWS monitoring and infrastructure health evaluation concepts.

The recommendations generated by the system are intended as a monitoring and decision-support layer and do not replace AWS-native scaling or infrastructure management services.
