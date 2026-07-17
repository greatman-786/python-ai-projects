from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

print("Loading your document...")

loader = TextLoader("knowledge.txt")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
chunks = splitter.split_documents(documents)

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vectorstore = Chroma.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever()

llm = ChatGoogleGenerativeAI(model="gemini-flash-latest")

print("Ready! Ask questions (type quit to exit)")

while True:
    question = input("You: ")
    if question.lower() == "quit":
        break
    docs = retriever.invoke(question)
    context = "\n".join([d.page_content for d in docs])
    prompt = f"Answer using only this context: {context}\n\nQuestion: {question}"
    answer = llm.invoke(prompt)
    text = answer.content
    if isinstance(text, list):
        text = text[0].get("text", str(text))
    print("AI:", text, "\n")