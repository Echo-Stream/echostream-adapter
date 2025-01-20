FROM public.ecr.aws/lambda/python:3.13

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install \
    --disable-pip-version-check \
    --no-cache-dir \
    -r requirements.txt

# Copy function code
COPY function.py ${LAMBDA_TASK_ROOT}

# Set the CMD to our handler
CMD [ "function.handler" ]
