import streamlit as st
import pandas as pd
import time

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="NoRio 2026",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 🔗 CONFIGURAÇÃO DA PLANILHA (LINK REAL INSERIDO)
# ==============================================================================
URL_DA_PLANILHA = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRUKXXyPy65HyuqrIzsxqlN-Ii5-i3Rwgi5kt48uVlp0d5JDFPNBkFCnw2SZ_26XJzgtCv7NqZ_y6vp/pub?gid=1464058578&single=true&output=csv"
# ==============================================================================


# --- 2. CSS (DESIGN BLINDADO E ALINHADO) ---
st.markdown("""
    <style>
    /* Esconde elementos padrão */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
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
    
    /* TEXTO DE AVISO (DISCLAIMER) */
    .disclaimer {
        text-align: center;
        color: #555555;
        font-size: 0.9rem;
        line-height: 1.4;
        margin-bottom: 30px;
        font-weight: 400;
    }
    
    /* TÍTULO DO INPUT */
    .input-label {
        text-align: center;
        color: #001F5B;
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 10px;
        display: block;
    }
    
    /* --- INPUT DE TEXTO --- */
    .stTextInput label { display: none; }
    
    .stTextInput input {
        text-align: center;
        font-size: 20px;
        border-radius: 10px;
        padding: 16px;
        border: 2px solid #d0d0d0;
        background-color: #f4f4f4 !important;
        color: #000000 !important;
        caret-color: #001F5B;
        transition: all 0.3s;
        width: 100%;
        box-sizing: border-box;
        letter-spacing: 2px;
    }
    
    ::placeholder { color: #888888 !important; opacity: 1; letter-spacing: normal; }
    
    .stTextInput input:focus {
        border-color: #B8860B;
        background-color: #ffffff !important;
        box-shadow: 0 0 0 2px rgba(184, 134, 11, 0.2);
    }

    /* --- CORREÇÃO DEFINITIVA DO BOTÃO BUSCAR (FLEXBOX) --- */
    .stButton {
        width: 100% !important;
        display: flex !important;
        justify-content: center !important;
        margin-top: 15px;
    }
    
    .stButton > button {
        width: 100% !important;
        display: block !important;
        flex: 1 !important;
        background-color: #001F5B !important;
        color: #ffffff !important;
        border: none;
        padding: 18px;
        font-size: 16px;
        border-radius: 10px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        transition: 0.3s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .stButton > button:hover {
        background-color: #003399 !important;
        transform: translateY(-2px);
    }
    .stButton > button * { color: #ffffff !important; }
    
    /* --- BOTÃO COMPRAR (DOURADO) --- */
    a[kind="primary"] {
        width: 100%;
        background: linear-gradient(135deg, #B8860B 0%, #FFD700 100%);
        color: #ffffff !important;
        text-decoration: none;
        padding: 18px;
        border-radius: 10px;
        font-weight: 700;
        font-size: 18px;
        text-align: center;
        display: block;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(184, 134, 11, 0.3);
        transition: all 0.3s ease;
        border: none;
        margin-top: 15px;
        box-sizing: border-box;
    }
    a[kind="primary"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(184, 134, 11, 0.4);
        color: #ffffff !important;
    }
    
    /* --- BOTÃO SECUNDÁRIO (COPO) --- */
    a[kind="secondary"] {
        width: 100%;
        background-color: transparent;
        color: #001F5B !important;
        text-decoration: none;
        padding: 16px;
        border-radius: 10px;
        font-weight: 700;
        font-size: 16px;
        text-align: center;
        display: block;
        text-transform: uppercase;
        letter-spacing: 1px;
        border: 2px solid #001F5B;
        margin-top: 10px;
        box-sizing: border-box;
        transition: all 0.3s ease;
    }
    a[kind="secondary"]:hover {
        background-color: #001F5B;
        color: #ffffff !important;
        transform: translateY(-2px);
    }
    
    .success-text {
        text-align: center;
        color: #001F5B;
        font-size: 1.1rem;
        margin: 30px 0 20px 0;
        line-height: 1.5;
    }
    
    /* MENSAGEM DE ERRO (VERMELHA) */
    .error-msg {
        color: #d32f2f;
        background-color: #ffebee;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        margin-top: 15px;
        font-size: 0.95rem;
        font-weight: bold;
        border: 1px solid #ffcdd2;
    }
    </style>
""", unsafe_allow_html=True)


# --- 3. CARREGAMENTO DE DADOS (GOOGLE SHEETS EM TEMPO REAL) ---
@st.cache_data(ttl=5)
def load_data():
    if URL_DA_PLANILHA == "COLE_SEU_LINK_CSV_AQUI" or not URL_DA_PLANILHA.startswith("http"):
        return "LINK_NAO_CONFIGURADO"
    try:
        # Tenta ler o CSV do Google
        df = pd.read_csv(URL_DA_PLANILHA)
        df.columns = df.columns.str.strip() # Limpa espaços nos nomes das colunas
        
        # Garante que a coluna Telefone seja tratada como texto
        if 'Telefone' in df.columns:
             df['Telefone'] = df['Telefone'].astype(str)
        
        return df
    except Exception as e:
        return f"ERRO_CONEXAO: {e}"

