"""Module for the main WhenIsTheLambdaInitPhaseFreeAndWhenIsItBilled Stack."""

# Standard library imports
# -

# Third party imports
# -

# Local application/library specific imports
from aws_cdk import core as cdk


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

        # The code that defines your stack goes here
