import streamlit as st
import plotly.graph_objects as go

# Cores da identidade visual (Mantidas para destaques)
COR_ROXO = "#6A0DAD"
COR_PRETO = "#000000"
COR_BRANCO = "#FFFFFF"
COR_ROXO_CLARO = "#8B5FBF"
COR_CINZA_ESCURO = "#2D2D2D"

# Função de cálculo
def simular_consorcio(valor_carta, parcelas, valor_parcela, percentual_venda, valor_embutido):
    valor_carta_liquido = valor_carta * (1 - valor_embutido / 100)
    valor_total_pago = parcelas * valor_parcela
    valor_venda = valor_carta_liquido * (percentual_venda / 100)
    lucro = valor_venda - valor_total_pago
    rendimento_bruto = (lucro / valor_total_pago) * 100 if valor_total_pago else 0
    rendimento_mensal = ((1 + rendimento_bruto / 100) ** (1 / parcelas) - 1) * 100 if rendimento_bruto > -100 and parcelas > 0 else 0
    return valor_total_pago, valor_venda, lucro, rendimento_bruto, rendimento_mensal, valor_carta_liquido

# Função para mostrar storytelling
def mostrar_storytelling():
    st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, {COR_ROXO} 0%, #2D2D2D 100%);
        padding: 40px;
        border-radius: 15px;
        color: white;
        margin: 20px 0;
    '>
        <h1 style='text-align: center; color: white; margin-bottom: 30px;'>🎯 A Revolução no Mercado de Consórcios</h1>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ## 💡 O Problema que Resolvemos
        
        **Imagine este cenário:**
        - 📉 **Clientes perdidos** por falta de clareza nos investimentos
        - 🤔 **Dúvidas constantes** sobre rentabilidade real do consórcio
        - 📊 **Falta de transparência** no processo de venda de cotas
        - 💸 **Oportunidades desperdiçadas** por cálculos complexos
        
        **Até agora...**
        """)
        
    with col2:
        st.markdown("📈")
        st.metric("Complexidade", "Alta", delta_color="off")
        st.metric("Transparência", "Baixa", delta_color="off")
    
    st.markdown("--- \n ## 🚀 Nossa Solução Inovadora")
    
    col1, col2, col3 = st.columns(3)
    
    card_style = f"padding: 20px; border-radius: 10px; border-left: 5px solid {COR_ROXO_CLARO}; height: 200px; margin-bottom: 20px; border: 1px solid rgba(128,128,128,0.2);"
    
    with col1:
        st.markdown(f"<div style='{card_style}'><h3>🎯 Simplicidade</h3><p>Interface intuitiva que qualquer cliente entende em segundos</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div style='{card_style}'><h3>💡 Transparência</h3><p>Todos os cálculos explicados passo a passo</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div style='{card_style}'><h3>📈 Confiança</h3><p>Resultados claros que geram segurança na decisão</p></div>", unsafe_allow_html=True)

    st.markdown("--- \n ## 🗺️ A Jornada do Cliente Transformada")
    st.error("### **ANTES** ❌ \n 🔴 **Cliente confuso** → Dúvidas não respondidas → Desistência → Perda de negócio")
    st.success("### **DEPOIS** ✅ \n 🟢 **Cliente curioso** → Simulação transparente → Confiança gerada → Negócio fechado")

# Função para mostrar cálculos
def mostrar_calculos():
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, {COR_ROXO} 0%, #2D2D2D 100%); padding: 40px; border-radius: 15px; color: white; margin: 20px 0; text-align: center;'>
        <h1 style='color: white; margin-bottom: 10px;'>🧮 Explicação dos Cálculos</h1>
        <p style='font-size: 1.2em; opacity: 0.9;'>Transparência total na metodologia aplicada</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**💰 Valor Líquido da Carta** \n Valor Líquido = Valor da Carta × (1 - Valor Embutido ÷ 100)")
        st.info("**💸 Valor Total Pago** \n Total Pago = Nº de Parcelas × Valor da Parcela")
    with col2:
        st.info("**📈 Lucro Realizado** \n Lucro = Valor de Venda - Total Pago")
        st.info("**📅 Rendimento Mensal** \n Rend. Mensal = [(1 + Rend. Bruto/100)^(1/Parcelas) - 1] × 100")

# Função principal do simulador
def mostrar_simulador():
    st.markdown(f"""
        <style>
            h1, h2, h3 {{ color: {COR_ROXO} !important; }}
            .stButton > button {{
                background-color: {COR_ROXO};
                color: white;
                font-weight: bold;
                border-radius: 8px;
                width: 100%;
            }}
            .result-subtitle {{
                color: {COR_ROXO};
                font-weight: 700;
                font-size: 2.0em;
                margin-top: 1em;
            }}
            .metric-subtitle {{
                color: {COR_ROXO};
                font-weight: 700;
                font-size: 1.2em;
            }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"<h1 style='text-align:center;'>📊 Simulador Consórcio - Carta de Crédito</h1>", unsafe_allow_html=True)

    st.sidebar.markdown(f"### 📥 Dados da simulação")
    valor_carta = st.sidebar.number_input("Valor da Carta (R$)", min_value=1000.0, step=500.0, format="%.2f")
    parcelas = st.sidebar.number_input("Número de Parcelas", min_value=1, step=1)
    valor_parcela = st.sidebar.number_input("Valor da Parcela (R$)", min_value=0.0, step=50.0, format="%.2f")
    percentual_venda = st.sidebar.selectbox("Porcentagem de Venda (%)", [20, 25, 30, 40])
    valor_embutido = st.sidebar.selectbox("Valor Embutido (%)", [0, 20, 40])

    if st.sidebar.button("🚀 Simular"):
        # ACIONAR BALÕES SEMPRE NO CLIQUE
        st.balloons()
        
        total_pago, valor_venda, lucro, rendimento_bruto, rendimento_mensal, valor_carta_liquido = simular_consorcio(
            valor_carta, parcelas, valor_parcela, percentual_venda, valor_embutido
        )

        st.markdown(f"<div class='result-subtitle'>🔍 Resultados da Simulação</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"<div class='metric-subtitle'>💳 Carta Líquida</div>", unsafe_allow_html=True)
            st.metric("", f"R$ {valor_carta_liquido:,.2f}")
            st.markdown(f"<div class='metric-subtitle'>💰 Total Pago</div>", unsafe_allow_html=True)
            st.metric("", f"R$ {total_pago:,.2f}")
        with col2:
            st.markdown(f"<div class='metric-subtitle'>🏷️ Venda da Carta</div>", unsafe_allow_html=True)
            st.metric("", f"R$ {valor_venda:,.2f}")
            st.markdown(f"<div class='metric-subtitle'>📈 Lucro</div>", unsafe_allow_html=True)
            st.metric("", f"R$ {lucro:,.2f}")

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"<div class='metric-subtitle'>📊 Rendimento Bruto</div>", unsafe_allow_html=True)
            st.metric("", f"{rendimento_bruto:.2f}%")
        with col_b:
            st.markdown(f"<div class='metric-subtitle'>📅 Rendimento Mensal</div>", unsafe_allow_html=True)
            st.metric("", f"{rendimento_mensal:.2f}%")

        if rendimento_mensal > 2:
            st.success("🏆 Excelente! Rendimento mensal acima de 2%.")
        elif rendimento_mensal > 1:
            st.info("🎯 Boa escolha! Rendimento razoável.")
        else:
            st.warning("⚠️ Rendimento baixo. Tente ajustar as variáveis.")

        st.progress(min(max(rendimento_mensal / 5, 0), 1))

        # Ajuste de cores do gráfico para não sumir no Light/Dark
        fig = go.Figure()
        fig.add_trace(go.Bar(name='Total Pago', x=['Simulação'], y=[total_pago], marker_color=COR_ROXO))
        fig.add_trace(go.Bar(name='Valor de Venda', x=['Simulação'], y=[valor_venda], marker_color=COR_ROXO_CLARO))
        fig.update_layout(
            barmode='group',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color=COR_ROXO)
        )
        st.plotly_chart(fig, use_container_width=True)

        with st.expander("📘 Como interpretar os resultados?"):
            st.write("Explicação detalhada sobre Carta Líquida, Lucro e Rendimentos.")

def main():
    st.set_page_config(page_title="Capital Invest", page_icon="📊", layout="wide")
    tab1, tab2, tab3 = st.tabs(["📊 Simulador", "🎯 Storytelling", "🧮 Cálculos"])
    with tab1: mostrar_simulador()
    with tab2: mostrar_storytelling()
    with tab3: mostrar_calculos()

if __name__ == "__main__":
    main()
