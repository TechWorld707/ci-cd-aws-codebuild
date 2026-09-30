from constructs import Construct
from aws_cdk import RemovalPolicy, Stack, aws_ecr as ecr


class EcrStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.ecr = ecr.Repository(
            self,
            "hello-app",
            removal_policy=RemovalPolicy.DESTROY,
        )

    @property
    def ecr_data(self) -> ecr.Repository:
        return self.ecr
