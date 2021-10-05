#!/usr/bin/env python3
import os

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from cdk_http_api_lambda.cdk_http_api_lambda_stack import CdkHttpApiLambdaStack

app = core.App()
CdkHttpApiLambdaStack(
    app,
    "CdkHttpApiLambdaStack",
)

app.synth()
