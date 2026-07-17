# Python AI Projects

A collection of AI agents, chatbots, and automation tools built from scratch in Python using Large Language Models (Google Gemini) and LangChain. Each project demonstrates practical, real-world applications of AI.

**Built by Asad Ullah** — AI Automation Specialist
Portfolio: [asad-portfolio-drab.vercel.app](https://asad-portfolio-drab.vercel.app)

---

## 🛠️ Tech Stack

- **Python** — core language
- **Google Gemini** — large language model
- **LangChain** — AI agent + RAG framework
- **ChromaDB** — vector database for RAG
- **BeautifulSoup + Requests** — web scraping
- **python-dotenv** — secure API key management

---

## 📂 Projects

### 1. Interactive AI Agent (`agent.py`)
A conversational AI assistant that answers any question in a continuous chat loop, powered by Google Gemini.
- Real-time conversation
- Secure API key handling via `.env`

### 2. AI Web Scraper (`scraper.py`)
Scrapes text content from any website and uses AI to summarize what the page is about.
- Combines web scraping (BeautifulSoup) with AI summarization
- Takes any URL as input

### 3. Social Media Content Agent (`social_agent.py`)
Generates ready-to-post social media content for any business and platform, complete with hashtags and suggested posting times.
- Multi-platform (Facebook, Instagram, LinkedIn)
- Practical marketing automation tool

### 4. RAG Document Chatbot (`rag_chatbot.py`)
A Retrieval-Augmented Generation (RAG) chatbot that answers questions based only on a provided text document.
- Uses embeddings + ChromaDB vector store
- Answers strictly from the source document

### 5. PDF RAG Chatbot (`pdf_chatbot.py`)
Reads a real PDF document and answers questions about its content using RAG.
- Processes actual PDF files
- "Chat with your document" functionality

### 6. Customer Support AI (`support_ai.py`)
A customer support agent that answers customer questions using a company's FAQ/knowledge base, and offers to escalate to a human when needed.
- Real business use case
- Friendly support-agent tone with auto-retry handling

---

## 🚀 How to Run

1. Install the required libraries:
pip install google-generativeai python-dotenv requests beautifulsoup4 langchain langchain-google-genai langchain-community langchain-text-splitters chromadb pypdf

2. Create a `.env` file with your Gemini API key:
GEMINI_API_KEY=your_key_here

3. Run any project:
python agent.py

---

## 📌 About

These projects were built to demonstrate hands-on ability to design and code AI systems — from simple conversational agents to production-style RAG chatbots and business automation tools. Every project was built from scratch.

**Contact:** [LinkedIn](https://linkedin.com/in/asad-ullah-b0190a236) • [Portfolio](https://asad-portfolio-drab.vercel.app)
