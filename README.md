# Bite-Sized Serverless: When is the Lambda Init Phase Free, and when is it Billed

This project contains the infrastructure definition used in the article When is the Lambda Init Phase Free, and when is it Billed on Bite-Sized Serverless: https://bitesizedserverless.com/bite/when-is-the-lambda-init-phase-free-and-when-is-it-billed/

The compiled CloudFormation files can be found in the `cdk.out` folder. The Python files for the Lambda functions are placed in `lambda/functions`.

To compile the CloudFormation templates, follow these steps:

1. First create a `virtualenv` with `python3 -m venv .venv`.
2. Then activate the `virtualenv` with `source .venv/bin/activate`.
3. Next, install the required Python packages by running `pip install -r requirements.txt`
4. Then compile CloudFormation by running `cdk synth`. The output will be stored in `cdk.out`.

To deploy the templates to your AWS account, run `cdk deploy`.
