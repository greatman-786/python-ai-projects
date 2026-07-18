import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY", "")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash-lite")

st.set_page_config(page_title="Asad's AI Toolkit", page_icon="🤖", layout="wide")

st.sidebar.title("🤖 AI Toolkit")
st.sidebar.markdown("Built by **Asad Ullah**")
choice = st.sidebar.radio("Choose a tool:", [
    "AI Chat Agent",
    "AI Web Scraper",
    "Social Media Generator",
    "Document Q&A",
    "Customer Support AI"
])
st.sidebar.markdown("---")
st.sidebar.markdown("[Portfolio](https://asad-portfolio-drab.vercel.app)")
st.sidebar.markdown("[GitHub](https://github.com/greatman-786)")


def ask_ai(prompt):
    try:
        r = model.generate_content(prompt)
        return r.text
    except Exception as e:
        return f"Server busy, please try again. ({e})"


if choice == "AI Chat Agent":
    st.title("🤖 AI Chat Agent")
    st.write("Ask me anything — powered by Google Gemini.")
    q = st.text_input("Your question:")
    if st.button("Ask") and q:
        with st.spinner("Thinking..."):
            st.write(ask_ai(q))

elif choice == "AI Web Scraper":
    st.title("🕷️ AI Web Scraper")
    st.write("Enter a website and AI will summarise it.")
    url = st.text_input("Website URL:", "https://example.com")
    if st.button("Scrape & Summarise") and url:
        with st.spinner("Scraping..."):
            try:
                page = requests.get(url, timeout=10)
                soup = BeautifulSoup(page.content, "html.parser")
                text = " ".join(soup.get_text().split())[:3000]
                st.success("Scraped successfully!")
                st.write(ask_ai(f"Summarise this website in 3 sentences: {text}"))
            except Exception as e:
                st.error(f"Could not scrape that site. {e}")

elif choice == "Social Media Generator":
    st.title("📱 Social Media Content Generator")
    biz = st.text_input("Your business/topic:", "coffee shop")
    plat = st.selectbox("Platform:", ["Instagram", "Facebook", "LinkedIn", "Twitter/X"])
    num = st.slider("How many posts?", 1, 5, 3)
    if st.button("Generate Posts"):
        with st.spinner("Writing..."):
            st.write(ask_ai(f"Create {num} engaging {plat} posts for this business: {biz}. Include hashtags and a suggested posting time for each."))

elif choice == "Document Q&A":
    st.title("📄 Document Q&A")
    st.write("Paste any text, then ask questions about it.")
    doc = st.text_area("Paste your document text here:", height=200)
    q = st.text_input("Your question about the document:")
    if st.button("Get Answer") and doc and q:
        with st.spinner("Reading..."):
            st.write(ask_ai(f"Answer using only this document:\n\n{doc}\n\nQuestion: {q}"))

elif choice == "Customer Support AI":
    st.title("🎧 Customer Support AI")
    st.write("A support agent that answers from a company's FAQ.")
    faq = st.text_area("Company FAQ / info:", height=150, value="""We are open Monday to Friday, 9 AM to 6 PM EST.
We offer a 30-day money-back guarantee on all products.
Standard shipping takes 5-7 business days.
We ship to over 50 countries.
We accept all major credit cards, PayPal, and bank transfers.""")
    q = st.text_input("Customer question:")
    if st.button("Get Support Reply") and q:
        with st.spinner("Responding..."):
            st.write(ask_ai(f"You are a friendly customer support agent. Answer using only this company info. If the answer isn't there, politely offer to connect them to a human.\n\nInfo: {faq}\n\nQuestion: {q}"))