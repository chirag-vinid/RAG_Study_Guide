"""
Gemini API Integration for Study Guide Generation
Processes text chunks with Gemini to create structured study content
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv
import time

load_dotenv()


def generate_study_content_with_gemini(relevant_chunks: list, topics: str, custom_prompt: str = None) -> str:
    """
    Send relevant chunks to Gemini API to generate structured study guide content
    
    Args:
        relevant_chunks: List of text chunks relevant to the topics
        topics: Topics the user wants to study
        custom_prompt: Optional custom prompt for Gemini (you can modify this)
    
    Returns:
        str: Generated study guide content from Gemini
    """
    
    print("\n" + "="*80)
    print("[Gemini] Starting content generation")
    print("="*80)
    
    # Get API key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        error_msg = "Google API key not found in .env file"
        print(f"[Gemini] ❌ ERROR: {error_msg}")
        raise ValueError(error_msg)
    
    print(f"[Gemini] ✅ API key found (length: {len(api_key)})")
    
    # Configure Gemini
    try:
        genai.configure(api_key=api_key)
        print("[Gemini] ✅ API configured successfully")
    except Exception as e:
        print(f"[Gemini] ❌ ERROR configuring API: {str(e)}")
        raise
    
    # Use Gemini 2.5 Flash (stable version)
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        print("[Gemini] ✅ Model initialized: gemini-2.5-flash")
    except Exception as e:
        print(f"[Gemini] ❌ ERROR initializing model: {str(e)}")
        raise
    
    print(f"[Gemini] Processing {len(relevant_chunks)} chunks for topics: {topics}")
    
    # Combine all chunks into one text
    combined_text = "\n\n---\n\n".join(relevant_chunks)
    print(f"[Gemini] Combined text length: {len(combined_text)} characters")
    
    # Limit text length to avoid token limits (Gemini 2.5 Flash has 1M token limit, but be conservative)
    MAX_CHARS = 50000  # Conservative limit for prompt
    if len(combined_text) > MAX_CHARS:
        print(f"[Gemini] ⚠️  Text too long, truncating to {MAX_CHARS} characters")
        combined_text = combined_text[:MAX_CHARS] + "\n\n[... content truncated due to length ...]"
    
    # Default prompt (YOU CAN MODIFY THIS)
    if not custom_prompt:
        custom_prompt = f"""
You are an expert study guide creator. Based on the provided study material and topics, create a comprehensive, well-structured study guide.

**Topics to focus on:** {topics}

**Study Material:**
{combined_text}

**Instructions:**
1. Create a detailed study guide focusing ONLY on the topics: {topics}
2. Structure the content with clear headings and subheadings
3. Include key concepts, definitions, and important points
4. Add examples where relevant
5. Organize information in a logical, easy-to-study format
6. Use bullet points and numbered lists for clarity
7. Highlight critical information that students should memorize
8. If applicable, add practice questions or review points at the end

**Format your response in Markdown with proper headings (##, ###, etc.)**

Generate the study guide now:
"""
    
    print(f"[Gemini] Prompt length: {len(custom_prompt)} characters")
    
    try:
        print("[Gemini] 🚀 Sending request to Gemini API...")
        print("[Gemini] This may take 10-30 seconds...")
        
        # Add retry logic
        max_retries = 3
        for attempt in range(max_retries):
            try:
                # Generate content with Gemini
                response = model.generate_content(
                    custom_prompt,
                    generation_config=genai.types.GenerationConfig(
                        temperature=0.7,
                        top_p=0.95,
                        top_k=40,
                        max_output_tokens=8192,
                    ),
                    safety_settings=[
                        {
                            "category": "HARM_CATEGORY_HARASSMENT",
                            "threshold": "BLOCK_NONE",
                        },
                        {
                            "category": "HARM_CATEGORY_HATE_SPEECH",
                            "threshold": "BLOCK_NONE",
                        },
                        {
                            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                            "threshold": "BLOCK_NONE",
                        },
                        {
                            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                            "threshold": "BLOCK_NONE",
                        },
                    ]
                )
                
                # Check if response was blocked
                if not response.text:
                    print(f"[Gemini] ⚠️  Response blocked or empty")
                    if hasattr(response, 'prompt_feedback'):
                        print(f"[Gemini] Prompt feedback: {response.prompt_feedback}")
                    raise ValueError("Response was blocked by safety filters or is empty")
                
                print("[Gemini] ✅ Successfully generated study content")
                print(f"[Gemini] Response length: {len(response.text)} characters")
                print("="*80 + "\n")
                
                # Return the generated text
                return response.text
                
            except Exception as retry_error:
                print(f"[Gemini] ⚠️  Attempt {attempt + 1}/{max_retries} failed: {str(retry_error)}")
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s
                    print(f"[Gemini] Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    raise
        
    except Exception as e:
        print(f"[Gemini] ❌ Error generating content: {str(e)}")
        print(f"[Gemini] Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()
        
        # Fallback: return a formatted version of the chunks
        print("[Gemini] 🔄 Falling back to basic formatting...")
        fallback_content = f"## Study Guide for: {topics}\n\n"
        fallback_content += "*Note: AI generation unavailable, showing extracted content*\n\n"
        fallback_content += f"*Error: {str(e)}*\n\n"
        fallback_content += "---\n\n"
        
        for i, chunk in enumerate(relevant_chunks[:10], 1):  # Limit to 10 chunks in fallback
            fallback_content += f"### Section {i}\n\n{chunk}\n\n---\n\n"
        
        if len(relevant_chunks) > 10:
            fallback_content += f"\n*Note: Showing 10 of {len(relevant_chunks)} relevant sections*\n"
        
        return fallback_content


def generate_study_content_with_custom_prompt(
    relevant_chunks: list, 
    topics: str, 
    custom_instructions: str
) -> str:
    """
    Alternative function that lets you pass completely custom instructions
    
    Args:
        relevant_chunks: List of text chunks
        topics: Topics to study
        custom_instructions: Your own custom prompt/instructions
    
    Returns:
        str: Generated content
    """
    
    combined_text = "\n\n---\n\n".join(relevant_chunks)
    
    # Limit text length
    MAX_CHARS = 50000
    if len(combined_text) > MAX_CHARS:
        combined_text = combined_text[:MAX_CHARS] + "\n\n[... content truncated ...]"
    
    full_prompt = f"""
{custom_instructions}

**Topics:** {topics}

**Study Material:**
{combined_text}
"""
    
    api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        print(f"[Gemini] Error: {str(e)}")
        return f"Error generating content: {str(e)}"


# For testing
if __name__ == "__main__":
    print("="*80)
    print("Gemini Generator Module - Test Mode")
    print("="*80)
    
    # Test API key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("❌ No API key found in .env file")
        print("Please create a .env file with: GOOGLE_API_KEY=your_key_here")
    else:
        print(f"✅ API key found (length: {len(api_key)})")
        
        # Test simple generation
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            print("\nTesting Gemini 2.5 Flash API with simple prompt...")
            response = model.generate_content("Say 'Hello, Gemini 2.5 Flash is working!'")
            print(f"\n✅ Test successful!")
            print(f"Response: {response.text}")
            
        except Exception as e:
            print(f"\n❌ Test failed: {str(e)}")
            import traceback
            traceback.print_exc()