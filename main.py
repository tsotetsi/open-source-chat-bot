"""
OPEN-SOURCE-CHAT-BOT Using Google Gemma LLM
A lightweight chatbot using Google Gemma LLM with Transformers and PyTorch
See README.md for more information.
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig


# Model configuration
model_id = "google/gemma-3-270m"

# Loads the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)

# Loads the model with quantization(4-bit) for reduced memory usage
quantization_config = BitsAndBytesConfig(load_in_4bit=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=quantization_config,
    device_map="auto",
    torch_dtype=torch.bfloat16
)

print("Open Source ChatBot(Gemma) is ready! (Type 'quit' to exit)")

while True:
    # Get user input
    prompt = input("Enter your prompt here: ")
    if prompt.lower() == "quit":
        break

    # tokenizes the input text
    input_ids = tokenizer(prompt, return_tensors="pt").to("cuda")

    # Generate a response from the model. The max_new_tokens parameter controls 
    # the length of the generated output you can adjust it if you want
    outputs = model.generate(
        **input_ids,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95
    )

    # Decode the generated output to a human-readable string
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Print the result, stripping the original prompt for a cleaner output
    response = generated_text[len(prompt):].strip()
    print(f"\nBot: {response}")
