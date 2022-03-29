#!/usr/bin/env python3
"""The main app. Contains all the stacks."""

# Standard library imports
# -

# Third party imports
# -

# Local application/library specific imports
from aws_cdk import core as cdk
from when_is_the_lambda_init_phase_free_and_when_is_it_billed.when_is_the_lambda_init_phase_free_and_when_is_it_billed_stack import WhenIsTheLambdaInitPhaseFreeAndWhenIsItBilledStack

app = cdk.App()
WhenIsTheLambdaInitPhaseFreeAndWhenIsItBilledStack(
    scope=app,
    construct_id="WhenIsTheLambdaInitPhaseFreeAndWhenIsItBilledStack",
)

app.synth()
