import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
def create_vector_store(text_chunks: list) -> Chroma:
    """
    Takes text chunks, embeds them using a Google Gemini model,
    and stores them in a Chroma vector database.

    Args:
        text_chunks (list): A list of text chunks.

    Returns:
        Chroma: The initialized Chroma vector store object.
    """
    # Get the API key from environment variables for security
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Google API key not found. Please set it in your environment variables.")

    # Configure the Gemini API client
    genai.configure(api_key=api_key)

    # Use the LangChain wrapper for the Gemini embedding model
    gemini_embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    # --- Setup Chroma vector store ---
    persist_directory = "./chroma_store_gemini"

    vectorstore = Chroma.from_texts(
        texts=text_chunks,
        embedding=gemini_embeddings,
        persist_directory=persist_directory,
    )
    
    print(f"✅ Vector store created and saved at {persist_directory}")
    return vectorstore