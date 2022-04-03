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

        #### NodeJS 12 x86
        lambda_.Function(
            scope=self,
            id="ZipNodeJs12Init1Second",
            code=lambda_.Code.from_asset("lambda/functions/base_nodejs"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            runtime=lambda_.Runtime.NODEJS_12_X,
            handler="main.handler",
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
        )
        # Result: REPORT RequestId: bc3405d6-db99-44e7-a74c-3294c4089d5e
        # Duration: 1031.01 ms
        # Billed Duration: 1032 ms
        # Memory Size: 128 MB
        # Max Memory Used: 60 MB
        # Init Duration: 1152.58 ms

        #### NodeJS 12 arm64
        lambda_.Function(
            scope=self,
            id="ZipNodeJs12Init1SecondArm",
            code=lambda_.Code.from_asset("lambda/functions/base_nodejs"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            runtime=lambda_.Runtime.NODEJS_12_X,
            handler="main.handler",
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
            architecture=lambda_.Architecture.ARM_64,
        )
        # Result: REPORT RequestId: 4fb4bbd6-fe12-44f9-b89f-0322ac082f22
        # Duration: 1019.79 ms
        # Billed Duration: 1020 ms
        # Memory Size: 128 MB
        # Max Memory Used: 59 MB
        # Init Duration: 1144.01 ms

        #### NodeJS 14 x86
        lambda_.Function(
            scope=self,
            id="ZipNodeJs14Init1Second",
            code=lambda_.Code.from_asset("lambda/functions/base_nodejs"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            runtime=lambda_.Runtime.NODEJS_14_X,
            handler="main.handler",
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
        )
        # Result:
        # REPORT RequestId: ef945c24-7755-4fca-9f2f-62578fc489c9
        # Duration: 1077.13 ms
        # Billed Duration: 1078 ms
        # Memory Size: 128 MB
        # Max Memory Used: 62 MB
        # Init Duration: 1273.41 ms

        #### NodeJS 14 arm64
        lambda_.Function(
            scope=self,
            id="ZipNodeJs14Init1SecondArm",
            code=lambda_.Code.from_asset("lambda/functions/base_nodejs"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            runtime=lambda_.Runtime.NODEJS_14_X,
            handler="main.handler",
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
            architecture=lambda_.Architecture.ARM_64,
        )
        # Result:
        # REPORT RequestId: 8ffc3890-7ddf-4170-b90d-943c21e87237
        # Duration: 1011.18 ms
        # Billed Duration: 1012 ms
        # Memory Size: 128 MB
        # Max Memory Used: 61 MB
        # Init Duration: 1156.92 ms
