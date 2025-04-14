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
  
    h1 {
        text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
        animation: cyberpunk 2s ease-in-out infinite;
    }

    @keyframes cyberpunk {
        0% {
            color: #00ffff;
            text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
        }
        50% {
            color: #ff00ff;
            text-shadow: 0 0 5px #ff00ff, 0 0 10px #ff00ff;
        }
        100% {
            color: #00ffff;
            text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("👾 ALT - Interface Neural Cyberpunk")

texto = st.text_input("Digite sua mensagem:")

if texto:
    # Resposta da ALT, você pode personalizar o que ALT responde.
    resposta = f"ALT: Oi! Eu sou a Inteligência Artificial de Interface Neural. Como posso ajudar?"
    st.markdown(f"🧠 Resposta: `{resposta}`")
