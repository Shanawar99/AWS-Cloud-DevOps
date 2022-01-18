import aws_cdk as core
import aws_cdk.assertions as assertions

from sprint_five_proj.sprint_five_proj_stack import SprintFiveProjStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sprint_five_proj/sprint_five_proj_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SprintFiveProjStack(app, "sprint-five-proj")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
