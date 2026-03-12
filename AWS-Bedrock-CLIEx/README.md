# AWS Bedrock Examples

This repository contains Python examples demonstrating how to use Amazon Bedrock to interact with various AI models, including text generation with Claude and Llama models, and image generation with Stable Diffusion (Titan Image Generator).

## Prerequisites

Before running these examples, ensure you have:

1. **AWS Account**: An active AWS account with access to Amazon Bedrock.
2. **IAM User**: Create an IAM user with the necessary permissions for Bedrock. The user should have policies like `AmazonBedrockFullAccess` or equivalent.
3. **AWS CLI**: Install and configure the AWS CLI with your credentials.
4. **Python Environment**: Python 3.13 or higher.

### Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure AWS Credentials**:
   Run the following command and provide your AWS access key, secret key, and default region (e.g., us-east-1):
   ```bash
   aws configure
   ```

3. **Enable Bedrock Models**: Ensure the required models are enabled in your AWS Bedrock console:
   - Anthropic Claude (e.g., claude-3-haiku)
   - Meta Llama (e.g., llama3-2-1b-instruct)
   - Amazon Titan Image Generator

## Files Overview

- `main.py`: A simple entry point script.
- `claude.py`: Example using Anthropic Claude model for text generation.
- `llama2.py`: Example using Meta Llama model for text generation.
- `stablediffusion.py`: Example using Amazon Titan Image Generator for image creation.
- `requirements.txt`: Python dependencies.
- `pyproject.toml`: Project configuration.

## Usage

### Text Generation with Claude

Run the Claude example to generate a Shakespearean poem about Generative AI:

```bash
python claude.py
```

This script uses the Claude 3 Haiku model via an inference profile to generate text.

### Text Generation with Llama

Run the Llama example for similar text generation:

```bash
python llama2.py
```

This uses the Llama 3.2 1B Instruct model.

### Image Generation with Stable Diffusion

Generate an image using the Titan Image Generator:

```bash
python stablediffusion.py
```

This creates a stylized image of a cute cat and saves it to the `output/` directory.

## Notes

- Update the `inference_profile_id_or_arn` in the scripts with your actual inference profile ARN from AWS Bedrock.
- The models used may incur costs based on your AWS usage.
- Ensure your region supports the selected models.
