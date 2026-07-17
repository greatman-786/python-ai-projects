import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-latest")

print("🤖 AI Agent ready! Type your question (or 'quit' to exit)\n")

while True:
    question = input("You: ")
    
    if question.lower() == "quit":
        print("Goodbye! 👋")
        break
    
    response = model.generate_content(question)
    print("AI:", response.text, "\n")
