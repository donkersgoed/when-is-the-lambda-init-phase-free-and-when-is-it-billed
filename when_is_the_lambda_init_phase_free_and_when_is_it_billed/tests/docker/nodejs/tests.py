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
        ### NODEJS OFFICIAL IMAGES
        ##########################

        #### FROM public.ecr.aws/lambda/nodejs:12 Multi-architecture base image
        lambda_.DockerImageFunction(
            scope=self,
            id="DockerNodeJs12Init1Second",
            code=lambda_.DockerImageCode.from_image_asset(
                "lambda/functions/docker_nodejs_12"
            ),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
        )
        # Result:
        # REPORT RequestId: 4e5f22d1-d064-4992-bd7b-fbccc0d98b82
        # Duration: 1049.63 ms
        # Billed Duration: 2344 ms
        # Memory Size: 128 MB
        # Max Memory Used: 59 MB
        # Init Duration: 1293.83 ms

        #### FROM public.ecr.aws/lambda/nodejs:14 Multi-architecture base image
        lambda_.DockerImageFunction(
            scope=self,
            id="DockerNodeJs14Init1Second",
            code=lambda_.DockerImageCode.from_image_asset(
                "lambda/functions/docker_nodejs_14"
            ),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
        )
        # Result:
        # REPORT RequestId: baa0af59-2c6e-4d06-a694-12daff71585e
        # Duration: 1058.15 ms
        # Billed Duration: 2366 ms
        # Memory Size: 128 MB
        # Max Memory Used: 61 MB
        # Init Duration: 1307.68 ms
