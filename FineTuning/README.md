# Fine-Tuning Notebook

## Overview
This notebook demonstrates fine-tuning a large language model (LLM) for JSON data extraction from HTML product information. It uses the **Phi-3-mini-4k-instruct** model with **LoRA (Low-Rank Adaptation)** for efficient parameter-tuned training.

## Project Structure
- **FineTuning.ipynb** - Main training and inference notebook
- **json_extraction_dataset_500.json** - Training dataset with 500 product examples
- **Modelfile** - Configuration file for model deployment (Ollama format)

## Key Features

### Model Architecture
- **Base Model**: Phi-3-mini-4k-instruct (4-bit quantized via Unsloth)
- **Fine-tuning Method**: LoRA (Rank=64, Alpha=128)
- **Max Sequence Length**: 2048 tokens

### Dataset
- **Size**: 500 examples
- **Task**: Extract structured product information from HTML markup
- **Fields**: Product name, price, category, manufacturer

### Training Configuration
- **Batch Size**: 2 (with gradient accumulation of 4 → effective batch size of 8)
- **Epochs**: 3
- **Learning Rate**: 2e-4
- **Optimizer**: AdamW 8-bit
- **Save Strategy**: Save after each epoch (keep last 2 checkpoints)

## Dependencies

```bash
pip install unsloth trl peft accelerate bitsandbytes torch transformers datasets
```

### Key Libraries
- **Unsloth**: Optimized fine-tuning framework for LLMs
- **TRL**: Transformer Reinforcement Learning library
- **PEFT**: Parameter-Efficient Fine-Tuning
- **Transformers**: Hugging Face models
- **Accelerate**: Distributed training support
- **Bitsandbytes**: 8-bit optimization

## Workflow

### 1. Data Loading
Loads 500 training examples from the JSON dataset and displays sample format.

### 2. Environment Setup
- Installs required dependencies
- Verifies GPU availability (CUDA)
- Checks GPU model name

### 3. Model Loading
Loads the Phi-3-mini model in 4-bit quantized format for memory efficiency.

### 4. Data Preparation
Formats training data into prompt-response pairs:
```
### Input: <html_markup>
### Output: <json_output><|endoftext|>
```

### 5. LoRA Configuration
Applies Low-Rank Adapter modules to these layers:
- Query, Key, Value, Output projections (self-attention)
- Gate, Up, Down projections (feed-forward)

### 6. Training
Trains the model using the Supervised Fine-Tuning (SFT) trainer with the configured hyperparameters.

### 7. Inference
Tests the fine-tuned model on a sample product extraction task.

## Usage

### Prerequisites
- GPU with CUDA support (recommended: NVIDIA GPU with 8GB+ VRAM)
- Python 3.8+
- Jupyter notebook or VS Code

### Running the Notebook
1. Ensure dataset file (`json_extraction_dataset_500.json`) is available
2. Run cells sequentially from top to bottom
3. Monitor training progress and GPU memory usage
4. Test inference with custom prompts

### Sample Input/Output
**Input:**
```
Extract the product information:
<div class='product'><h2>iPad Air</h2><span class='price'>$1344</span><span class='category'>audio</span><span class='brand'>Dell</span></div>
```

**Expected Output:**
```json
{
  "name": "iPad Air",
  "price": "$1344",
  "category": "audio",
  "manufacturer": "Dell"
}
```

## Model Deployment

The `Modelfile` configures the fine-tuned model for deployment using Ollama:
- Loads the quantized model file
- Sets inference parameters (temperature=0.7, top_p=0.9)
- Defines prompt template and system message

## Performance Optimization

- **4-bit Quantization**: Reduces memory footprint by ~75%
- **LoRA**: Only ~3-5% of parameters are trainable
- **Gradient Checkpointing**: Reduces memory consumption during backpropagation
- **8-bit Optimizer**: Further memory optimization

## Output
- **Model Checkpoints**: Saved in `outputs/` directory after each epoch
- **Training Logs**: Displayed during training with loss metrics every 25 steps
- **Inference Results**: Model predictions on test prompts

## Notes
- Adjust `per_device_train_batch_size` and `gradient_accumulation_steps` based on available GPU memory
- The model expects HTML-formatted product data as input
- Training duration depends on GPU capabilities (typically 10-30 minutes for 3 epochs)

## References
- [Unsloth Documentation](https://github.com/unslothai/unsloth)
- [PEFT Library](https://huggingface.co/docs/peft)
- [Phi-3 Model Card](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct)
