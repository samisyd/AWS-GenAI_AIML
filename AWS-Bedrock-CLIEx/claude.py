# Create an IAM user before invoking the bedrock models
# Call aws configure to setup the credentials and region before running the code

import boto3
import json

prompt_data="Act as a Shakespeare and write a poem on Generative AI"

# Replace with the actual ID or ARN of your inference profile
inference_profile_id_or_arn = "arn:aws:bedrock:us-east-1:229704421964:inference-profile/us.anthropic.claude-3-haiku-20240307-v1:0" 

bedrock=boto3.client(service_name="bedrock-runtime")

# Claude 3 uses the Messages API format
payload = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 150,
    "temperature": 0.8,
    "top_p": 0.8,
    "messages": [
        {
            "role": "user",
            "content": prompt_data
        }
    ]
}

body = json.dumps(payload)
#  botocore.errorfactory.ValidationException: An error occurred (ValidationException) when calling the InvokeModel operation:
#  Invocation of model ID anthropic.claude-haiku-4-5-20251001-v1:0 with on-demand throughput isn’t supported. Retry your request with the ID or ARN of an inference profile that contains this model.
model_id = "anthropic.claude-haiku-4-5-20251001-v1:0"
response = bedrock.invoke_model(
    body=body,
    modelId=inference_profile_id_or_arn,
    accept="application/json",
    contentType="application/json",
)

response_body = json.loads(response.get("body").read())
response_text = response_body['content'][0]['text']
print(response_text)