import pytest
from aws_cdk import core
#import aws_cdk.assertions as assertions
from sprint5_irfan.sprint5_irfan_stack import Sprint5IrfanStack
app=core.App()
Sprint5IrfanStack(app, 'Stack')
template=app.synth().get_stack_by_name('Stack').template
#unit test to check number of dynamo DB table 
def test_dynamodb():
    dynamodb_table = [resource for resource in template['Resources'].values()  if resource['Type']=="AWS::DynamoDB::Table"]
    assert len(dynamodb_table)>=2
    #assert 2==2  #
    #
    


    
    