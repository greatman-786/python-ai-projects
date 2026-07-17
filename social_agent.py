import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-flash-latest")

print("🚀 Social Media AI Agent\n")

# Get business info from user
business = input("What is your business/topic? ")
platform = input("Which platform? (Facebook / Instagram / LinkedIn): ")
days = input("How many posts do you want? ")

print("\n⏳ Generating your content...\n")

# AI generates the content
prompt = f"""
You are a social media manager. Create {days} engaging {platform} posts for this business: {business}

For each post, include:
- The post text (matching {platform}'s style)
- Relevant hashtags
- A suggested day/time to post

Make each post different and engaging. Number them clearly.
"""

response = model.generate_content(prompt)

print("=" * 50)
print(f"YOUR {platform.upper()} CONTENT PLAN")
print("=" * 50)
print(response.text)