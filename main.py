import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

def main():
    for _ in range(20):
        generated_content = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
                ),
            )
        
        candidates = generated_content.candidates
        if candidates:
            for candidate in candidates:
                messages.append(candidate.content)
        
        usage_metadata = generated_content.usage_metadata
        if usage_metadata:
            if args.verbose:
                print(f"User prompt: {args.user_prompt}")
                print(f"Prompt tokens: {usage_metadata.prompt_token_count}")
                print(f"Response tokens: {usage_metadata.candidates_token_count}")
            
            function_calls = generated_content.function_calls
            
            if function_calls:
                function_results = []
                for function_call in function_calls:
                    function_call_result = call_function(function_call, args.verbose)
                    
                    if not function_call_result.parts:
                        raise Exception("function_call_result.parts does not exists ")
                    
                    function_call_result_part = function_call_result.parts[0]
                    
                    if not function_call_result_part.function_response or not function_call_result_part.function_response.response:
                        raise Exception("function_call_result response is does not exists")
                    
                    function_results.append(function_call_result_part)
                    
                    if args.verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
                        
                messages.append(types.Content(role="user", parts=function_results))
            else:
                print(generated_content.text)
                return
        else:
            raise RuntimeError("Failed to connect to Gemini API")
        
    print("Model could not produce a result with 20 interation. Exiting with code 1")
    exit(1)


if __name__ == "__main__":
    main()
