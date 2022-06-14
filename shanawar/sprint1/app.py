#!/usr/bin/env python3
import os

from aws_cdk import core as cdk
from aws_cdk import core

from project_shanawar.project_shanawar_stack import ProjectShanawarStack
app = core.App()
ProjectShanawarStack(app, "ProjectShanawarStack",)

app.synth()
