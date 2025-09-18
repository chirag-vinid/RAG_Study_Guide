from pypdf import PdfReader

def extract_pdf_text(pdf_path):
    try:
        # Load the PDF file
        reader = PdfReader(pdf_path)
        text = ""

        # Loop through all pages and extract text
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        f = open("extracted_text.txt", "w", encoding="utf-8")
        f.write(text)
        f.close()
        return text

    except Exception as e:
        # return f"Error: {e}"
        return "Value error"
from pypdf import PdfReader

def extract_pdf_text(pdf_path):
    try:
        # Load the PDF file
        reader = PdfReader(pdf_path)
        text = ""

        # Loop through all pages and extract text
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        f = open("extracted_text.txt", "w", encoding="utf-8")
        f.write(text)
        f.close()
        return text

    except Exception as e:
        # return f"Error: {e}"
        return "Value error"