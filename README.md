# Open-Source-Chat-Bot

<div align="center">

  [![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?logo=PyTorch&logoColor=white)](https://docs.pytorch.org/docs/stable/index.html)
  [![Transformers](https://img.shields.io/badge/🤗%20Transformers-%23FFCE3C.svg)](https://huggingface.co/docs/transformers/en/index)
  [![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-yellow)](https://huggingface.co/join)
  [![Gemma](https://img.shields.io/badge/Google%20Gemma-8E75B2?logo=google&logoColor=white)](https://ai.google.dev/gemma/docs)
  [![Python](https://img.shields.io/badge/Python-3.12+-3776ab?logo=python&logoColor=white)](https://www.python.org/)
  [![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

</div>

A simple and efficient Python-based chatbot powered by Google's open-source Gemma language model. This project demonstrates how to run a large language model locally on your machine with quantization for reduced memory usage.

## 📋 Prerequisites

Before you begin, ensure you have the following:

1.  **A Hugging Face Account:** You need an account to access the model.
    *   Sign up at [https://huggingface.co/join](https://huggingface.co/join)
2.  **Hugging Face Token:** You need a User Access Token to grant the script permission to download the model.
    *   Go to your [Hugging Face settings](https://huggingface.co/settings/tokens).
    *   Generate a new token with "Read" access.
3.  **Python 3.12 or higher**
4.  **pip** (Python package installer)

## 🚀 Getting Started

Follow these steps to get the chatbot running on your local machine.

### 1. Clone the Repository

```bash
git https://github.com/Rakeshvarma007/open-source-chat-bot
cd open-source-chat-bot
```

### 2. Set up a Python Virtual Environment (Recommended)

It's good practice to create an isolated environment for Python projects and activate it.

```bash
   python -m venv venv
```

Then you need to activate the virtual envrionment.

- **On MacOS/Linux**:

    `source venv/bin/activate`

- **On Windows**:

    `.\venv\Scripts\activate`

### 3. Install Dependencies

```bash
   pip install -r requirements.txt
```

### 4. Authenticate with Hugging Face

You need to log in to the Hugging Face CLI using your access token. This allows the script to download the model.

Run the following command in your terminal and paste your token when prompted:

```bash
   huggingface-cli login
```

### 5. Run the Chatbot

Once authentication is successful, you can run the chatbot.

```bash
  python main.py
```

You will be prompted to enter your message. The model will generate a response and display it in the terminal.


> **Note:** *This project requires **PyTorch**. The `requirements.txt` specifies the CPU version by default for maximum compatibility. If you have a compatible NVIDIA GPU, you can get significantly better performance by installing the CUDA-enabled version of PyTorch. Visit pytorch.org for the correct install command for your system*


## 📁 Project Structure
```text
open-source-chat-bot/
├── main.py          # Main script for the open-source-chat-bot.
├── requirements.txt # Project dependencies.
└── README.md        # This file.
```

### 🔧 Configuration

The model's generation behavior can be tweaked in the `main.py` script by modifying the parameters inside model.generate():

- **max_new_tokens:** Controls the maximum length of the generated response.

- **temperature:** Controls randomness (lower = more deterministic, higher = more creative).

- **top_k:** Limits the model to consider only the top K most likely tokens.

- **top_p:** Uses nucleus sampling, considering the smallest set of tokens whose cumulative probability exceeds P.


### ❓ Troubleshooting

- **Issue:** "Access to model google/gemma-3-270m is restricted and you are not in the authorized list. Visit https://huggingface.co/google/gemma-3-270m to ask for access"
    - **Solution:** As per the message, visit https://huggingface.co/google/gemma-3-270m and click on  `Acknowledge license`. Then you will get something like: `*Gated model
You have been granted access to this model*`

- **Issue:** "You are not logged in to Hugging Face..." or "401 Client Error..."

    - **Solution:** Ensure you have run huggingface-cli login and provided the correct token.

- **Issue:** The script is very slow.

    - **Solution:** The model is running on your CPU. For faster performance, ensure you have a compatible GPU and have installed the CUDA version of PyTorch.

- **Issue:** OutOfMemoryError when loading the model.

    - **Solution:** The model requires a significant amount of RAM/VRAM. The script uses 4-bit quantization to reduce memory footprint. If you still encounter issues, try closing other memory-intensive applications.


## 🗒️ Notes

The first run will download the ~2GB model("google/gemma-3-270m") file, which may take some time. Addtionally, more
downloads will come from `torch`(~899MB) and `transformers` required by the main.py file. See `requirements.txt` file.

This is a fun project for demonstration purposes. The quality of responses may vary.

No other API keys (e.g., for OpenAI or Gemini) are required or used by this project. It runs entirely locally using the Hugging Face transformers library.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

When reporting an issue, please provide:

- Your operating system.

- Python version.

- The exact error message and traceback.

- Steps to reproduce the problem.

> Please do not report issues related to the fundamental capabilities of the base model (e.g., "why is it not as smart as ChatGPT?") as this is a demonstration project using a specific, publicly available model.


## 📝 License

This project is open source. Please check the repository for any licensing information.

<div align="center">

Made with ❤️ by [Rakesh Varma](https://github.com/Rakeshvarma007)

</div>