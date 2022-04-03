FROM public.ecr.aws/lambda/python:3.9-arm64

# Copy function code
COPY main.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler
CMD [ "main.handler" ]
