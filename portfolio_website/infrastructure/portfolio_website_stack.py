"""AWS CDK stack for my portfolio website."""

from aws_cdk import (
    Stack,
    aws_s3 as s3,
    RemovalPolicy,
    aws_s3_deployment as s3deploy,
    aws_route53 as route53,
    aws_route53_targets as targets,
)
from constructs import Construct


class PortfolioWebsiteStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Provision an S3 bucket
        bucket = s3.Bucket(
            self, "PortfolioWebsiteBucketDev",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            block_public_access=s3.BlockPublicAccess(block_public_policy=False),
            public_read_access=True,
            website_index_document="index.html",
            bucket_name="bigben.codes"
        )

        # Deploy the bucket as a static website
        deployment = s3deploy.BucketDeployment(
            self, "DeployWebsite",
            sources=[s3deploy.Source.asset('./portfolio_website/web-content')],
            destination_bucket=bucket,
        )

        # Provision a DNS record for the website
        record = route53.RecordSet(self, "AliasRecord",
                                   record_name="bigben.codes",
                                   record_type=route53.RecordType.A,
                                   target=route53.RecordTarget.from_alias(targets.BucketWebsiteTarget(bucket)),
                                   zone=route53.HostedZone.from_lookup(self, "HostedZone", domain_name="bigben.codes")
                                   )
