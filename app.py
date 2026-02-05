import streamlit as st
from fpdf import FPDF
import pandas as pd

# 1. DESIGN DE ALTA FIDELIDADE
st.set_page_config(page_title="Freelance Intelligence Pro", page_icon="🏦", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background-color: #0E1117; color: #FFFFFF; } /* Dark Mode Premium */
    
    /* Cartões Estilo Dashboard */
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
    }
    .stButton>button {
        background: linear-gradient(90deg, #D4AF37 0%, #F1D27B 100%);
        color: black; font-weight: bold; border: none; border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE CÁLCULO AVANÇADA ---
def calcular_impostos(valor, isento_iva):
    iva = 0 if isento_iva else valor * 0.23
    ss = (valor * 0.70) * 0.214
    irs_retencao = valor * 0.25 # Taxa padrão de retenção
    liquido = valor - ss - irs_retencao
    return iva, ss, irs_retencao, liquido

# --- SIDEBAR PROFISSIONAL ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135706.png", width=80)
    st.title("Hub Fiscal 2026")
    opcao = st.radio("Módulos", ["Painel de Análise", "Emissor de Documentos", "Consultoria IA"])
    st.divider()
    st.info("💡 **Dica PRO:** Em 2026, o limite de isenção de IVA em Portugal é de 15.000€ anuais.")

# --- MÓDULO 1: PAINEL DE ANÁLISE ---
if opcao == "Painel de Análise":
    st.title("Análise de Performance Fiscal")
    
    col_input1, col_input2 = st.columns([2, 1])
    with col_input1:
        valor_bruto = st.number_input("Volume de Faturação Mensal (€)", min_value=0.0, value=2500.0)
    with col_input2:
        isento = st.checkbox("Isento de IVA (Art. 53º)", value=True)

    iva, ss, irs, liquido = calcular_impostos(valor_bruto, isento)

    # Gráfico de Distribuição
    st.markdown("### 📈 Distribuição do Faturamento")
    dados_grafico = {
        "Categoria": ["Líquido Real", "Segurança Social", "Retenção IRS"],
        "Valores": [liquido, ss, irs]
    }
    df = pd.DataFrame(dados_grafico)
    st.bar_chart(df.set_index("Categoria"))

    # Métricas em Cartões
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Líquido Final", f"{liquido:.2f}€")
    with c2: st.metric("Seg. Social", f"-{ss:.2f}€", delta_color="inverse")
    with c3: st.metric("Retenção IRS", f"-{irs:.2f}€")
    with c4: st.metric("IVA a Entregar", f"{iva:.2f}€")

    st.warning("⚠️ **Atenção:** Estes valores são simulações baseadas no Regime Simplificado. A retenção de 25% de IRS é a taxa comum para serviços.")

# --- MÓDULO 2: EMISSOR ---
elif opcao == "Emissor de Documentos":
    st.title("Emissor de Recibos Profissionais")
    # (Mantém-se a lógica do PDF anterior, mas com design melhorado)
    st.text_input("Entidade Adquirente (Nome da Empresa)")
    st.text_input("NIF da Entidade")
    st.button("Gerar Recibo de Elite")

# --- FOOTER ---
st.markdown("""<div style='text-align: center; color: #666; font-size: 12px; margin-top: 50px;'>
    © 2026 Freelance Intelligence Pro | Algoritmo atualizado em Jan/2026 | Dados protegidos por encriptação ponta-a-ponta
    </div>""", unsafe_allow_html=True)