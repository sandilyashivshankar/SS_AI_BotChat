import os
import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# Load environment variables
load_dotenv()

# Streamlit Page Configuration
st.set_page_config(
    page_title="Mistral AI Studio | Shiv Shankar Tiwari",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Realistic & Modern Clean CSS Styling
st.markdown("""
<style>
    /* Main Background & Clean Typography */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }

    /* Sidebar Custom Profile Styling */
    .profile-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4);
    }
    
    .profile-name {
        font-size: 1.25rem;
        font-weight: 700;
        color: #38bdf8;
        margin-bottom: 0.2rem;
    }

    .profile-title {
        font-size: 0.85rem;
        color: #94a3b8;
        font-weight: 500;
        margin-bottom: 1rem;
    }

    .contact-item {
        font-size: 0.82rem;
        color: #cbd5e1;
        margin-bottom: 0.4rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .social-btn {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 8px;
        font-size: 0.8rem;
        font-weight: 600;
        text-decoration: none !important;
        margin-right: 6px;
        margin-top: 8px;
        transition: all 0.2s ease;
    }
    
    .btn-linkedin {
        background-color: #0077b5;
        color: white !important;
    }
    
    .btn-github {
        background-color: #333333;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* Header Banner */
    .header-box {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 1.8rem 2rem;
        backdrop-filter: blur(12px);
        margin-bottom: 1.5rem;
    }
    
    .header-title {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }

    .header-sub {
        color: #94a3b8;
        font-size: 1rem;
        margin-top: 0.4rem;
    }

    /* Content Cards */
    .content-card {
        background: #1e293b;
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 14px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }

    /* Output Box */
    .output-container {
        background: #090d16;
        border-left: 4px solid #38bdf8;
        border-radius: 8px;
        padding: 1.5rem;
        font-family: 'Georgia', serif;
        line-height: 1.8;
        font-size: 1.05rem;
        color: #e2e8f0;
        white-space: pre-wrap;
    }

    /* Modern Tabs Override */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #1e293b;
        padding: 6px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 42px;
        border-radius: 8px;
        color: #94a3b8;
        font-weight: 600;
        border: none !important;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #0284c7 !important;
        color: #ffffff !important;
    }

    /* Persona Badges */
    .badge-angry {
        background-color: rgba(239, 68, 68, 0.2);
        color: #f87171;
        border: 1px solid rgba(239, 68, 68, 0.4);
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
    }

    .badge-funny {
        background-color: rgba(245, 158, 11, 0.2);
        color: #fbbf24;
        border: 1px solid rgba(245, 158, 11, 0.4);
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
    }

    .badge-sad {
        background-color: rgba(59, 130, 246, 0.2);
        color: #60a5fa;
        border: 1px solid rgba(59, 130, 246, 0.4);
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# SIDEBAR: DEVELOPER PROFILE & CONTACT
# ------------------------------------------------------------------------------
st.sidebar.markdown("""
<div class="profile-card">
    <div style="text-align: center; margin-bottom: 0.8rem;">
        <span style="font-size: 3rem;">👨‍💻</span>
    </div>
    <div class="profile-name">Shiv Shankar Tiwari</div>
    <div class="profile-title">Data Scientist & AI-ML Engineer</div>
    <hr style="border-color: rgba(255,255,255,0.1); margin: 0.8rem 0;">
    <div class="contact-item">📞 <b>Phone:</b> +91 9889027860</div>
    <div class="contact-item">✉️ <b>Email:</b> shivshankartiwari312@gmail.com</div>
    <div style="margin-top: 1rem;">
        <a href="https://www.linkedin.com/in/sandilyashivshankar/" target="_blank" class="social-btn btn-linkedin">LinkedIn</a>
        <a href="https://github.com/sandilyashivshankar" target="_blank" class="social-btn btn-github">GitHub</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.caption("Powered by LangChain & Mistral AI")

# ------------------------------------------------------------------------------
# MAIN APP HEADER
# ------------------------------------------------------------------------------
st.markdown("""
<div class="header-box">
    <h1 class="header-title">Mistral AI Interactive Studio</h1>
    <p class="header-sub">Generative AI Poetry Workbench & Persona-Driven Conversational Agent</p>
</div>
""", unsafe_allow_html=True)

# Navigation Tabs
tab1, tab2 = st.tabs(["✍️ Poem Generator", "🎭 Persona Chat Engine"])

# ------------------------------------------------------------------------------
# TAB 1: MISTRAL POEM GENERATOR
# ------------------------------------------------------------------------------
with tab1:
    col_input, col_output = st.columns([1, 2], gap="large")

    with col_input:
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.subheader("Prompt Setup")
        
        prompt_text = st.text_input("Enter Topic / Prompt:", value="write a poem on AI")
        
        st.write("")
        st.markdown("**Configuration:**")
        st.markdown("- **Model:** `mistral-small-2506`")
        st.markdown("- **Temperature:** `0.9`")
        
        st.write("")
        run_poem = st.button("Generate Poem", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_output:
        st.subheader("Generated Poem")
        if run_poem:
            with st.spinner("Invoking Mistral AI..."):
                try:
                    model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)
                    response = model.invoke(prompt_text)
                    
                    st.markdown(f'<div class="output-container">{response.content}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error executing Mistral model: {e}")
        else:
            st.info("Click 'Generate Poem' to run the model.")

# ------------------------------------------------------------------------------
# TAB 2: PERSONA MULTI-MODE CHAT
# ------------------------------------------------------------------------------
with tab2:
    col_setup, col_chat = st.columns([1, 2], gap="large")

    with col_setup:
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.subheader("Choose AI Mode")
        
        choice = st.radio(
            "Select AI Persona:",
            (1, 2, 3),
            format_func=lambda x: {
                1: "Press 1 for Angry mode 😡",
                2: "Press 2 for Funny mode 😂",
                3: "Press 3 for Sad mode 😢"
            }[x]
        )

        # Map Choice to Persona Prompt
        if choice == 1:
            mode = "You are an angry AI agent. You respond aggressively and impatiently."
            badge = '<div class="badge-angry">😡 Angry AI Active</div>'
        elif choice == 2:
            mode = "You are a very funny AI agent. You respond with humor and jokes."
            badge = '<div class="badge-funny">😂 Funny AI Active</div>'
        else:
            mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."
            badge = '<div class="badge-sad">😢 Sad AI Active</div>'

        st.write("")
        st.markdown(badge, unsafe_allow_html=True)

        # Reset Session State on persona change
        if "selected_mode" not in st.session_state or st.session_state["selected_mode"] != choice:
            st.session_state["selected_mode"] = choice
            st.session_state["messages"] = [SystemMessage(content=mode)]
            st.session_state["chat_history"] = []

        st.write("")
        if st.button("Reset Conversation 🔄", use_container_width=True):
            st.session_state["messages"] = [SystemMessage(content=mode)]
            st.session_state["chat_history"] = []
            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

    with col_chat:
        st.subheader("Chat Assistant")
        
        # Display Message History
        for message in st.session_state["chat_history"]:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # Chat Input
        if user_prompt := st.chat_input("Type your message..."):
            st.session_state["messages"].append(HumanMessage(content=user_prompt))
            st.session_state["chat_history"].append({"role": "user", "content": user_prompt})
            
            with st.chat_message("user"):
                st.write(user_prompt)

            with st.chat_message("assistant"):
                with st.spinner("AI is responding..."):
                    try:
                        model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)
                        response = model.invoke(st.session_state["messages"])
                        
                        st.session_state["messages"].append(AIMessage(content=response.content))
                        st.session_state["chat_history"].append({"role": "assistant", "content": response.content})
                        st.write(response.content)
                    except Exception as e:
                        st.error(f"Chat Execution Error: {e}")