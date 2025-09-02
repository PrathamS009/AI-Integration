from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")

#Writing if-else to check loading of API Key
if api_key:
    print("API key loaded successfully")
else:
    print("Failed to load API key")


client = OpenAI()

#Giving a prompt and a dummy response in case of error
try:
    response = client.responses.create(
        model="gpt-5",
        input="Write a one-sentence bedtime story about a unicorn."
    )
    print(response.output_text)
except Exception as e:
    print("API call failed due to: ",e)
    
