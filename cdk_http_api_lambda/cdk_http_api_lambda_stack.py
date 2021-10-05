from aws_cdk import core as cdk
from aws_cdk.aws_apigatewayv2 import CorsHttpMethod, HttpApi, HttpMethod
from aws_cdk.aws_apigatewayv2_authorizers import HttpLambdaAuthorizer, HttpLambdaResponseType
from aws_cdk.aws_apigatewayv2_integrations import LambdaProxyIntegration
from aws_cdk.aws_lambda import Runtime
from aws_cdk.aws_lambda_python import PythonFunction

APP_NAME = "CdkHttpApiLambda"


class CdkHttpApiLambdaStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        common_lambda_param = {"runtime": Runtime.PYTHON_3_9}
        auth_lambda = PythonFunction(self, f"{APP_NAME}AuthLambda", entry="src/authorizer", **common_lambda_param)
        app_lambda = PythonFunction(self, f"{APP_NAME}AppLambda", entry="src/app", **common_lambda_param)

        authorizer = HttpLambdaAuthorizer(
            authorizer_name="hogehoge_authorizer",
            identity_source=["$request.header.HogeAuthorization"],
            response_types=[HttpLambdaResponseType.SIMPLE],
            handler=auth_lambda,
        )

        lambda_integration = LambdaProxyIntegration(handler=app_lambda)

        http_api = HttpApi(
            self,
            f"{APP_NAME}HttpApi",
            cors_preflight={
                "allow_origins": ["*"],
                "allow_headers": ["*"],
                "allow_methods": [CorsHttpMethod.ANY],
            },
        )
        http_api.add_routes(
            path="/",
            methods=[HttpMethod.ANY],
            integration=lambda_integration,
            authorizer=authorizer,
        )
