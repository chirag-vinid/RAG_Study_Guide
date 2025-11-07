"""
Simplified PDF Extractor - Study Material Only
Extracts text from PDF and saves to a single file
"""

from pypdf import PdfReader
import os


def extract_pdf_to_text_file(pdf_path, output_folder="./extracted_text"):
    """
    Extract text from PDF and save to a text file.
    Simple and straightforward - no chapter detection.
    
    Args:
        pdf_path (str): Path to the PDF file
        output_folder (str): Folder where extracted text file will be saved
    
    Returns:
        dict: Information about extraction
    """
    try:
        print(f"\n{'='*70}")
        print("PDF EXTRACTOR - STUDY MATERIAL MODE")
        print(f"{'='*70}")
        print(f"Reading PDF: {pdf_path}")
        
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        # Load the PDF file
        reader = PdfReader(pdf_path)
        total_pages = len(reader.pages)
        print(f"Total pages: {total_pages}")
        
        # Extract all text
        full_text = ""
        for page_num, page in enumerate(reader.pages, 1):
            page_text = page.extract_text()
            if page_text:
                full_text += page_text + "\n"
            
            # Progress indicator for large PDFs
            if page_num % 10 == 0:
                print(f"Processed {page_num}/{total_pages} pages...")
        
        print(f"Extraction complete. Total characters: {len(full_text)}")
        
        # Get base filename without extension
        base_filename = os.path.splitext(os.path.basename(pdf_path))[0]
        
        # Create output filename
        output_filename = f"{base_filename}_extracted.txt"
        output_filepath = os.path.join(output_folder, output_filename)
        
        # Save to file
        print(f"\nSaving to: {output_filepath}")
        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(full_text)
        
        print(f"✅ Saved: {output_filename} ({len(full_text)} characters)")
        
        result = {
            'success': True,
            'total_pages': total_pages,
            'total_characters': len(full_text),
            'output_file': output_filepath,
            'filename': output_filename,
            'text': full_text  # Return the text directly too
        }
        
        print("\n" + "="*70)
        print("EXTRACTION COMPLETE!")
        print("="*70)
        print(f"Output file: {os.path.abspath(output_filepath)}")
        print("="*70 + "\n")
        
        return result
        
    except FileNotFoundError:
        print(f"❌ ERROR: File not found: {pdf_path}")
        return {'success': False, 'error': 'File not found'}
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return {'success': False, 'error': str(e)}


def load_text_from_file(text_file_path):
    """
    Load text from a previously extracted text file.
    
    Args:
        text_file_path (str): Path to the text file
    
    Returns:
        str: The text content
    """
    try:
        with open(text_file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        print(f"✅ Loaded text from: {text_file_path} ({len(text)} characters)")
        return text
    except Exception as e:
        print(f"❌ ERROR loading file: {str(e)}")
        return None


# Keep old function name for backward compatibility
def extract_pdf_text(pdf_path, save_to_file=False):
    """
    Legacy function - redirects to new function
    """
    if save_to_file:
        result = extract_pdf_to_text_file(pdf_path, "./extracted_text")
        return result['text'] if result['success'] else "Value error"
    else:
        # Just extract without saving
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return text
        except:
            return "Value error"


# ============================================================================
# TESTING/DEMO MODE
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("PDF EXTRACTOR - STANDALONE TEST MODE")
    print("="*70)
    
    # Get user input
    pdf_path = input("\nEnter the full path to your PDF file: ").strip()
    
    if not os.path.exists(pdf_path):
        print(f"❌ Error: File not found at {pdf_path}")
        exit(1)
    
    output_folder = input("\nEnter output folder path (default: ./extracted_text): ").strip()
    if not output_folder:
        output_folder = "./extracted_text"
    
    # Extract PDF
    result = extract_pdf_to_text_file(pdf_path, output_folder)
    
    if result['success']:
        print("\n" + "="*70)
        print("EXTRACTION SUMMARY")
        print("="*70)
        print(f"Total pages: {result['total_pages']}")
        print(f"Total characters: {result['total_characters']}")
        print(f"Output file: {result['filename']}")
        print("="*70)
        
        # Show preview
        print(f"\nFirst 500 characters of extracted text:")
        print("-" * 70)
        print(result['text'][:500] + "...")
        print("-" * 70)
    else:
        print(f"\n❌ Extraction failed: {result.get('error', 'Unknown error')}")