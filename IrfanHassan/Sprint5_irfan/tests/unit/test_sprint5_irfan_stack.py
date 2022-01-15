import aws_cdk as core
import aws_cdk.assertions as assertions

from sprint5_irfan.sprint5_irfan_stack import Sprint5IrfanStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sprint5_irfan/sprint5_irfan_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Sprint5IrfanStack(app, "sprint5-irfan")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
