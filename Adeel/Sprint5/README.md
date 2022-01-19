# Sprint 5

## project discription
**__ Use docker-compose to build API test clients using pyresttest and Syntribos. These tests will exercise the web crawler's CRUD endpoint built in the previous sprint. Publish built images to Elastic Container Registry (ECR). Deploy API test clients from Sprint 4 on an EC2 instanceAWS Fargate. Build and push API test dockers through CodePipeline. Push API test results into CloudWatch. Setup alarming and notification on API test metrics. Extend tests in each stage. __**

## Concepts:

* Learn AWS services: ECR 
* Learn docker: DockerFile, Image, Containers. Docker commands [build, start/stop container, deleting container]. 
* Learn container registries: Working with images (Pull/Push), auto-updates to pull new images once published 
* Learn API functional testing framework: pyresttest 
* Learn API security testing framework: Syntribos 
* Learn AWS Services: EC2 and AWS Fargate 
* Extend tests and prod/beta Cl/CD pipelines in CodeDeploy / CodePipeline 

 
## Techonologies

* Pyresttest
* Syntribos
* Docker image
* AWS ECR
* AWS ECS
* AWS Fargate

## project tasks
* Docker image for Pyresttest and syntribos
* Publish the image to ECR.
* Deploy the image to ECS and create EC2 instance
* CloudWatch Alarms for API using docker image

# How to Run

# Docker Image
**Docker file is present on git hub clone it and run the folloing commands**

>docker build -t pyrestful .

#Publish to ECR

**After image build is complete Create a ECR repo with same name and Publish cammands can be fount on ECR**

## Clone

**First clone all the files from git hub repository using this command.**

> git clone https://github.com/adeel2021skipq/ProximaCentauri.git

**Go to project directory**

> cd ProximaCentauri/Adeel/Sprint4/AdeelProject4

## Virtual environment

**Go to virtual environment using command**

> source .venv/bin/activate

## Bootstrap

**Bootstrap the code using that command**

> cdk bootstrap aws://3159974972.20/us-east-2 --qualifier adeel123 --toolkit-stack-name adtoolkit

## Deploy

> cdk deploy AdeelPipelineStack3


##Results 

**Go to cloud watch and see the results for API tests**

