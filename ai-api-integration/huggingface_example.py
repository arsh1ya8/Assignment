# huggingface_example.py
# Query Hugging Face models using the new InferenceClient

import os
from huggingface_hub import InferenceClient

# --- API Configuration ---
api_key = os.getenv("HUGGINGFACE_API_KEY")
if not api_key:
    raise EnvironmentError("HUGGINGFACE_API_KEY environment variable not set.")

client = InferenceClient(
    provider="novita",
    api_key=api_key,
)


def query_huggingface(prompt: str) -> str:
    """Query Hugging Face Inference API with a prompt"""
    try:
        completion = client.chat.completions.create(
            model="Qwen/Qwen2.5-72B-Instruct",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"


# --- Main Execution ---
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("\nQuerying Hugging Face (Qwen2.5-72B-Instruct)...")
    result = query_huggingface(user_prompt)
    print("\nResponse:")
    print(result)
