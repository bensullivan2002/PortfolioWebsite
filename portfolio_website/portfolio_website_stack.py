from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3,
    RemovalPolicy,
    # aws_sqs as sqs,
)
from constructs import Construct


class PortfolioWebsiteStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(
            self, "PortfolioWebsiteBucketDev",
            versioned=True, removal_policy=RemovalPolicy.DESTROY, auto_delete_objects=True,  # public_read_access=True,
        )

        # example resource
        # queue = sqs.Queue(
        #     self, "PortfolioWebsiteQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
