import streamlit as st
import time
import base64
from io import BytesIO

# --- Configuration & Styling ---
st.set_page_config(
    page_title="Notes Publication Agent",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Define the futuristic color palette
COLORS = {
    "dark_blue": "#2A3056",
    "teal": "#43B0AF",
    "cyan": "#67FFF2", # BRIGHT CYAN
    "dark_green": "#294933",
    "light_green": "#81EC86", # BRIGHT LIME GREEN
    "font_family": "Orbitron, sans-serif" 
}

# --- CUSTOM CSS WITH STATIC BACKGROUND GRID (NO ANIMATION) AND BRIGHTER FOREGROUND ---

CUSTOM_CSS = f"""
    /* 1. Import Orbitron Font */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
    /* ------------------------------------------- */
    /* STATIC BACKGROUND GRID (NO ANIMATION) */
    /* ------------------------------------------- */
    
    .stApp {{
        /* Set static base properties */
        color: white;
        font-family: {COLORS['font_family']};
        background-color: {COLORS['dark_blue']}; 
        overflow: hidden; 
        
        background-image: 
            /* Vertical lines */
            repeating-linear-gradient(
                0deg, 
                transparent 0, transparent 49px, 
                rgba(103, 255, 242, 0.15) 50px /* Subtle Cyan Grid Line */
            ),
            /* Horizontal lines */
            repeating-linear-gradient(
                90deg, 
                transparent 0, transparent 49px, 
                rgba(67, 176, 175, 0.15) 50px /* Subtle Teal Grid Line */
            );
        
        background-size: 50px 50px; /* Define grid size */
        background-repeat: repeat;
        background-position: center;
        /* ANIMATION REMOVED */
    }}

    /* ------------------------------------------- */
    /* *** GUARANTEED VISIBILITY FIXES *** */
    /* ------------------------------------------- */
    
    /* FIX 1: Universal Selector (Forces Orbitron and White Text) */
    * {{
        color: white !important;
        font-family: {COLORS['font_family']} !important;
    }}
    
    /* Main Content Container: High opacity to ensure background is dark and clear */
    .main .block-container {{
        max-width: 900px; 
        padding: 60px 50px; 
        margin-left: auto;
        margin-right: auto;
        background-color: rgba(42, 48, 86, 0.98); /* HIGH OPACITY for a solid backdrop */
        border-radius: 15px;
        border: 3px solid {COLORS['cyan']}80; /* Brighter border */
        box-shadow: 0 0 35px {COLORS['cyan']}60; /* More intense glow */
        z-index: 10;
    }}
    
    /* Headers & Accent Colors */
    .main-header {{
        color: {COLORS['cyan']} !important; 
        font-size: 4.5em; 
        font-weight: 900;
        text-align: center;
        text-shadow: 0 0 35px {COLORS['cyan']}90; /* High intensity glow */
    }}
    .subheader {{
        color: white;
        font-size: 1.5em;
        text-align: center;
        margin-bottom: 40px;
    }}
    .stMarkdown h3 {{
        color: {COLORS['teal']} !important; 
        font-size: 2.6em; 
        font-weight: 700; 
        border-bottom: 4px solid {COLORS['dark_green']}; 
        padding-bottom: 10px;
        margin-top: 50px;
        margin-bottom: 18px;
    }}
    
    /* Input Field Text and Placeholder Styling */
    textarea, input[type="text"] {{
        color: {COLORS['cyan']} !important; /* BRIGHT text for user input */
        background-color: rgba(56, 63, 102, 1);
        border: 2px solid {COLORS['dark_green']};
        padding: 12px;
        font-size: 1.4em;
    }}
    textarea::placeholder, input[type="text"]::placeholder {{
        font-family: {COLORS['font_family']} !important;
        font-style: italic;
        color: {COLORS['cyan']} !important;
        opacity: 0.7; 
    }}
    
    /* File Uploader box */
    .stFileUploader {{
        border: 3px dashed {COLORS['dark_green']};
        padding: 25px;
        border-radius: 12px;
        background-color: rgba(56, 63, 102, 1);
    }}
    
    /* Buttons (kept high contrast) */
    div.stButton > button {{
        color: {COLORS['dark_blue']} !important;
        background-color: {COLORS['teal']} !important;
        font-size: 1.8em; 
        box-shadow: 0 0 30px {COLORS['teal']}A0; 
    }}
    .download-link-container a {{
        color: {COLORS['dark_blue']} !important;
        background-color:{COLORS['light_green']} !important;
        font-size: 1.6em;
        box-shadow: 0 0 25px {COLORS['light_green']}A0;
    }}
"""
st.markdown(f"<style>{CUSTOM_CSS}</style>", unsafe_allow_html=True)


# --- RAG Agent and Download Functions (UNCHANGED) ---

def generate_study_guide_content(file_name, user_query):
    st.info(f"RAG Agent analyzing **{file_name}** with prompt: '{user_query}'...")
    with st.spinner('Compiling knowledge modules and formatting output...'):
        time.sleep(4) 
    content = f"STUDY GUIDE GENERATED. Query: {user_query}. Content derived from {file_name}. All systems nominal."
    return content.encode('utf-8') 


def get_download_link(data, filename, text):
    b64 = base64.b64encode(data).decode()
    href = f"""
        <div class="download-link-container" style="text-align:center;">
            <a href="data:file/octet-stream;base64,{b64}" download="{filename}">{text}</a>
        </div>
    """
    return href

# ---------------------------------------------------
# --- Frontend Layout (UNCHANGED) ---
# ---------------------------------------------------

st.markdown('<p class="main-header">🧠 AI BASED STUDY PLANNER</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">AUTOMATED RAG-POWERED STUDY GUIDE GENERATION</p>', unsafe_allow_html=True)

st.markdown("<h3>1. INPUT SOURCE MATERIAL</h3>", unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "UPLOAD LECTURE TRANSCRIPTS OR SLIDES (PDF, DOCX, TXT)",
    type=['pdf', 'docx', 'txt'],
    key="file_uploader"
)

st.markdown("<h3>2. DEFINE SUMMARY QUERY</h3>", unsafe_allow_html=True)
user_query = st.text_area(
    "SPECIFY THE STRUCTURE: SUMMARIZE BY CHAPTER/WEEK, KEY TERMS ONLY, ETC.",
    height=200, 
    placeholder="E.G., SUMMARIZE THE CONTENT INTO 5 CHAPTERS FOCUSING ON ALL BOLDED TERMS, OR CREATE A 10-QUESTION QUIZ.",
    key="query_input"
)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 GENERATE STUDY GUIDE", key="generate_button"):
    if not uploaded_file or not user_query:
        st.error("🚨 **SYSTEM ALERT:** INITIATE FILE UPLOAD AND DEFINE QUERY TO PROCEED.")
    else:
        file_name = uploaded_file.name
        generated_content_bytes = generate_study_guide_content(file_name, user_query)
        
        st.success(f"✅ **GENERATION COMPLETE!** YOUR STUDY GUIDE IS READY TO DOWNLOAD.")
        
        download_filename = f"Generated_Guide_{file_name.replace('.', '_').replace(' ', '_')}.pdf"
        st.markdown(
            get_download_link(
                generated_content_bytes, 
                download_filename, 
                f"⬇️ DOWNLOAD {download_filename.upper()}"
            ), 
            unsafe_allow_html=True
        )