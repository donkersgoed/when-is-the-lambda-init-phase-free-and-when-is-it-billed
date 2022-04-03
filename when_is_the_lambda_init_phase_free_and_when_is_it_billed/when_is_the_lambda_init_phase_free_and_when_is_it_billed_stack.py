"""Module for the main WhenIsTheLambdaInitPhaseFreeAndWhenIsItBilled Stack."""

# Standard library imports
# -

# Third party imports
from aws_cdk import core as cdk

# Local application/library specific imports
from tests.docker.nodejs.tests import Tests as DockerNodeJsTests
from tests.docker.python.tests import Tests as DockerPythonTests
from tests.zip.managed_runtimes.nodejs.tests import Tests as ZipNodeJsTests
from tests.zip.managed_runtimes.python.tests import Tests as ZipPythonTests


class WhenIsTheLambdaInitPhaseFreeAndWhenIsItBilledStack(cdk.Stack):
    """The WhenIsTheLambdaInitPhaseFreeAndWhenIsItBilled Stack."""

    def __init__(
        self,
        scope: cdk.Construct,
        construct_id: str,
        **kwargs,
    ) -> None:
        """Construct a new WhenIsTheLambdaInitPhaseFreeAndWhenIsItBilledStack."""
        super().__init__(scope, construct_id, **kwargs)

        ## DOCKER TESTS
        DockerNodeJsTests(scope=self, construct_id="DockerNodeJsTests")
        DockerPythonTests(scope=self, construct_id="DockerPythonTests")

        ## ZIP TESTS
        ZipNodeJsTests(scope=self, construct_id="ZipNodeJsTests")
        ZipPythonTests(scope=self, construct_id="ZipPythonTests")
        # ZipRubyTests(scope=self, construct_id="ZipRubyTests")
        # ZipJavaTests(scope=self, construct_id="ZipJavaTests")
        # ZipGoTests(scope=self, construct_id="ZipGoTests")
        # ZipDotNetTests(scope=self, construct_id="ZipDotNetTests")
        # ZipCustomRuntimeTests(scope=self, construct_id="ZipCustomRuntimeTests")
