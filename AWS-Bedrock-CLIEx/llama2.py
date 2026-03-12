import boto3
import json

prompt_data="""
Act as a Shakespeare and write a poem on Genertaive AI
"""

# Replace with the actual ID or ARN of your inference profile
inference_profile_id_or_arn = "arn:aws:bedrock:us-east-1:229704421964:inference-profile/us.meta.llama3-2-1b-instruct-v1:0" 

bedrock=boto3.client(service_name="bedrock-runtime")

payload={
    "prompt":"[INST]"+ prompt_data +"[/INST]",
    "max_gen_len":130,
    "temperature":0.5,
    "top_p":0.9
}
body=json.dumps(payload)
# model_id="meta.llama2-70b-chat-v1"
model_id="meta.llama3-2-1b-instruct-v1:0"
response=bedrock.invoke_model(
    body=body,
    modelId=inference_profile_id_or_arn,
    accept="application/json",
    contentType="application/json"
)

response_body=json.loads(response.get("body").read())
repsonse_text=response_body['generation']
print(repsonse_text)