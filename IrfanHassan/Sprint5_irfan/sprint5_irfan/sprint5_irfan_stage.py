from aws_cdk import core as cdk

from sprint5_irfan.sprint5_irfan_stack import Sprint5IrfanStack

class Sprint5IrfanStage(cdk.Stage):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        irfan_stack =  Sprint5IrfanStack(self,'Sprint5IrfanStack')