import streamlit as st
from fpdf import FPDF

# 1. CONFIGURAÇÃO DA PÁGINA E DESIGN PREMIUM
st.set_page_config(page_title="Freelance Gold | PT", page_icon="⚖️", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #FAFAFA; }
    h1 { color: #1E1E1E; font-family: 'Helvetica Neue', sans-serif; font-weight: 800; letter-spacing: -1px; }
    .stButton>button { 
        width: 100%; border-radius: 5px; height: 3em; 
        background-color: #1E1E1E; color: white; border: none; transition: 0.3s; 
    }
    .stButton>button:hover { background-color: #D4AF37; color: white; }
    [data-testid="stMetricValue"] { font-size: 28px; color: #D4AF37; }
    .footer { font-size: 11px; color: gray; text-align: justify; margin-top: 50px; border-top: 1px solid #ddd; padding-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNÇÃO PARA GERAR PDF ---
def gerar_pdf(nome, valor, servico):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Recibo de Prestação de Serviços", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"Eu, {nome}, confirmo que recebi a quantia de {valor}€ "
                              f"relativa ao serviço de: {servico}.")
    return pdf.output(dest='S').encode('latin-1')

# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.title("💎 Freelance Gold")
opcao = st.sidebar.radio("Navegação", ["Simulador Fiscal", "Gerador de Recibo"])

st.sidebar.divider()
st.sidebar.markdown("### ✨ Versão Premium")
st.sidebar.write("- Relatórios Trimestrais")
st.sidebar.write("- Planeamento de IVA")
if st.sidebar.button("Aceder ao Premium"):
    st.balloons()
    st.sidebar.success("Lista de espera aberta!")

# --- CONTEÚDO PRINCIPAL ---
st.title("Freelance Gold")
st.caption("A ferramenta de gestão fiscal para profissionais de elite em Portugal.")

if opcao == "Simulador Fiscal":
    st.subheader("Simulador Fiscal Recibos Verdes")
    
    with st.container():
        col_in1, col_in2 = st.columns(2)
        with col_in1:
            ganho_mensal = st.number_input("Faturação Mensal Bruta (€)", min_value=0.0, step=100.0)
        with col_in2:
            categoria = st.selectbox("Categoria de Atividade", ["Serviços (Coef. 0.75)", "Vendas (Coef. 0.15)"])

    coeficiente = 0.75 if "Serviços" in categoria else 0.15
    ss_estimada = (ganho_mensal * 0.70) * 0.214
    base_irs = ganho_mensal * coeficiente

    st.markdown("### 📊 Estimativa de Obrigações")
    c1, c2, c3 = st.columns(3)
    c1.metric("Seg. Social", f"{ss_estimada:.2f}€")
    c2.metric("Base IRS", f"{base_irs:.2f}€")
    c3.metric("Líquido Est.", f"{(ganho_mensal - ss_estimada):.2f}€")
    
    st.info("💡 Este cálculo baseia-se no regime simplificado de 2026.")

elif opcao == "Gerador de Recibo":
    st.header("📄 Gerador de Recibo Profissional")
    with st.form("form_recibo"):
        nome = st.text_input("Seu Nome Completo")
        servico = st.text_area("Descrição do Serviço Prestado")
        valor = st.number_input("Valor total recebido (€)", min_value=0.0)
        submit = st.form_submit_button("Gerar Documento PDF")
        
        if submit:
            if nome and servico and valor > 0:
                pdf_bytes = gerar_pdf(nome, valor, servico)
                st.download_button(label="📥 Descarregar Recibo PDF", 
                                   data=pdf_bytes, 
                                   file_name="recibo_freelance.pdf", 
                                   mime="application/pdf")
            else:
                st.error("Por favor, preencha todos os campos.")

# --- RODAPÉ LEGAL ---
st.markdown("""
<div class="footer">
    <strong>Aviso Legal:</strong> Este site é uma ferramenta informativa de apoio e não substitui o aconselhamento de um profissional ou da Autoridade Tributária. 
    Os cálculos são estimativas baseadas na legislação de 2026. Não armazenamos os seus dados.
</div>
""", unsafe_allow_html=True)