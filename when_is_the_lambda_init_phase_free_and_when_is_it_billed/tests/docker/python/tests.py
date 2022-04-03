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

        ##########################
        ### PYTHON OFFICIAL IMAGES
        ##########################

        #### FROM public.ecr.aws/lambda/python:3.7 Multi-architecture base image
        lambda_.DockerImageFunction(
            scope=self,
            id="DockerPython37Init1Second",
            code=lambda_.DockerImageCode.from_image_asset(
                "lambda/functions/python_3_7"
            ),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
        )
        # Result:
        # REPORT RequestId: 2f9093d3-4c10-44f9-aedb-4d1d3ff1ed6f
        # Duration: 1002.25 ms
        # Billed Duration: 2261 ms
        # Memory Size: 128 MB
        # Max Memory Used: 35 MB
        # Init Duration: 1258.24 ms

        #### FROM public.ecr.aws/lambda/python:3.8 Multi-architecture base image
        lambda_.DockerImageFunction(
            scope=self,
            id="DockerPython38Init1Second",
            code=lambda_.DockerImageCode.from_image_asset(
                "lambda/functions/python_3_8"
            ),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
        )
        # Result:
        # REPORT RequestId: 69f92a00-da7b-44aa-a7c6-e0b92f79074a
        # Duration: 1002.07 ms
        # Billed Duration: 2288 ms
        # Memory Size: 128 MB
        # Max Memory Used: 37 MB
        # Init Duration: 1285.01 ms

        #### FROM public.ecr.aws/lambda/python:3.9 Multi-architecture base image
        lambda_.DockerImageFunction(
            scope=self,
            id="DockerPython39Init1Second",
            code=lambda_.DockerImageCode.from_image_asset(
                "lambda/functions/python_3_9"
            ),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
        )
        # Result:
        # REPORT RequestId: e8a09fdb-d97d-47e5-91d0-0346a74342a7
        # Duration: 1001.62 ms
        # Billed Duration: 2150 ms
        # Memory Size: 128 MB
        # Max Memory Used: 35 MB
        # Init Duration: 1148.21 ms

        #### FROM public.ecr.aws/lambda/python:3.9-arm64  Architecture-specific base image
        lambda_.DockerImageFunction(
            scope=self,
            id="DockerPython39Init1SecondArmSpecific",
            code=lambda_.DockerImageCode.from_image_asset(
                "lambda/functions/python_3_9_arm"
            ),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
            architecture=lambda_.Architecture.ARM_64,
        )
        # Result:
        # REPORT RequestId: f2b8482c-a51f-428d-88fe-4abc37a471bb
        # Duration: 1001.65 ms
        # Billed Duration: 2150 ms
        # Memory Size: 128 MB
        # Max Memory Used: 34 MB
        # Init Duration: 1147.77 ms

        ########################
        ### PYTHON ALPINE IMAGES
        ########################

        #### FROM python-alpine
        lambda_.DockerImageFunction(
            scope=self,
            id="DockerPython39AlpineInit1Second",
            code=lambda_.DockerImageCode.from_image_asset(
                "lambda/functions/python_3_9_alpine"
            ),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
        )
        # Result:
        # REPORT RequestId: c79e3bca-577d-433f-b7d3-7cd947bcd51d
        # Duration: 1002.00 ms
        # Billed Duration: 2687 ms
        # Memory Size: 128 MB
        # Max Memory Used: 31 MB
        # Init Duration: 1684.10 ms
