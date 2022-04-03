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

        #################
        # 1 SECOND RUNS #
        #################

        #### PYTHON_3_7 x86
        lambda_.Function(
            scope=self,
            id="ZipPython37Init1Second",
            code=lambda_.Code.from_asset("lambda/functions/base_python"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
            runtime=lambda_.Runtime.PYTHON_3_7,
            handler="main.handler",
        )
        # Result:
        # REPORT RequestId: 06bcabf6-4f97-46d8-9c18-33cbb82d62b8
        # Duration: 1003.04 ms
        # BilledDuration: 1004 ms
        # Memory Size: 128 MB
        # Max Memory Used: 36 MB
        # InitDuration: 1125.03 ms

        #### PYTHON_3_7 arm64
        # PYTHON_3_7 arm64 managed runtime does not exist

        # Result:
        #### PYTHON_3_8 x86
        lambda_.Function(
            scope=self,
            id="ZipPython38Init1Second",
            code=lambda_.Code.from_asset("lambda/functions/base_python"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
            runtime=lambda_.Runtime.PYTHON_3_8,
            handler="main.handler",
        )
        # Result:
        # REPORT RequestId: f6ba6b7a-8d86-4f42-bc2a-466c98fc2d30
        # Duration: 1001.90 ms
        # BilledDuration: 1002 ms
        # Memory Size: 128 MB
        # Max Memory Used: 39 MB
        # InitDuration: 1189.79 ms

        #### PYTHON_3_8 arm64
        lambda_.Function(
            scope=self,
            id="ZipPython38Init1SecondArm",
            code=lambda_.Code.from_asset("lambda/functions/base_python"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
            runtime=lambda_.Runtime.PYTHON_3_8,
            handler="main.handler",
            architecture=lambda_.Architecture.ARM_64,
        )
        # Result:
        # REPORT RequestId: 66417377-908a-4b60-8211-041158dc8faf
        # Duration: 1001.59 ms
        # BilledDuration: 1002 ms
        # Memory Size: 128 MB
        # Max Memory Used: 38 MB
        # InitDuration: 1108.83 ms

        # Result:
        #### PYTHON_3_9 x86
        lambda_.Function(
            scope=self,
            id="ZipPython39Init1Second",
            code=lambda_.Code.from_asset("lambda/functions/base_python"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="main.handler",
        )
        # Result:
        # REPORT RequestId: d77efa0f-df9c-4a3c-98b7-f04cde2c354b
        # Duration: 1002.54 ms
        # BilledDuration: 1003 ms
        # Memory Size: 128 MB
        # Max Memory Used: 36 MB
        # InitDuration: 1101.84 ms

        #### PYTHON_3_9 x86 with Internal Extension
        extension_layer = lambda_.LayerVersion(
            scope=self,
            id="ZipPython39InternalExtensionInit1SecondLayer",
            code=lambda_.Code.from_asset("lambda/extensions/python_internal"),
        )

        lambda_.Function(
            scope=self,
            id="ZipPython39InternalExtensionInit1Second",
            code=lambda_.Code.from_asset("lambda/functions/base_python"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
                "AWS_LAMBDA_EXEC_WRAPPER": "/opt/sleepwrapper",
            },
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="main.handler",
            layers=[extension_layer],
        )
        # Result:
        # REPORT RequestId: 6897f517-31db-4bf0-8fd9-5abd2863dee5
        # Duration: 1001.82 ms
        # Billed Duration: 1002 ms
        # Memory Size: 128 MB
        # Max Memory Used: 37 MB
        # Init Duration: 2124.46 ms

        #### PYTHON_3_9 x86 with External Extension
        extension_layer = lambda_.LayerVersion(
            scope=self,
            id="ZipPython39ExternalExtensionInit1SecondLayer",
            code=lambda_.Code.from_asset("lambda/extensions/python_external"),
        )

        lambda_.Function(
            scope=self,
            id="ZipPython39ExternalExtensionInit1Second",
            code=lambda_.Code.from_asset("lambda/functions/base_python"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="main.handler",
            layers=[extension_layer],
        )
        # Result:
        # REPORT RequestId: e7e42165-fee9-4017-b19f-a7a28129cb8c
        # Duration: 1002.16 ms
        # Billed Duration: 1003 ms
        # Memory Size: 128 MB
        # Max Memory Used: 60 MB
        # Init Duration: 2509.05 ms

        #### PYTHON_3_9 arm64
        lambda_.Function(
            scope=self,
            id="ZipPython39Init1SecondArm",
            code=lambda_.Code.from_asset("lambda/functions/base_python"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "1",
                "HANDLER_SLEEP": "1",
            },
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="main.handler",
            architecture=lambda_.Architecture.ARM_64,
        )
        # Result:
        # REPORT RequestId: 43563f23-7568-4eaa-8f63-62580a6810c9
        # Duration: 1001.86 ms
        # Billed Duration: 1002 ms
        # Memory Size: 128 MB
        # Max Memory Used: 36 MB
        # Init Duration: 1096.78 ms

        ##################
        # 10 SECOND RUNS #
        ##################

        #### PYTHON_3_7 x86
        lambda_.Function(
            scope=self,
            id="ZipPython37Init10Seconds",
            code=lambda_.Code.from_asset("lambda/functions/base_python"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "10",
                "HANDLER_SLEEP": "1",
            },
            runtime=lambda_.Runtime.PYTHON_3_7,
            handler="main.handler",
        )
        # Result:
        # REPORT RequestId: e8b971ad-a58a-4c66-b392-014de692c294
        # Duration: 12100.60 ms
        # Billed Duration: 12101 ms
        # Memory Size: 128 MB
        # Max Memory Used: 11 MB

        #### PYTHON_3_7 arm64
        # PYTHON_3_7 arm64 managed runtime does not exist

        # Result:
        #### PYTHON_3_8 x86
        lambda_.Function(
            scope=self,
            id="ZipPython38Init10Seconds",
            code=lambda_.Code.from_asset("lambda/functions/base_python"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "10",
                "HANDLER_SLEEP": "1",
            },
            runtime=lambda_.Runtime.PYTHON_3_8,
            handler="main.handler",
        )
        # Result:
        # REPORT RequestId: 7e8b2086-6ca9-4e66-9e40-48785092d3cd
        # Duration: 12121.07 ms
        # Billed Duration: 12122 ms
        # Memory Size: 128 MB
        # Max Memory Used: 11 MB

        #### PYTHON_3_8 arm64
        lambda_.Function(
            scope=self,
            id="ZipPython38Init10SecondsArm",
            code=lambda_.Code.from_asset("lambda/functions/base_python"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "10",
                "HANDLER_SLEEP": "1",
            },
            runtime=lambda_.Runtime.PYTHON_3_8,
            handler="main.handler",
            architecture=lambda_.Architecture.ARM_64,
        )
        # Result:
        # REPORT RequestId: 19243617-0440-41db-bb8f-6f4e64127b42
        # Duration: 12107.96 ms
        # Billed Duration: 12108 ms
        # Memory Size: 128 MB
        # Max Memory Used: 11 MB

        # Result:
        #### PYTHON_3_9 x86
        lambda_.Function(
            scope=self,
            id="ZipPython39Init10Seconds",
            code=lambda_.Code.from_asset("lambda/functions/base_python"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "10",
                "HANDLER_SLEEP": "1",
            },
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="main.handler",
        )
        # Result:
        # REPORT RequestId: 4a1b71d4-295c-42f4-ad33-a1e98e0327ba
        # Duration: 12012.99 ms
        # Billed Duration: 12013 ms
        # Memory Size: 128 MB
        # Max Memory Used: 11 MB

        #### PYTHON_3_9 arm64
        lambda_.Function(
            scope=self,
            id="ZipPython39Init10SecondsArm",
            code=lambda_.Code.from_asset("lambda/functions/base_python"),
            memory_size=128,
            timeout=cdk.Duration.minutes(1),
            environment={
                "INIT_SLEEP": "10",
                "HANDLER_SLEEP": "1",
            },
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="main.handler",
            architecture=lambda_.Architecture.ARM_64,
        )
        # Result:
        # REPORT RequestId: 5321a4c5-4639-4049-9394-501141a716ac
        # Duration: 11937.29 ms
        # Billed Duration: 11938 ms
        # Memory Size: 128 MB
        # Max Memory Used: 10 MB
