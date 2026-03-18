# gemini_example.py
import os
from google import genai

# --- API Configuration ---
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise EnvironmentError("GOOGLE_API_KEY environment variable not set.")

client = genai.Client(api_key=api_key)

def query_gemini(prompt: str) -> str:
    """Query the Google Gemini API with a prompt"""
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )
        return response.text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# --- Main Execution ---
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("\nQuerying Google Gemini...")
    result = query_gemini(user_prompt)
    print("\nResponse:")
    print(result)