# Tenta carregar os dados
df_loaded = load_data()


# --- 4. INTERFACE ---

st.markdown("<h1>Réveillon NoRio 2026</h1>", unsafe_allow_html=True)

st.markdown("""
    <div class='disclaimer'>
        Seu telefone é a identificação única e exclusiva para o seu link de compra.<br>
        <strong>Não compartilhe o seu link.</strong>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='input-label'>Insira o número do seu telefone</div>", unsafe_allow_html=True)

# Input com trava de 11 dígitos
telefone_input = st.text_input("hidden_label", placeholder="77999262626", max_chars=11, label_visibility="collapsed")

# Botão
buscar = st.button("BUSCAR LINK")

if buscar:
    # 1. Limpa tudo que não for número
    apenas_numeros = ''.join(filter(str.isdigit, telefone_input))
    
    # 2. VALIDAÇÃO RIGOROSA: Tem que ser EXATAMENTE 11
    if len(apenas_numeros) != 11:
        st.markdown(f"""
            <div class='error-msg'>
                ⚠️ Digite exatamente 11 números (DDD + Telefone).<br>
                Você digitou {len(apenas_numeros)}.
            </div>
        """, unsafe_allow_html=True)
        
    # 3. VERIFICAÇÃO DE CONEXÃO
    elif isinstance(df_loaded, str) and df_loaded == "LINK_NAO_CONFIGURADO":
         st.markdown(f"<div class='error-msg'>⚠️ Erro Técnico: Link da planilha não configurado.</div>", unsafe_allow_html=True)
    elif isinstance(df_loaded, str) and df_loaded.startswith("ERRO_CONEXAO:"):
         st.markdown(f"<div class='error-msg'>⚠️ Erro ao conectar com o Google. Verifique sua internet.</div>", unsafe_allow_html=True)
    elif df_loaded is None:
         st.markdown("<div class='error-msg'>⚠️ Erro desconhecido ao carregar dados.</div>", unsafe_allow_html=True)
         
    else:
        # 4. BUSCA REAL NA PLANILHA
        df = df_loaded # Usa o dataframe carregado
        with st.spinner(text=''):
            time.sleep(0.5)
            
            encontrado = False
            nome_cliente = ""
            link_pagamento = ""
            link_copo = ""
            
            # --- LOOP DE BUSCA ---
            for index, row in df.iterrows():
                # Busca segura usando .get
                # Tenta pegar pelo nome da coluna, ou pelo índice (0=Nome, 1=Telefone, 2=Link)
                # Isso deixa o código mais robusto caso o nome da coluna mude um pouco
                nome_excel = row.get('Nome', row.iloc[0] if len(row) > 0 else 'Cliente')
                tel_excel_raw = str(row.get('Telefone', row.iloc[1] if len(row) > 1 else ''))
                link_excel = row.get('Link Pagamento', row.iloc[2] if len(row) > 2 else '')
                link_copo_excel = row.get('Link Copo', row.iloc[3] if len(row) > 3 else '')
                
                # Limpeza do número da planilha
                tel_excel = tel_excel_raw.replace(".0", "").strip()
                tel_excel_limpo = ''.join(filter(str.isdigit, tel_excel))
                
                # Comparação
                if apenas_numeros == tel_excel_limpo:
                    encontrado = True
                    nome_cliente = nome_excel
                    link_pagamento = link_excel
                    link_copo = link_copo_excel
                    break
            
            # --- RESULTADO FINAL ---
            if encontrado:
                # Verifica se o link é válido
                if pd.isna(link_pagamento) or str(link_pagamento).strip() == "" or str(link_pagamento) == "nan":
                    st.markdown(f"<div class='error-msg'>Olá {nome_cliente}. Seu link ainda não foi gerado. Aguarde alguns minutos.</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                        <div class="success-text">
                            Olá, <strong>{nome_cliente}</strong>.<br>
                            Seu link de pagamento é:
                        </div>
                    """, unsafe_allow_html=True)
                    
                    
                    # Verifica se tem link do copo
                    link_copo_final = link_copo if (link_copo and str(link_copo).strip() != "" and str(link_copo) != "nan") else "#"
                    
                    st.link_button("COMPRE AGORA  >", link_pagamento, type="primary", use_container_width=True)
                    if link_copo_final != "#":
                         st.link_button("COMPRAR COPO DA FESTA >", link_copo_final, type="secondary", use_container_width=True)
            else:
                st.markdown("<div class='error-msg'>❌ Número não encontrado. Verifique se digitou corretamente ou se já preencheu o formulário.</div>", unsafe_allow_html=True)

st.write("")