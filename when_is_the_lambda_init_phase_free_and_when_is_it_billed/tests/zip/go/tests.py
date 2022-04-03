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

        #### Go 1.x x86 Managed Runtime
        lambda_.Function(
            scope=self,
            id="ZipGo1Init1Second",
            code=lambda_.Code.from_asset("lambda/functions/base_go/function.zip"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            runtime=lambda_.Runtime.GO_1_X,
            handler="main",
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
        )
        # Result:
        # REPORT RequestId: 1cfdcad0-7d2e-4ff8-9ed8-100888987aac
        # Duration: 1002.60 ms
        # Billed Duration: 1003 ms
        # Memory Size: 128 MB
        # Max Memory Used: 32 MB
        # Init Duration: 1083.49 ms

        #### Go 1.x x86 Amazon Linux 2
        lambda_.Function(
            scope=self,
            id="ZipGoAl2Init1Second",
            code=lambda_.Code.from_asset(
                "lambda/functions/bootstrapped_go/function.zip"
            ),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            runtime=lambda_.Runtime.PROVIDED_AL2,
            handler="main",
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
        )
        # Result:
        # REPORT RequestId: 0f0e127b-f37e-475a-8ad8-ae58770b7bf3
        # Duration: 1001.72 ms
        # Billed Duration: 2067 ms
        # Memory Size: 128 MB
        # Max Memory Used: 18 MB
        # Init Duration: 1064.65 ms

        #### Go 1.x arm64 Amazon Linux 2
        lambda_.Function(
            scope=self,
            id="ZipGoAl2ArmInit1Second",
            code=lambda_.Code.from_asset(
                "lambda/functions/bootstrapped_go_arm/function.zip"
            ),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            runtime=lambda_.Runtime.PROVIDED_AL2,
            architecture=lambda_.Architecture.ARM_64,
            handler="main",
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
        )
        # Result:
        # REPORT RequestId: b4dd2991-fa57-4371-a5a9-70c267749399
        # Duration: 1002.49 ms
        # Billed Duration: 2053 ms
        # Memory Size: 128 MB
        # Max Memory Used: 17 MB
        # Init Duration: 1049.58 ms
