import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Page Configuration
st.set_page_config(
    page_title="Dynamic Theme Groq Bot", 
    page_icon="🤖", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Dynamic Theme Keyword & CSS Injector Engine
def apply_dynamic_theme(query: str):
    query_lower = query.lower()
    
    # Theme color definitions (Gradient background + Accent glow)
    themes = {
        "space": {
            "bg": "linear-gradient(135deg, #0b0d17 0%, #1c1035 50%, #082032 100%)",
            "accent": "#00f2fe",
            "card_bg": "rgba(20, 25, 45, 0.65)",
            "icon": "🚀"
        },
        "code": {
            "bg": "linear-gradient(135deg, #0d1117 0%, #161b22 50%, #0d2818 100%)",
            "accent": "#2ea043",
            "card_bg": "rgba(22, 27, 34, 0.75)",
            "icon": "⚡"
        },
        "finance": {
            "bg": "linear-gradient(135deg, #06101e 0%, #0b2545 50%, #134074 100%)",
            "accent": "#00b4d8",
            "card_bg": "rgba(11, 37, 69, 0.65)",
            "icon": "📈"
        },
        "nature": {
            "bg": "linear-gradient(135deg, #05190e 0%, #132a13 50%, #31572c 100%)",
            "accent": "#52b788",
            "card_bg": "rgba(19, 42, 19, 0.65)",
            "icon": "🌿"
        },
        "health": {
            "bg": "linear-gradient(135deg, #1f0318 0%, #320d2b 50%, #4a1236 100%)",
            "accent": "#ff4d6d",
            "card_bg": "rgba(50, 13, 43, 0.65)",
            "icon": "🍎"
        },
        "default": {
            "bg": "linear-gradient(135deg, #0f0c20 0%, #15102a 50%, #241442 100%)",
            "accent": "#a855f7",
            "card_bg": "rgba(30, 20, 50, 0.65)",
            "icon": "🤖"
        }
    }
    
    # Match query keywords to theme
    selected_theme = "default"
    if any(k in query_lower for k in ["space", "mars", "star", "planet", "galaxy", "orbit", "cosmos"]):
        selected_theme = "space"
        st.toast("Theme Switched: Deep Space 🚀")
    elif any(k in query_lower for k in ["code", "python", "bug", "script", "app", "developer", "sql", "api", "function"]):
        selected_theme = "code"
        st.toast("Theme Switched: Developer Matrix ⚡")
    elif any(k in query_lower for k in ["money", "crypto", "stock", "finance", "invest", "bank", "market", "trading"]):
        selected_theme = "finance"
        st.toast("Theme Switched: High Finance 📈")
    elif any(k in query_lower for k in ["tree", "plant", "ocean", "animal", "earth", "nature", "forest", "green"]):
        selected_theme = "nature"
        st.toast("Theme Switched: Eco Nature 🌿")
    elif any(k in query_lower for k in ["health", "workout", "gym", "food", "diet", "doctor", "fit", "sleep"]):
        selected_theme = "health"
        st.toast("Theme Switched: Active Health 🍎")

    theme = themes[selected_theme]

    # Dynamic CSS with Keyframe Animations & Glassmorphism
    css = f"""
    <style>
    /* Animated Main Background */
    .stApp {{
        background: {theme["bg"]};
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: #ffffff;
        transition: all 0.8s ease-in-out;
    }}

    @keyframes gradientBG {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    /* Title Glow & Animation */
    .animated-header {{
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(90deg, #ffffff, {theme["accent"]});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: pulseGlow 3s ease-in-out infinite alternate;
    }}

    @keyframes pulseGlow {{
        from {{ filter: drop-shadow(0 0 2px {theme["accent"]}); }}
        to {{ filter: drop-shadow(0 0 12px {theme["accent"]}); }}
    }}

    /* Response Glassmorphism Card */
    .response-card {{
        background: {theme["card_bg"]};
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        animation: fadeInUp 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        margin-top: 20px;
    }}

    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Customizing Streamlit Button */
    .stButton > button {{
        background: linear-gradient(90deg, {theme["accent"]}, #6366f1) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 28px !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
    }}

    .stButton > button:hover {{
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 6px 20px {theme["accent"]}66 !important;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
    return theme["icon"]

# 3. Sidebar Configuration
with st.sidebar:
    st.image("https://groq.com/wp-content/uploads/2024/03/PBG-mark-1.svg", width=60)
    st.header("Groq Configuration")
    
    groq_api_key = st.text_input("Groq API Key", type="password", placeholder="gsk_...")
    
    model = st.selectbox(
        "Select Model", 
        ["llama-3.3-70b-versatile", "mixtral-8x7b-32768", "gemma2-9b-it"]
    )
    
    col1, col2 = st.columns(2)
    with col1:
        temperature = st.slider("Temp", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
    with col2:
        max_tokens = st.slider("Tokens", min_value=128, max_value=4096, value=1024, step=128)

# 4. Main App Interface
question = st.text_area("Ask anything:", key="user_input", placeholder="Ask about code, space, money, nature, health...")

# Apply background theme dynamically based on input
active_icon = apply_dynamic_theme(question if question else "")

st.markdown(f'<div class="animated-header">{active_icon} Interactive Groq AI</div>', unsafe_allow_html=True)
st.caption("Background theme auto-adapts in real-time based on your prompt topics!")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful, clear, and engaging AI assistant."),
    ("user", "Question: {input}")
])

# 5. Generation Logic
if st.button("✨ Generate Response"):
    if not groq_api_key:
        st.error("🔑 Please enter your Groq API Key in the sidebar to run requests.")
    elif not question.strip():
        st.warning("⚠️ Please enter a question first.")
    else:
        try:
            with st.spinner("⚡ Processing on Groq LPU speed..."):
                llm = ChatGroq(
                    model=model,
                    groq_api_key=groq_api_key,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
                output_parser = StrOutputParser()
                chain = prompt | llm | output_parser
                
                response = chain.invoke({"input": question})

            # Render response inside animated glassmorphism container
            st.markdown(
                f"""
                <div class="response-card">
                    <h4 style="margin-top:0; color:#fff;">{active_icon} AI Assistant Output</h4>
                    <hr style="border-color: rgba(255,255,255,0.1);">
                </div>
                """, 
                unsafe_allow_html=True
            )
            st.markdown(response)

        except Exception as e:
            st.error(f"Execution Error: {str(e)}")