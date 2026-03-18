# AI API Integration

A collection of Python programs that interact with four different Generative AI providers:
**Groq · Ollama · Hugging Face · Cohere**

---

## Project Structure

```
ai-api-integration/
├── groq_example.py
├── ollama_example.py
├── huggingface_example.py
├── cohere_example.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── groq_output.png
    ├── ollama_output.png
    ├── huggingface_output.png
    └── cohere_output.png
```

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd ai-api-integration
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set environment variables

**Windows (PowerShell) — temporary for current session:**
```powershell
$env:GROQ_API_KEY="your-groq-key"
$env:HUGGINGFACE_API_KEY="your-hf-key"
$env:COHERE_API_KEY="your-cohere-key"
```

**Windows — permanent using setx (restart VS Code after):**
```cmd
setx GROQ_API_KEY "your-groq-key"
setx HUGGINGFACE_API_KEY "your-hf-key"
setx COHERE_API_KEY "your-cohere-key"
```

**Using a .env file (recommended):**

Create a `.env` file in the project folder:
```
GROQ_API_KEY=your-groq-key
HUGGINGFACE_API_KEY=your-hf-key
COHERE_API_KEY=your-cohere-key
```
Add this to the top of each Python file:
```python
from dotenv import load_dotenv
load_dotenv()
```

> ⚠️ Add `.env` to `.gitignore` — never commit API keys to GitHub!

---

## How to Obtain Each API Key

| Provider | Steps |
|----------|-------|
| **Groq** | Sign up at https://console.groq.com/ → API Keys → Create key (Free) |
| **Ollama** | Download from https://ollama.ai/ → No key needed (runs locally) → `ollama pull llama3.2` |
| **Hugging Face** | Sign up at https://huggingface.co/ → Settings → Access Tokens → New token (Free) |
| **Cohere** | Sign up at https://dashboard.cohere.com/ → API Keys → Copy trial key (Free) |

---

## How to Run Each Program

```bash
# Groq
python groq_example.py

# Ollama (runs locally, no key needed — make sure Ollama is installed)
python ollama_example.py

# Hugging Face
python huggingface_example.py

# Cohere
python cohere_example.py
```

Each program will prompt you to type your question and then print the AI's response.

---

## Screenshots

See the `screenshots/` folder for output from each provider.

---

## Notes

- All APIs used are **free tier** — no credit card required.
- Ollama runs **locally** on your machine — ensure Ollama is installed and running before executing `ollama_example.py`.
- Hugging Face uses `InferenceClient` with the `Qwen/Qwen2.5-72B-Instruct` model.
- Cohere uses the `command-r-plus-08-2024` model.
