import os
from pdf_extracter import extract_pdf_text
from text_chunks import get_text_chunks
from embedding import create_vector_store
    
if __name__ == "__main__":
    try:
        # --- Step 1: Ingest the document ---
        print("Welcome to the RAG Document Ingestion System.")
        pdf_path = input("Please enter the full path to your PDF file: ")

        if not os.path.exists(pdf_path):
            print(f"Error: The file at {pdf_path} was not found. Please try again.")
        else:
            print("Extracting text from PDF...")
            raw_text = extract_pdf_text(pdf_path)

            if "Error" in raw_text:
                print(raw_text)
            else:
                # --- Step 2: Chunk the text ---
                print("Text extracted. Splitting into chunks...")
                chunks = get_text_chunks(raw_text)
                print(f"Total chunks created: {len(chunks)}")
                
                # --- Step 3: Embed and Index ---
                print("Embedding and indexing chunks in ChromaDB...")
                vector_store = create_vector_store(chunks)
                print("Vector store created and saved.")

                # --- Step 4: Implement Retrieval ---
                while True:
                    print("\n--- Document Ready for Queries ---")
                    query = input("Enter your query (type 'exit' to quit): ")
                    if query.lower() == 'exit':
                        break
                    
                    print(f"Searching for relevant information for: '{query}'...")
                    results = vector_store.similarity_search(query, k=3) # Search for top 3 results
                    
                    print("\n--- Relevant Chunks Found ---")
                    for i, result in enumerate(results, 1):
                        print(f"Chunk {i}:\n{result.page_content}\n")
                    print("-" * 30)

    except Exception as e:
        print(f"\nAn error occurred during the process: {e}")
    finally:
        print("Program finished.")

import os
from pdf_extracter import extract_pdf_text
from text_chunks import get_text_chunks
from embedding import create_vector_store
    
if __name__ == "__main__":
    try:
        # --- Step 1: Ingest the document ---
        print("Welcome to the RAG Document Ingestion System.")
        pdf_path = input("Please enter the full path to your PDF file: ")

        if not os.path.exists(pdf_path):
            print(f"Error: The file at {pdf_path} was not found. Please try again.")
        else:
            print("Extracting text from PDF...")
            raw_text = extract_pdf_text(pdf_path)

            if "Error" in raw_text:
                print(raw_text)
            else:
                # --- Step 2: Chunk the text ---
                print("Text extracted. Splitting into chunks...")
                chunks = get_text_chunks(raw_text)
                print(f"Total chunks created: {len(chunks)}")
                
                # --- Step 3: Embed and Index ---
                print("Embedding and indexing chunks in ChromaDB...")
                vector_store = create_vector_store(chunks)
                print("Vector store created and saved.")

                # --- Step 4: Implement Retrieval ---
                while True:
                    print("\n--- Document Ready for Queries ---")
                    query = input("Enter your query (type 'exit' to quit): ")
                    if query.lower() == 'exit':
                        break
                    
                    print(f"Searching for relevant information for: '{query}'...")
                    results = vector_store.similarity_search(query, k=3) # Search for top 3 results
                    
                    print("\n--- Relevant Chunks Found ---")
                    for i, result in enumerate(results, 1):
                        print(f"Chunk {i}:\n{result.page_content}\n")
                    print("-" * 30)

    except Exception as e:
        print(f"\nAn error occurred during the process: {e}")
    finally:
        print("Program finished.")
