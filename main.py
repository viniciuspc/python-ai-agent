import os
import argparse
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

def main():
    generated_content = client.models.generate_content(model="gemini-2.5-flash", contents=args.user_prompt)
    usage_metadata = generated_content.usage_metadata
    if usage_metadata:
        print(f"Prompt tokens: {usage_metadata.prompt_token_count}")
        print(f"Response tokens: {usage_metadata.candidates_token_count}")
        print(generated_content.text)
    else:
        raise RuntimeError("Failed to connect to Gemini API")


if __name__ == "__main__":
    main()
