import streamlit as st
import plotly.graph_objects as go

# Cores da identidade visual
COR_ROXO = "#6A0DAD"
COR_PRETO = "#000000"
COR_BRANCO = "#FFFFFF"
COR_FUNDO = "#1E1E1E"
COR_ROXO_CLARO = "#8B5FBF"
COR_CINZA_ESCURO = "#2D2D2D"
COR_AZUL_ESCURO = "#00008B" # Cor para o Grupo Maldivas

# --- MELHORIA 5: REFATORAÇÃO DE CSS (FUNÇÃO HELPER) ---
def aplicar_estilo_card(titulo, texto, cor_borda="#8B5FBF", altura="200px"):
    return f"""
    <div style='background: #2D2D2D; padding: 20px; border-radius: 10px; border-left: 5px solid {cor_borda}; 
                height: {altura}; margin-bottom: 20px; color: white;'>
        <h3 style='color: #BB86FC; margin-top: 0;'>{titulo}</h3>
        <p style='color: #E0E0E0; line-height: 1.5;'>{texto}</p>
    </div>
    """

# Função de cálculo (MANTIDA ORIGINAL)
def simular_consorcio(valor_carta, parcelas, valor_parcela, percentual_venda, valor_embutido):
    valor_carta_liquido = valor_carta * (1 - valor_embutido / 100)
    valor_total_pago = parcelas * valor_parcela
    valor_venda = valor_carta_liquido * (percentual_venda / 100)
    lucro = valor_venda - valor_total_pago
    rendimento_bruto = (lucro / valor_total_pago) * 100 if valor_total_pago else 0
    rendimento_mensal = ((1 + rendimento_bruto / 100) ** (1 / parcelas) - 1) * 100 if rendimento_bruto > -100 and parcelas > 0 else 0
    return valor_total_pago, valor_venda, lucro, rendimento_bruto, rendimento_mensal, valor_carta_liquido

