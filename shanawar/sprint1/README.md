<h1 align="center">  Sprint 1: Create a web health monitoring application and send notification for alarms.

## Flow Diagram
![image](https://user-images.githubusercontent.com/96059754/150779518-daeef32c-a638-4701-b8e8-fececeed1f0c.png)

 
## Technologies
  * Lambda
  * SNS
  * Cloudwatch
  * S3 Bucket
  * DynamoDB


```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
