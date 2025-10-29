# import streamlit as st
# import time
# import base64
# from io import BytesIO

# # --- Configuration & Styling ---
# st.set_page_config(
#     page_title="Notes Publication Agent",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # Define the futuristic color palette
# COLORS = {
#     "dark_blue": "#2A3056",
#     "teal": "#43B0AF",
#     "cyan": "#67FFF2",
#     "dark_green": "#294933",
#     "light_green": "#81EC86",
#     "font_family": "Orbitron, sans-serif" 
# }

# # --- CUSTOM CSS WITH HOLOGRAPHIC RIPPLE & FORCED ORBITRON IN ALL ELEMENTS ---

# CUSTOM_CSS = f"""
#     /* 1. Import Orbitron Font */
#     @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
#     /* ------------------------------------------- */
#     /* LIVE DYNAMIC HOLOGRAPHIC RIPPLE ANIMATION */
#     /* ------------------------------------------- */
    
#     @keyframes holographic-shift {{
#         0%   {{ background-position: 0% 0%; }}
#         100% {{ background-position: 200px 200px; }}
#     }}
    
#     .stApp {{
#         color: white;
#         font-family: {COLORS['font_family']};
#         background-color: {COLORS['dark_blue']}; 
#         overflow: hidden; 
        
#         background-image: 
#             /* Layer 1: Horizontal stripes */
#             repeating-linear-gradient(
#                 90deg, 
#                 transparent 0%, transparent 1px, 
#                 rgba(67, 176, 175, 0.1) 2px, transparent 10px
#             ),
#             /* Layer 2: Diagonal glowing grid */
#             repeating-linear-gradient(
#                 45deg, 
#                 rgba(103, 255, 242, 0.05) 0%, rgba(103, 255, 242, 0.05) 1px, 
#                 transparent 10px, transparent 11px
#             );
        
#         background-size: 50px 50px, 50px 50px; 
#         background-repeat: repeat;
        
#         animation: holographic-shift 50s linear infinite; 
#         animation-play-state: running;
#     }}

#     /* ------------------------------------------- */
#     /* FONT & LAYOUT STYLES - GUARANTEED ORBITRON */
#     /* ------------------------------------------- */
    
#     /* Global Font Overrides: TARGETING ALL TEXT ELEMENTS WITH HIGH SPECIFICITY */
#     p, label, .stText, .stMarkdown, .stInfo, .stError, .stSuccess,
#     .stSelectbox label p, .stFileUploader label p, .stTextArea label p,
#     /* Crucial fix for Streamlit's internal widget text classes: */
#     .st-bd, .st-bh, .st-ce, .st-cf, .st-cc, .st-cj, .st-cn, .st-cp, .st-ch, .st-ci {{
#         font-family: {COLORS['font_family']} !important;
#     }}
    
#     /* Main Content Container */
#     .main .block-container {{
#         max-width: 850px;
#         padding: 50px 40px;
#         margin-left: auto;
#         margin-right: auto;
#         background-color: rgba(42, 48, 86, 0.95); 
#         border-radius: 15px;
#         border: 2px solid {COLORS['cyan']}40; 
#         box-shadow: 0 0 20px {COLORS['cyan']}30; 
#     }}
    
#     .main-header {{
#         color: {COLORS['cyan']};
#         font-size: 4em;
#         font-weight: 900;
#         text-align: center;
#         margin-bottom: 5px;
#         text-shadow: 0 0 20px {COLORS['cyan']}60;
#         line-height: 1.1;
#     }}
#     .subheader {{
#         color: white;
#         font-size: 1.4em;
#         text-align: center;
#         margin-bottom: 40px;
#         font-family: {COLORS['font_family']};
#     }}
    
#     .stMarkdown h3 {{
#         color: {COLORS['teal']};
#         font-size: 2.2em;
#         font-weight: 700; 
#         margin-top: 50px;
#         margin-bottom: 18px;
#         border-bottom: 3px solid {COLORS['dark_green']};
#         padding-bottom: 10px;
#         text-align: left;
#         font-family: {COLORS['font_family']};
#     }}
    
#     /* File Uploader and Text Area Box Styles */
#     .stFileUploader {{
#         border: 3px dashed {COLORS['dark_green']};
#         padding: 25px;
#         border-radius: 12px;
#         background-color: rgba(56, 63, 102, 0.98);
#     }}
    
#     /* Specific Input Fields: This targets the actual text and placeholder */
#     textarea, input[type="text"] {{
#         font-size: 1.3em;
#         color: {COLORS['cyan']};
#         background-color: rgba(56, 63, 102, 1);
#         border: 2px solid {COLORS['dark_green']};
#         padding: 10px;
#         font-family: {COLORS['font_family']} !important;
#     }}
    
