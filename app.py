import streamlit as st

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="NoRio 2026",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS (DESIGN BLINDADO E ALINHADO) ---
st.markdown("""
    <style>
    /* Esconde elementos padrão */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    
    /* Fundo da página */
    .stApp {
        background-color: #FFFFFF;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    /* CARD CENTRAL */
    .block-container {
        background-color: #FFFFFF;
        padding: 3rem 2.5rem;
        border-radius: 25px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.12);
        max-width: 500px;
        margin: auto;
        border: 1px solid #e0e0e0;
    }
    
    /* TÍTULO PRINCIPAL */
    h1 {
        color: #001F5B !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: 800;
        text-align: center;
        letter-spacing: -1px;
        margin-bottom: 1rem !important;
        font-size: 2.2rem !important;
        line-height: 1.2;
    }
    
    /* MENSAGEM FINAL */
    .event-message {
        text-align: center;
        color: #001F5B;
        font-size: 1.5rem;
        font-weight: 700;
        margin-top: 20px;
        line-height: 1.4;
    }
    
    </style>
""", unsafe_allow_html=True)


# --- 4. INTERFACE ---

st.markdown("<h1>Réveillon NoRio 2026</h1>", unsafe_allow_html=True)

st.markdown("""
    <div class='event-message'>
        Nos aguardamos no Réveillon NoRio
    </div>
""", unsafe_allow_html=True)

st.write("")