# Standard library imports
# -

# Third party imports
from aws_cdk import core as cdk, aws_lambda as lambda_

# Local application/library specific imports
# -


class Tests(cdk.Construct):
    def __init__(
        self,
        scope: cdk.Construct,
        construct_id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #### RUBY_2_7 x86
        lambda_.Function(
            scope=self,
            id="ZipRuby27Init1Second",
            code=lambda_.Code.from_asset("lambda/functions/base_ruby"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
            runtime=lambda_.Runtime.RUBY_2_7,
            handler="main.handler",
        )
        # Result:
        # REPORT RequestId: 171b287a-a267-4704-88fb-d992de03863c
        # Duration: 1003.05 ms
        # Billed Duration: 1004 ms
        # Memory Size: 128 MB
        # Max Memory Used: 30 MB
        # Init Duration: 1142.84 ms

        #### RUBY_2_7 arm64
        lambda_.Function(
            scope=self,
            id="ZipRuby27ArmInit1Second",
            code=lambda_.Code.from_asset("lambda/functions/base_ruby"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
            runtime=lambda_.Runtime.RUBY_2_7,
            architecture=lambda_.Architecture.ARM_64,
            handler="main.handler",
        )
        # Result:
        # REPORT RequestId: e8bc61bf-e73b-4571-bef4-734880f4b3ab
        # Duration: 1003.10 ms
        # Billed Duration: 1004 ms
        # Memory Size: 128 MB
        # Max Memory Used: 31 MB
        # Init Duration: 1139.89 ms
