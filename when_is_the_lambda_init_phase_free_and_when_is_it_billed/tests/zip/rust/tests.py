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

        #### Rust x86 Amazon Linux 2
        lambda_.Function(
            scope=self,
            id="ZipRustAl2Init1Second",
            code=lambda_.Code.from_asset(
                "lambda/functions/bootstrapped_rust/function.zip"
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
        # REPORT RequestId: e9a45ab3-9641-403c-a903-e6872f8efb96
        # Duration: 1002.13 ms
        # Billed Duration: 2027 ms
        # Memory Size: 128 MB
        # Max Memory Used: 13 MB
        # Init Duration: 1023.89 ms
