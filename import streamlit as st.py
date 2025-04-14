import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: #0d0d0d;
        color: #00ffff;
        font-family: 'Share Tech Mono', monospace;
    }
    .stTextInput > div > input {
        background-color: #1a1a1a;
        color: #00ffff;
        border: 2px solid #00ffff;
        border-radius: 8px;
        box-shadow: 0 0 10px #00ffff;
    }
    .stButton > button {
        background-color: #ff00ff;
        color: white;
        border: none;
        border-radius: 8px;
        box-shadow: 0 0 15px #ff00ff;
    }
    h1 {
        text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("👾 ALT - Interface Neural Cyberpunk")

texto = st.text_input("Digite sua mensagem:")

if texto:
    resposta = "Traduzindo mensagem..."  # Aqui você pode conectar seu modelo futuramente
    st.markdown(f"🧠 Resposta: `{resposta}`")
