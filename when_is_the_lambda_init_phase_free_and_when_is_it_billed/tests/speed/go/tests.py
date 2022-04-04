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

        #### FROM public.ecr.aws/lambda/go:1
        lambda_.DockerImageFunction(
            scope=self,
            id="GoSpeedTestDocker",
            code=lambda_.DockerImageCode.from_image_asset(
                "lambda/functions/speedtest_go_docker"
            ),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
        )

        #### Go 1.x x86 Managed Runtime
        lambda_.Function(
            scope=self,
            id="GoSpeedTestZipX86",
            code=lambda_.Code.from_asset(
                "lambda/functions/speedtest_go_x86_managed/function.zip"
            ),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            runtime=lambda_.Runtime.GO_1_X,
            handler="main",
        )

        #### Go 1.x x86 Amazon Linux 2
        lambda_.Function(
            scope=self,
            id="GoSpeedTestZipX86AL2",
            code=lambda_.Code.from_asset(
                "lambda/functions/speedtest_go_x86/function.zip"
            ),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            runtime=lambda_.Runtime.PROVIDED_AL2,
            handler="main",
        )

        #### Go 1.x arm64 Amazon Linux 2
        lambda_.Function(
            scope=self,
            id="GoSpeedTestZipArm64",
            code=lambda_.Code.from_asset(
                "lambda/functions/speedtest_go_arm64/function.zip"
            ),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            runtime=lambda_.Runtime.PROVIDED_AL2,
            architecture=lambda_.Architecture.ARM_64,
            handler="main",
        )
