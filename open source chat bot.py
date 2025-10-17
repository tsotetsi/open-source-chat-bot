# First, you need to install the required libraries.
# !pip install -U transformers accelerate bitsandbytes torch

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig


model_id = "google/gemma-3-270m"

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Load the model with quantization for reduced memory usage.
# This can be helpful if you have a GPU with limited VRAM.
quantization_config = BitsAndBytesConfig(load_in_4bit=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=quantization_config,
    device_map="auto",
    torch_dtype=torch.bfloat16
)

# Define the prompt for the LLM.
prompt = "Write a short poem about the night sky."

# Tokenize the input text.
input_ids = tokenizer(prompt, return_tensors="pt").to("cuda")

# Generate a response from the model.
# The `max_new_tokens` parameter controls the length of the generated output.
outputs = model.generate(
    **input_ids,
    max_new_tokens=200,
    do_sample=True,
    temperature=0.7,
    top_k=50,
    top_p=0.95
)

# Decode the generated output to a human-readable string.
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Print the result.
print(generated_text)