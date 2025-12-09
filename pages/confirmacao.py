import streamlit as st
import time

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Confirmação - NoRio 2026",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS (IDÊNTICO AO APP.PY PARA MANTER PADRÃO) ---
st.markdown("""
    <style>
    /* Esconde elementos padrão e sidebar */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;} /* Esconde a sidebar explicitamente */
    
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
    
    /* MENSAGEM SUCESSO */
    .success-message {
        text-align: center;
        color: #001F5B;
        font-size: 1.3rem;
        font-weight: 600;
        margin: 30px 0;
        line-height: 1.5;
    }

    .check-icon {
        font-size: 4rem;
        text-align: center;
        display: block;
        margin-bottom: 20px;
        color: #B8860B; /* Dourado */
    }
    
    /* BOTÃO VOLTAR */
    a.voltar-btn {
        width: 100%;
        background-color: transparent;
        color: #555 !important;
        text-decoration: none;
        padding: 12px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 14px;
        text-align: center;
        display: block;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 40px;
        transition: all 0.3s ease;
    }
    a.voltar-btn:hover {
        color: #001F5B !important;
        background-color: #f4f4f4;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. INTERFACE ---

st.markdown("<h1>Réveillon NoRio 2026</h1>", unsafe_allow_html=True)

st.markdown("""
    <div class='check-icon'>✨</div>
    <div class='success-message'>
        Parabéns!<br>
        Sua compra foi concluída com sucesso.
    </div>
    <div style='text-align: center; color: #666; font-size: 0.9rem; margin-bottom: 20px;'>
        Aguardamos você para viver momentos inesquecíveis.
    </div>
""", unsafe_allow_html=True)

# Botão para voltar ao início (opcional, já que é redirect)
st.markdown("<a href='../' target='_self' class='voltar-btn'>Voltar para o início</a>", unsafe_allow_html=True)
