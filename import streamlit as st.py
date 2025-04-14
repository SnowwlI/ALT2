import streamlit as st

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom, #371819, #0d0907);
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

    .neon-response {
        color: #ff0044;
        font-weight: bold;
        text-shadow: 0 0 5px #ff0044, 0 0 10px #ff0044;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title(" ALT - Interface Neural Cyberpunk")

texto = st.text_input("Digite sua mensagem:")

if texto:
    resposta = "ALT Neural Response™"  # Simulação de resposta
    st.markdown(f"<div class='neon-response'>🧠 Resposta: {resposta}</div>", unsafe_allow_html=True)
