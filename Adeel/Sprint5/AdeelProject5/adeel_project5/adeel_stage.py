##########################Importing All the nessearry libraries#######################################
from aws_cdk import (
    core as cdk,
    aws_lambda as lambda_,
    aws_events as event_,
    aws_events_targets as targets_,
    aws_iam,
    aws_cloudwatch as cloudwatch_,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions_,
    aws_cloudwatch_actions as actions_,
    aws_dynamodb as db
)
from adeel_project5.adeel_project5_stack import AdeelProject5Stack
  
class AdeelStage(cdk.Stage):

    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
      
        adeel_project5_stack = AdeelProject5Stack(self , 'AdeelStack')
        