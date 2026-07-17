from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os
import time

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

print("Loading company FAQ...")

loader = TextLoader("company_faq.txt")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
chunks = splitter.split_documents(documents)

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vectorstore = Chroma.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

print("\nCustomer Support AI Ready!")
print("Ask any question (type quit to exit)\n")

while True:
    question = input("Customer: ")
    if question.lower() == "quit":
        print("Thank you for contacting us!")
        break
    docs = retriever.invoke(question)
    context = "\n".join([d.page_content for d in docs])
    prompt = f"You are a friendly customer support agent. Answer using only this company information. If the answer isn't in the info, politely say you'll connect them to a human agent.\n\nCompany info: {context}\n\nCustomer question: {question}"
    
    for attempt in range(3):
        try:
            answer = llm.invoke(prompt)
            text = answer.content
            if isinstance(text, list):
                text = text[0].get("text", str(text))
            print("Support:", text, "\n")
            break
        except Exception:
            if attempt < 2:
                print("(one moment...)")
                time.sleep(5)
            else:
                print("Support: Sorry, please try again in a moment.\n")