import streamlit as st
from fpdf import FPDF

# Configuração da Página
st.set_page_config(page_title="Gestor Freelancer Pro", page_icon="💰")

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

# --- INTERFACE ---
st.title("🚀 Ferramenta para Freelancers Portugal")
st.sidebar.header("Menu de Ferramentas")
opcao = st.sidebar.selectbox("Escolha o que deseja fazer:", 
                               ["Calculadora de Impostos (IRS/SS)", "Gerador de Recibo Rápido"])

if opcao == "Calculadora de Impostos (IRS/SS)":
    st.header("🧮 Calculadora de Carga Fiscal (Recibos Verdes)")
    
    ganho_mensal = st.number_input("Quanto faturou este mês? (€)", min_value=0.0, step=100.0)
    categoria = st.selectbox("Tipo de Atividade:", ["Serviços (Coeficiente 0.75)", "Venda de Produtos (Coeficiente 0.15)"])
    
    coeficiente = 0.75 if "Serviços" in categoria else 0.15
    
    # Cálculos Matemáticos (Base simplificada PT)
    # Base Tributável IRS = Ganhos * Coeficiente
    # Segurança Social (SS) = (Ganhos * 0.70) * 0.214
    
    base_tributavel = ganho_mensal * coeficiente
    ss_estimada = (ganho_mensal * 0.70) * 0.214
    
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Segurança Social (Est.)", f"{ss_estimada:.2f}€")
    with col2:
        st.write(f"**Base Tributável para IRS:** {base_tributavel:.2f}€")
        st.caption("Nota: O valor final de IRS depende do seu escalão anual.")

    st.info("💡 Dica: Reserve sempre cerca de 25% a 30% do seu faturamento bruto para obrigações fiscais.")

elif opcao == "Gerador de Recibo Rápido":
    st.header("📄 Gerar Recibo Simples (PDF)")
    
    with st.form("meu_form"):
        nome = st.text_input("Seu Nome Completo")
        servico = st.text_area("Descrição do Serviço")
        valor = st.number_input("Valor total (€)", min_value=0.0)
        submit = st.form_submit_button("Gerar PDF")
        
        if submit:
            pdf_bytes = gerar_pdf(nome, valor, servico)
            st.download_button(label="📥 Descarregar Recibo", 
                               data=pdf_bytes, 
                               file_name="recibo.pdf", 
                               mime="application/pdf")
            
            
            st.divider() # Cria uma linha divisória

# Texto Legal no fundo do site
st.markdown("""
<style>
    .footer {
        font-size: 12px;
        color: gray;
        text-align: justify;
    }
</style>
<div class="footer">
    <strong>Aviso Legal e Termos de Uso:</strong><br>
    Este site é uma ferramenta de apoio informativo e não substitui o aconselhamento profissional de um contabilista certificado ou da Autoridade Tributária. 
    Os cálculos apresentados são estimativas baseadas nos coeficientes padrão do regime simplificado em Portugal (2026). 
    O utilizador é inteiramente responsável pela verificação e submissão dos seus dados fiscais. 
    Não armazenamos dados pessoais ou financeiros introduzidos nestes formulários. 
    Ao utilizar este site, concorda que os criadores não são responsáveis por quaisquer erros, omissões ou decisões tomadas com base nestas informações.
</div>
""", unsafe_allow_html=True)