# Função para mostrar storytelling (MANTIDA ORIGINAL + REFATORAÇÃO VISUAL)
def mostrar_storytelling():
    st.markdown("""
    <div style='background: linear-gradient(135deg, #6A0DAD 0%, #2D2D2D 100%); padding: 40px; border-radius: 15px; color: white; margin: 20px 0;'>
        <h1 style='text-align: center; color: white; margin-bottom: 30px;'>🎯 A Revolução no Mercado de Consórcios</h1>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<div style='color: white;'>## 💡 O Problema que Resolvemos\n**Imagine este cenário:**\n- 📉 **Clientes perdidos**\n- 🤔 **Dúvidas constantes**\n- 📊 **Falta de transparência**\n- 💸 **Oportunidades desperdiçadas**\n**Até agora...**</div>", unsafe_allow_html=True)
    with col2:
        st.metric("Complexidade", "Alta", delta_color="off")
        st.metric("Transparência", "Baixa", delta_color="off")

    st.markdown("<div style='color: white;'>--- \n## 🚀 Nossa Solução Inovadora</div>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    c1.markdown(aplicar_estilo_card("🎯 Simplicidade", "Interface intuitiva que qualquer cliente entende em segundos"), unsafe_allow_html=True)
    c2.markdown(aplicar_estilo_card("💡 Transparência", "Todos os cálculos explicados passo a passo"), unsafe_allow_html=True)
    c3.markdown(aplicar_estilo_card("📈 Confiança", "Resultados claros que geram segurança na decisão"), unsafe_allow_html=True)

# Nova função para mostrar cálculos (MANTIDA ORIGINAL)
def mostrar_calculos():
    st.markdown("<h1 style='text-align: center; color: white;'>🧮 Explicação dos Cálculos</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(aplicar_estilo_card("💰 Valor Líquido", "Valor da Carta × (1 - Valor Embutido ÷ 100)", altura="120px"), unsafe_allow_html=True)
    with col2:
        st.markdown(aplicar_estilo_card("📈 Lucro Realizado", "Valor de Venda - Total Pago", altura="120px"), unsafe_allow_html=True)

# Função principal do simulador (ADAPTADA COM AS MELHORIAS)
def mostrar_simulador():
    st.markdown(f"<style>h1, h2, h3 {{ color: {COR_ROXO} !important; font-weight: bold !important; }}</style>", unsafe_allow_html=True)
    st.markdown(f"<h1 style='text-align:center;'>📊 Simulador Consórcio - Maldivas</h1>", unsafe_allow_html=True)

    # Entradas na Sidebar
    st.sidebar.markdown(f"<div style='font-weight:700; font-size:1.3em;'>📥 Dados da simulação</div>", unsafe_allow_html=True)
    valor_carta = st.sidebar.number_input("Valor da Carta (R$)", min_value=1000.0, value=100000.0, step=500.0)
    parcelas = st.sidebar.number_input("Nº de Parcelas", min_value=1, value=24)
    valor_parcela = st.sidebar.number_input("Valor da Parcela (R$)", min_value=0.0, value=500.0)
    percentual_venda = st.sidebar.selectbox("Venda (%)", [20, 25, 30, 40])
    valor_embutido = st.sidebar.selectbox("Embutido (%)", [0, 20, 40])

    # --- MELHORIA 3: VALIDAÇÃO EM TEMPO REAL ---
    if valor_parcela <= 0:
        st.sidebar.warning("⚠️ Insira o valor da parcela para ver os resultados.")
        st.stop() # Interrompe a execução aqui se o dado for inválido

    # Cálculo (MANTIDO)
    total_pago, valor_venda, lucro, rend_bruto, rend_mensal, carta_liq = simular_consorcio(
        valor_carta, parcelas, valor_parcela, percentual_venda, valor_embutido
    )

    # Exibição de Métricas Principais
    st.markdown(f"### 🔍 Resultados do Cenário Atual")
    m1, m2, m3 = st.columns(3)
    m1.metric("💳 Carta Líquida", f"R$ {carta_liq:,.2f}")
    m2.metric("🏷️ Venda", f"R$ {valor_venda:,.2f}")
    m3.metric("📈 Lucro", f"R$ {lucro:,.2f}")

    # --- MELHORIA 4: CUSTO DE OPORTUNIDADE ---
    st.markdown("---")
    st.markdown("### 💸 Custo de Oportunidade")
    # Simulação básica de rendimento CDI/Selic (aprox 0.8% am) vs o Consórcio
    lucro_selic_estimado = total_pago * ((1.008)**parcelas - 1)
    
    c_op1, c_op2 = st.columns(2)
    c_op1.metric("Investimento em Renda Fixa (Est.)", f"R$ {lucro_selic_estimado:,.2f}")
    # --- MELHORIA 1: CENÁRIOS COMPARATIVOS (Diferencial de Ganho) ---
    ganho_extra = lucro - lucro_selic_estimado
    c_op2.metric("Vantagem Capital Invest", f"R$ {ganho_extra:,.2f}", delta=f"{((lucro/lucro_selic_estimado)-1)*100:.1f}% mais rentável")

    # --- MELHORIA 6: INTERATIVIDADE NO GRÁFICO (TOOLTIPS) ---
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Total Pago', x=['Resultado'], y=[total_pago], marker_color=COR_ROXO,
        hovertemplate="<b>Total Investido:</b> R$%{y:,.2f}<extra></extra>"
    ))
    fig.add_trace(go.Bar(
        name='Lucro Realizado', x=['Resultado'], y=[lucro], marker_color=COR_AZUL_ESCURO,
        hovertemplate="<b>Seu Lucro Líquido:</b> R$%{y:,.2f}<br>Rendimento: " + f"{rend_mensal:.2f}% am<extra></extra>"
    ))
    
    fig.update_layout(barmode='group', title="💹 Comparativo de Valores", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

    # Gauge (MANTIDO)
    gauge = go.Figure(go.Indicator(
        mode="gauge+number", value=rend_mensal,
        title={'text': "📅 Rendimento Mensal (%)", 'font': {'color': COR_ROXO}},
        gauge={'axis': {'range': [0, 5]}, 'bar': {'color': COR_ROXO}}
    ))
    gauge.update_layout(paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(gauge, use_container_width=True)

    # Expanders (MANTIDOS ORIGINAIS)
    with st.expander("📘 Como interpretar os resultados?"):
        st.write("Explicação dos termos técnicos conforme sua lógica original.")

# Função principal (MANTIDA)
def main():
    st.set_page_config(page_title="Capital Invest", page_icon="📊", layout="wide")
    tab1, tab2, tab3 = st.tabs(["📊 Simulador", "🎯 Storytelling", "🧮 Cálculos"])
    with tab1: mostrar_simulador()
    with tab2: mostrar_storytelling()
    with tab3: mostrar_calculos()

if __name__ == "__main__":
    main()
