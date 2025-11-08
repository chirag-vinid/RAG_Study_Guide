"""
List all available Gemini models
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("❌ No API key found")
    exit(1)

print(f"✅ API key found (length: {len(api_key)})")

genai.configure(api_key=api_key)

print("\n" + "="*80)
print("Available Gemini Models:")
print("="*80)

try:
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"\n✅ {model.name}")
            print(f"   Display Name: {model.display_name}")
            print(f"   Description: {model.description}")
            print(f"   Supported methods: {model.supported_generation_methods}")
except Exception as e:
    print(f"❌ Error listing models: {str(e)}")
    import traceback
    traceback.print_exc()

print("\n" + "="*80)