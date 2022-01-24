##------------Pipeline stack Code------------------------##
from aws_cdk import (
    core,
    pipelines,
    aws_codepipeline_actions as cpactions,
    aws_iam 
)
from sprint5_irfan.sprint5_irfan_stage import Sprint5IrfanStage
class Sprint5IrfanPipelineStack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
########################################################################################################
        pipeline_role=self.create_role()
        iam_=aws_iam.PolicyStatement(resources=['*'],actions=['iam:*'])
        sts_=aws_iam.PolicyStatement(resources=['*'],actions=['sts:*'])
#########  adding source to piepline (GitHub respository) ################################################
        source = pipelines.CodePipelineSource.git_hub(repo_string = "muhammadskipq2021/ProximaCentauri_",branch = "main",
                           authentication = core.SecretValue.secrets_manager("Irfan_sprint2_secretkey"),
                           trigger = cpactions.GitHubTrigger.POLL)
                           

##########  Installing the requirement and Build the Source ##############################################
        synth = pipelines.CodeBuildStep('synth', input= source,
                commands = ["cd IrfanHassan/Sprint5_irfan","pip install aws-cdk.aws_cloudwatch_actions==1.135.0", 
                            "pip install -r requirements.txt ","npm install -g aws-cdk","cdk synth" ],
                            primary_output_directory = "IrfanHassan/Sprint5_irfan/cdk.out",
                            role=pipeline_role,
                            role_policy_statements=[iam_,sts_]
                            )
        pipeline = pipelines.CodePipeline(self,'pipeline',synth=synth)
        
########   Adding Beta Stage with Unit Test and Initgration Test ###########################################
        betaStage =  Sprint5IrfanStage(self, "BetaStag", env = { 'account': '315997497220', 'region': 'us-east-2'})
        test = pipelines.CodeBuildStep('unit_and_Integration_test_',commands=["cd IrfanHassan/Sprint5_irfan", "pip install -r requirements.txt",
        "pip install pytest","pip install requests","pytest unittest"],
            role=pipeline_role,
            role_policy_statements=[iam_,sts_])#,"pytest Intigration"])
        pipeline.add_stage(betaStage)#, pre = [test])
    
        
#######  Addign Prodcution stage with mannaul approval in Pipeline  #######################################3
        prodstage=  Sprint5IrfanStage(self, "ProdStage", env={'account':'315997497220','region': 'us-east-2'} )
        pipeline.add_stage(prodstage, pre=[  pipelines.ManualApprovalStep("PromoteToProd") ])
        
    
    
    def create_role(self):
        role=aws_iam.Role(self,"pipeline-role",
        assumed_by=aws_iam.CompositePrincipal(
            aws_iam.ServicePrincipal("lambda.amazonaws.com"),
            aws_iam.ServicePrincipal("sns.amazonaws.com"),
            aws_iam.ServicePrincipal("codebuild.amazonaws.com")
            ),
            managed_policies=[
            aws_iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSLambdaBasicExecutionRole'),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name('CloudWatchFullAccess'),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess"),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("AwsCloudFormationFullAccess"),        
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMFullAccess"),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("AWSCodePipeline_FullAccess"),
            aws_iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess")
            ])
        return role
       
       
       
       
       
        