import google.generativeai as genai
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-flash-latest")

# Ask user for a website
url = input("Enter a website URL to scrape: ")

# Scrape the website
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
text = soup.get_text()

# Clean up the text (first 3000 characters)
clean_text = " ".join(text.split())[:3000]

print("\n✓ Scraped the website!\n")

# Send to AI for summary
response = model.generate_content(f"Summarize what this website is about in 3 sentences:\n\n{clean_text}")

print("AI Summary:")
print(response.text)