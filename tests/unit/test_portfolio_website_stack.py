import aws_cdk as core
import aws_cdk.assertions as assertions

from portfolio_website.portfolio_website_stack import PortfolioWebsiteStack

# example tests. To run these tests, uncomment this file along with the example
# resource in portfolio_website/portfolio_website_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PortfolioWebsiteStack(app, "portfolio-website")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
