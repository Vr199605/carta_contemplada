import streamlit as st
import plotly.graph_objects as go

# --- CONFIGURAÇÃO E CORES (Refatoração item 5) ---
COR_ROXO = "#6A0DAD"
COR_PRETO = "#000000"
COR_BRANCO = "#FFFFFF"
COR_FUNDO = "#1E1E1E"
COR_ROXO_CLARO = "#8B5FBF"
COR_CINZA_ESCURO = "#2D2D2D"
COR_AZUL_ESCURO = "#00008B"

# Helper para limpar o código de CSS (Item 5)
def estilo_card(titulo, texto, cor_borda="#8B5FBF", altura="200px"):
    return f"""
    <div style='background: #2D2D2D; padding: 20px; border-radius: 10px; border-left: 5px solid {cor_borda}; 
                height: {altura}; margin-bottom: 20px; color: white;'>
        <h3 style='color: #BB86FC; margin-top: 0;'>{titulo}</h3>
        <p style='color: #E0E0E0; line-height: 1.5;'>{texto}</p>
    </div>
    """

# --- LÓGICA DE CÁLCULO ---
def simular_consorcio(valor_carta, parcelas, valor_parcela, percentual_venda, valor_embutido):
    # Validação em tempo real (Item 3)
    if valor_parcela <= 0 or parcelas <= 0:
        return 0, 0, 0, 0, 0, 0
        
    valor_carta_liquido = valor_carta * (1 - valor_embutido / 100)
    valor_total_pago = parcelas * valor_parcela
    valor_venda = valor_carta_liquido * (percentual_venda / 100)
    lucro = valor_venda - valor_total_pago
    rendimento_bruto = (lucro / valor_total_pago) * 100 if valor_total_pago else 0
    rendimento_mensal = ((1 + rendimento_bruto / 100) ** (1 / parcelas) - 1) * 100 if rendimento_bruto > -100 and parcelas > 0 else 0
    return valor_total_pago, valor_venda, lucro, rendimento_bruto, rendimento_mensal, valor_carta_liquido

