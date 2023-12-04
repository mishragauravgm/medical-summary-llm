# Medical Summarization using T5 LLM

## Overview

This project focuses on utilizing the T5 LLM through Hugging Face's Transformer library to generate concise and accurate summaries of medical texts. Leveraging AWS Sagemaker and Lambda, the model was deployed, enabling seamless summarization of medical documents at scale.

### Features

- **T5 LLM Architecture**: Implemented a Longformer Language Model (LLM) powered by T5 for handling long medical texts.
- **AWS Sagemaker Integration**: Utilized Sagemaker to build and train the model, ensuring efficient and scalable ML workflows.
- **AWS Lambda Deployment**: Deployed the model using AWS Lambda for real-time medical text summarization.
- **Medical Text Summarization**: Generated abridged yet comprehensive summaries from extensive medical documents.

## How It Works

Explain the functioning of the model and the workflow:
- **Model Architecture**: Overview of the T5 LLM architecture and its suitability for medical summarization tasks.
- **Training and Fine-Tuning**: Insight into model training, fine-tuning on medical datasets, and optimization techniques used.
- **Deployment**: Steps to deploy the model on AWS Sagemaker and AWS Lambda, including configuration and setup instructions.

## Installation and Usage

### Requirements

- Python 3.x
- Hugging Face's Transformers library
- AWS Sagemaker and Lambda access

### Installation Steps

Guide users on setting up and running the project locally:
```bash
# Clone the repository
git clone <repository-url>
