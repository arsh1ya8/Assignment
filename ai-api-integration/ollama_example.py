# ollama_example.py
# Query a locally running Ollama model via its REST API

import requests
import json

# --- API Configuration ---
OLLAMA_BASE_URL = "http://localhost:11434"   # default Ollama address
MODEL_NAME      = "llama3.2"                   # change to any model you have pulled


def query_ollama(prompt: str) -> str:
    """Send a prompt to the local Ollama server and return the response text."""
    url     = f"{OLLAMA_BASE_URL}/api/generate"
    payload = {
        "model":  MODEL_NAME,
        "prompt": prompt,
        "stream": False,          # wait for the full response before returning
    }

    try:
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response received.").strip()
    except requests.exceptions.ConnectionError:
        return (
            "Error: Could not connect to Ollama. "
            "Make sure Ollama is running (`ollama serve`) and the model is pulled "
            f"(`ollama pull {MODEL_NAME}`)."
        )
    except Exception as e:
        return f"Error: {str(e)}"


# --- Main Execution ---
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print(f"\nQuerying Ollama ({MODEL_NAME})...")
    result = query_ollama(user_prompt)
    print("\nResponse:")
    print(result)