# --- COMPONENTES VISUAIS ---
def mostrar_storytelling():
    st.markdown("<div style='background: linear-gradient(135deg, #6A0DAD 0%, #2D2D2D 100%); padding: 40px; border-radius: 15px; color: white; margin: 20px 0;'>"
                "<h1 style='text-align: center; color: white; margin-bottom: 30px;'>🎯 A Revolução no Mercado de Consórcios</h1></div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<div style='color: white;'>## 💡 O Problema que Resolvemos\n**Imagine este cenário:**\n- 📉 **Clientes perdidos**\n- 🤔 **Dúvidas constantes**\n- 📊 **Falta de transparência**\n- 💸 **Oportunidades desperdiçadas**\n**Até agora...**</div>", unsafe_allow_html=True)
    with col2:
        st.metric("Complexidade", "Alta", delta_color="off")
        st.metric("Transparência", "Baixa", delta_color="off")

    st.markdown("<div style='color: white;'>--- \n## 🚀 Nossa Solução Inovadora</div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.markdown(estilo_card("🎯 Simplicidade", "Interface intuitiva que qualquer cliente entende."), unsafe_allow_html=True)
    c2.markdown(estilo_card("💡 Transparência", "Todos os cálculos explicados passo a passo."), unsafe_allow_html=True)
    c3.markdown(estilo_card("📈 Confiança", "Resultados claros que geram segurança."), unsafe_allow_html=True)

def mostrar_calculos():
    st.markdown("<h1 style='text-align: center;'>🧮 Explicação dos Cálculos</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(estilo_card("💰 Valor Líquido", "Valor da Carta × (1 - Embutido / 100)", altura="150px"), unsafe_allow_html=True)
    with col2:
        st.markdown(estilo_card("📈 Lucro Realizado", "Valor de Venda - Total Pago", altura="150px"), unsafe_allow_html=True)

def mostrar_simulador():
    st.markdown(f"<style>h1, h2, h3 {{ color: {COR_ROXO} !important; }} .sidebar-subtitle {{ color: {COR_BRANCO} !important; font-weight: bold; font-size: 1.3em; }}</style>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center;'>📊 Simulador Consórcio - Capital Invest</h1>", unsafe_allow_html=True)

    # --- SIDEBAR COM CENÁRIOS (Item 1) ---
    st.sidebar.markdown("<div class='sidebar-subtitle'>📥 Cenário Atual</div>", unsafe_allow_html=True)
    valor_carta = st.sidebar.number_input("Valor da Carta (R$)", min_value=1000.0, value=100000.0, step=500.0)
    parcelas = st.sidebar.number_input("Nº de Parcelas", min_value=1, value=24)
    valor_parcela = st.sidebar.number_input("Valor da Parcela (R$)", min_value=0.0, value=500.0)
    percentual_venda = st.sidebar.selectbox("Venda (%)", [20, 25, 30, 40])
    valor_embutido = st.sidebar.selectbox("Embutido (%)", [0, 20, 40])

    # Validação em tempo real (Item 3)
    if valor_parcela <= 0:
        st.sidebar.warning("⚠️ Insira o valor da parcela para calcular.")
        return

    # Cálculo do cenário atual
    res = simular_consorcio(valor_carta, parcelas, valor_parcela, percentual_venda, valor_embutido)
    total_pago, valor_venda, lucro, rend_bruto, rend_mensal, carta_liq = res

    # --- EXIBIÇÃO DE RESULTADOS ---
    col1, col2, col3 = st.columns(3)
    col1.metric("💳 Carta Líquida", f"R$ {carta_liq:,.2f}")
    col2.metric("🏷️ Venda", f"R$ {valor_venda:,.2f}")
    col3.metric("📈 Lucro", f"R$ {lucro:,.2f}")

    # --- CUSTO DE OPORTUNIDADE (Item 4) ---
    st.markdown(f"### 💸 Custo de Oportunidade")
    # Comparação hipotética com Poupança (0.5% am) e Selic (0.9% am)
    poupanca_acumulada = total_pago * ((1.005)**parcelas - 1)
    selic_acumulada = total_pago * ((1.009)**parcelas - 1)
    
    c_op1, c_op2 = st.columns(2)
    c_op1.metric("Rendimento Poupança Est.", f"R$ {poupanca_acumulada:,.2f}", delta=f"{lucro - poupanca_acumulada:,.2f} vs Consórcio")
    c_op2.metric("Rendimento Selic Est.", f"R$ {selic_acumulada:,.2f}", delta=f"{lucro - selic_acumulada:,.2f} vs Consórcio")

    # --- GRÁFICOS COM INTERATIVIDADE (Item 6) ---
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Investimento Total', x=['Resultado'], y=[total_pago], marker_color=COR_ROXO,
                         hovertemplate="O que você pagou: R$%{y:,.2f}<extra></extra>"))
    fig.add_trace(go.Bar(name='Lucro (Grupo Maldivas)', x=['Resultado'], y=[lucro], marker_color=COR_AZUL_ESCURO,
                         hovertemplate="Seu ganho limpo: R$%{y:,.2f}<extra></extra>"))
    
    fig.update_layout(barmode='group', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color=COR_BRANCO,
                      title="💹 Comparativo Financeiro Real")
    st.plotly_chart(fig, use_container_width=True)

    # Gauge de Performance
    gauge = go.Figure(go.Indicator(
        mode="gauge+number", value=rend_mensal,
        title={'text': "📅 Rendimento Mensal (%)", 'font': {'color': COR_ROXO}},
        gauge={'axis': {'range': [0, 5]}, 'bar': {'color': COR_ROXO},
               'steps': [{'range': [0, 1], 'color': "gray"}, {'range': [1, 2.5], 'color': COR_ROXO_CLARO}, {'range': [2.5, 5], 'color': COR_AZUL_ESCURO}]}
    ))
    gauge.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color=COR_BRANCO)
    st.plotly_chart(gauge, use_container_width=True)

def main():
    st.set_page_config(page_title="Capital Invest - CFO Hub", page_icon="📊", layout="wide")
    tab1, tab2, tab3 = st.tabs(["📊 Simulador Profissional", "🎯 Storytelling", "🧮 Metodologia"])
    with tab1: mostrar_simulador()
    with tab2: mostrar_storytelling()
    with tab3: mostrar_calculos()

if __name__ == "__main__":
    main()