#     /* Target the Placeholder Text specifically */
#     textarea::placeholder, input[type="text"]::placeholder {{
#         font-family: {COLORS['font_family']} !important;
#         font-style: italic;
#         color: rgba(103, 255, 242, 0.6);
#     }}
    
#     /* Button Styling */
#     div.stButton > button {{
#         background-color: {COLORS['teal']};
#         color: {COLORS['dark_blue']};
#         border-radius: 12px;
#         padding: 15px 35px;
#         font-size: 1.6em;
#         font-weight: 700;
#         border: none;
#         box-shadow: 0 0 25px {COLORS['teal']}80;
#         width: 100%;
#         font-family: {COLORS['font_family']};
#     }}
    
#     /* Download Button Styling */
#     .download-link-container a {{
#         color: {COLORS['dark_blue']} !important; 
#         text-decoration:none; 
#         display:inline-block; 
#         padding:18px 35px; 
#         background-color:{COLORS['light_green']}; 
#         border-radius:12px; 
#         font-weight:700;
#         font-size: 1.4em;
#         box-shadow: 0 0 18px {COLORS['light_green']}80;
#         margin-top: 20px;
#         width: 100%;
#         text-align: center;
#         font-family: {COLORS['font_family']};
#     }}
# """
# st.markdown(f"<style>{CUSTOM_CSS}</style>", unsafe_allow_html=True)


# # --- RAG Agent and Download Functions (UNCHANGED) ---

# def generate_study_guide_content(file_name, user_query):
#     # This is the simulated RAG call. Replace with your actual RAG logic.
#     st.info(f"RAG Agent analyzing **{file_name}** with prompt: '{user_query}'...")
#     with st.spinner('Compiling knowledge modules and formatting output...'):
#         time.sleep(4) 
#     content = f"STUDY GUIDE GENERATED. Query: {user_query}. Content derived from {file_name}. All systems nominal."
#     return content.encode('utf-8') 


# def get_download_link(data, filename, text):
#     b64 = base64.b64encode(data).decode()
#     href = f"""
#         <div class="download-link-container" style="text-align:center;">
#             <a href="data:file/octet-stream;base64,{b64}" download="{filename}">{text}</a>
#         </div>
#     """
#     return href

# # --- Frontend Layout ---

# st.markdown('<p class="main-header">🧠 NOTES PUBLICATION AGENT</p>', unsafe_allow_html=True)
# st.markdown('<p class="subheader">AUTOMATED RAG-POWERED STUDY GUIDE GENERATION</p>', unsafe_allow_html=True)

# st.markdown("<h3>1. INPUT SOURCE MATERIAL</h3>", unsafe_allow_html=True)
# uploaded_file = st.file_uploader(
#     "UPLOAD LECTURE TRANSCRIPTS OR SLIDES (PDF, DOCX, TXT)",
#     type=['pdf', 'docx', 'txt'],
#     key="file_uploader"
# )

# st.markdown("<h3>2. DEFINE SUMMARY QUERY</h3>", unsafe_allow_html=True)
# user_query = st.text_area(
#     "SPECIFY THE STRUCTURE: SUMMARIZE BY CHAPTER/WEEK, KEY TERMS ONLY, ETC.",
#     height=200, 
#     placeholder="E.G., SUMMARIZE THE CONTENT INTO 5 CHAPTERS FOCUSING ON ALL BOLDED TERMS, OR CREATE A 10-QUESTION QUIZ.",
#     key="query_input"
# )

# st.markdown("<br>", unsafe_allow_html=True)

# if st.button("🚀 GENERATE STUDY GUIDE", key="generate_button"):
#     if not uploaded_file or not user_query:
#         st.error("🚨 **SYSTEM ALERT:** INITIATE FILE UPLOAD AND DEFINE QUERY TO PROCEED.")
#     else:
#         file_name = uploaded_file.name
#         generated_content_bytes = generate_study_guide_content(file_name, user_query)
        
#         # --- REMOVED st.balloons() as requested ---
#         st.success(f"✅ **GENERATION COMPLETE!** YOUR STUDY GUIDE IS READY TO DOWNLOAD.")
        
#         download_filename = f"Generated_Guide_{file_name.replace('.', '_').replace(' ', '_')}.pdf"
#         st.markdown(
#             get_download_link(
#                 generated_content_bytes, 
#                 download_filename, 
#                 f"⬇️ DOWNLOAD {download_filename.upper()}"
#             ), 
#             unsafe_allow_html=True
#         )

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