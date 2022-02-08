  
A 6-week training on Production Grade Programming taught by a team of top instructors and industry coaches. 
##Sprints and agile framework##
We simulate the industry environment by running weekly sprints, starting with planning, backlog grooming via clear user stories and effort estimates determined through story points, tracking progress through daily stand-ups, and concluding with demos and retrospective. 
##Project-centric approach##
 Sprints are structured around a central project that the trainees build upon over 6 weeks. 
##Code reviews##
 Trainees improve their code daily based on code reviews from the instructor and the coach. Trainees also practice writing code reviews on other trainees' code repos. 
##Continuous assessment##
 Performance is evaluated after every sprint using metrics that track submitted code for correctness, testability, efficiency, modularity, and documentation quality. Trainees are also assessed on their learning pace, communication skills, and teamwork. 
##Soft skills development##
 Trainees learn to collaborate effectively by working in teams and by openly giving and receiving feedback through code reviews. They receive regular feedback from instructors on communication skills with respect to daily stand-ups, weekly project presentations, email, and documentation writing.
 
##Course Project: An engineer graduating from this course will use infrastructure-as-code (laC) constructs to build and operate a production-grade web application running across multiple AWS Regions. The DevOps engineer will write a RESTful Python application on AWS, use Cl/CD to automate multiple deployment stages (prod vs beta), write unit/integration tests to continuously deploy the application without human intervention, store logs in Cloud Watch, and automate metrics to roll back a deployment in case of service degradation. 
laC built in this course will rely on industry-standard Cloud Development Kit to deploy our infrastructure pieces, Github to version control the software, periodic and event-based Lambda functions to take care of business logic. Code Pipelines will be used to incrementally and safely deploy the code in waves. Each deployment stage will run different kinds of tests to ensure the safe deployment of code.
Our application will use Cloudwatch to store business-critical metrics along with application logs. Apart from test cases, we'll also create Cloudwatch alarms to send a notification if anything goes wrong. We will also build Docker-based API testing clients that will be hosted in Elastic Compute Cloud (EC2) instances and will test the public endpoints built in this project. Other technologies used to build this application will include Lambda, CloudWatch, DynamoDB, API Gateway, SNS, SOS, Cloud9, and S3.

## Course Breakdown

| Sprints  | Learning Objectives |
| ------------- | ------------- |
| Sprint 1  | Project: Use AWS CDK to build a canary in a Lambda function. This canary runs in one AWS Region and measures the availability and latency of a custom list (a json file placed in 53 bucket) of websites. Run the crawler periodically on a 5 min cadence and write <availability, latency> metrics for each website and each run to CloudWatch using CloudWatch's API. Create a CloudWatch Dashboard to monitor website health, and set up alarms when availability or latency falls below prescribed thresholds. Every alarm is also published to SNS/SQS notifications with tags that can be used to filter by metric type. Push the code to versioning control repo. Manage README files and runbooks in markdown on GitHub. 
###Concepts:  
*Introduction to the DevOps Engineer Role and Infrastructure-as-Code (laC) 
* Introduction to AWS: Regions/AZs/Edge Services, Foundational services (EC2, 53, CloudFront), Microservice architecture
* Introduction to the Art of Monitoring Web Applications 
* Learn AWS Services: IAM, Lambda ,Cloud Watch, SNS, SQS 
* Learn Tools: Shell and Scripting, Vim, GitHub |
  
| Sprint 2  | Project: Create multi-stage pipeline having Beta/Gamma and Prod stage using CDK. Deploy the project code in 1 Region. Each stage must have bakeTimes, code-review, and test blockers. Write unit/integration tests for the web crawler. Emit CloudWatch metrics and alarms for the operational health of the web crawler, including memory and time-to-process each crawler run. Automate rollback to the last build if metrics are in alarm. Manage README files and runbooks in markdown on GitHub. 
### Concepts
  * Introduction to Cl/CD 
*Learn AWS services: CodePipeline for build and test, CodeDeploy for CD 
*Integrate AWS CodePipeline with GitHub 
* Learn automated testing using PyTest running 
* Build a release process by writing merge-blocking automated tests for the canary on CodePipeline
*  Build operational CloudWatch metrics for web crawler
*  Write rollback automation allowing rollback to last build 
* Setup beta and prod environments in CodePipeline and deploy using CodeDeploy|
  
 | Sprint 3 | Project:Build a public CRUD API Gateway endpoint for the web crawler to create/read/update/delete the target list containing the list of websites/webpages to crawl. 
First, move the json file from S3 to a database (DynamoDB). Then implement CRUD REST commands on DynamoDB entries. Extend tests in each stage to cover the CRUD operations and DynamoDB read/write time. Write API documentation and commit to GitHub. Manage README files and runbooks in markdown on GitHub. 
###Concepts:  
  * Learn AWS Services: API Gateway, DynamoDB 
  * Write a RESTful API Gateway interface for web crawler CRUD operations 
  * Write a Python Function to implement the business logic of CRUD into DynamoDB
  * Extend tests and prod/beta Cl/CD pipelines in CodeDeploy / CodePipeline 
  * Use Cl/CD to automate multiple deployment stages (prod vs beta) 
 |
  

| Sprint 4  | Project:Build a Front-End user-interface for the CRUD API Gateway using ReacUS. The user interface should allow users to see and search the database (DynamoDB) and should load URLs with pagination. Login should be enabled through React with authentication using AWS Cognito or equivalent OAuth method. The React app can be rendered with an AWS Lambda Function. Use the library of foundational and advanced components and design system in Chakra UI to develop your React application. 
###Concepts:  
*Learn how to create a Front-End app with ReactJS 
  *Learn how to enable authentication using OAuth method 
  * Write accessible React apps using readily available UI libraries  |
  
 | Sprint 5 | Project: Use docker-compose to build API test clients and deploy on an EC2 instance. Build and push API test dockers through CodePipeline. Push API test results into CloudWatch. Setup alarming and notification on API test metrics. Extend tests in each stage. Manage README files and runbooks in markdown on GitHub. 
###Concepts:  
*Introduction to the DevOps Engineer Role and Infrastructure-as-Code (laC) 
* Introduction to AWS: Regions/AZs/Edge Services, Foundational services (EC2, 53, CloudFront), Microservice architecture
* Introduction to the Art of Monitoring Web Applications 
* Learn AWS Services: IAM, Lambda ,Cloud Watch, SNS, SQS 
* Learn Tools: Shell and Scripting, Vim, GitHub |
  
