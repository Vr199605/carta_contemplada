import streamlit as st
import plotly.graph_objects as go

# Cores da identidade visual
COR_ROXO = "#6A0DAD"
COR_PRETO = "#000000"
COR_BRANCO = "#FFFFFF"
COR_FUNDO = "#1E1E1E"
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
    st.markdown("""
    <div style='
        background: linear-gradient(135deg, #6A0DAD 0%, #2D2D2D 100%);
        padding: 40px;
        border-radius: 15px;
        color: white;
        margin: 20px 0;
    '>
        <h1 style='text-align: center; color: white; margin-bottom: 30px;'>🎯 A Revolução no Mercado de Consórcios</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Introdução impactante
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
    
    # Solução
    st.markdown("""
    ---
    
    ## 🚀 Nossa Solução Inovadora
    
    **Criamos uma ferramenta que transforma complexidade em clareza:**
    """)
    
    # Benefícios em cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='
            background: #2D2D2D;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #8B5FBF;
            height: 200px;
            margin-bottom: 20px;
        '>
            <h3 style='color: #BB86FC; margin-top: 0;'>🎯 Simplicidade</h3>
            <p style='color: #E0E0E0; line-height: 1.5;'>Interface intuitiva que qualquer cliente entende em segundos</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='
            background: #2D2D2D;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #8B5FBF;
            height: 200px;
            margin-bottom: 20px;
        '>
            <h3 style='color: #BB86FC; margin-top: 0;'>💡 Transparência</h3>
            <p style='color: #E0E0E0; line-height: 1.5;'>Todos os cálculos explicados passo a passo</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='
            background: #2D2D2D;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #8B5FBF;
            height: 200px;
            margin-bottom: 20px;
        '>
            <h3 style='color: #BB86FC; margin-top: 0;'>📈 Confiança</h3>
            <p style='color: #E0E0E0; line-height: 1.5;'>Resultados claros que geram segurança na decisão</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Jornada do cliente
    st.markdown("""
    ---
    
    ## 🗺️ A Jornada do Cliente Transformada
    
    ### **ANTES** ❌
    """)
    
    st.markdown("""
    <div style='
        background: #3A2D2D;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 5px solid #FF6B6B;
    '>
    🔴 **Cliente confuso** → Dúvidas não respondidas → Desistência → Perda de negócio
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### **DEPOIS** ✅")
    
    st.markdown("""
    <div style='
        background: #2D3A2D;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 5px solid #4CAF50;
    '>
    🟢 **Cliente curioso** → Simulação transparente → Confiança gerada → Negócio fechado
    </div>
    """, unsafe_allow_html=True)
    
    # Diferenciais competitivos
    st.markdown("""
    ---
    
    ## 🏆 O que Nos Torna Únicos
    
    ### 🎨 **Experiência Visual Impactante**
    - Design premium com identidade visual forte
    - Gráficos interativos que contam uma história
    - Animações que engajam o cliente
    
    ### 🧮 **Inteligência nos Cálculos**
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Cálculos que realizamos:**
        - 💰 Valor líquido da carta
        - 📊 Rentabilidade real
        - 🎯 Comparativo de cenários
        - 📈 Projeções mensais
        """)
    
    with col2:
        st.markdown("""
        **Benefícios:**
        - ✅ Decisões baseadas em dados
        - ✅ Clareza total nos números
        - ✅ Confiança no investimento
        - ✅ Redução de objeções
        """)
    
    # Resultados esperados
    st.markdown("""
    ---
    
    ## 📊 Impacto nos Negócios
    
    **Com esta ferramenta, esperamos:**
    """)
    
    metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)
    
    with metrics_col1:
        st.metric("🎯 Conversão", "+40%", "vs método tradicional")
    
    with metrics_col2:
        st.metric("💼 Fechamentos", "+35%", "em consórcios")
    
    with metrics_col3:
        st.metric("😊 Satisfação", "95%", "dos clientes")
    
    with metrics_col4:
        st.metric("⏱️ Tempo Venda", "-60%", "por operação")
    
    # Call to Action final
    st.markdown("""
    ---
    """)
    
    st.markdown("""
   

    ## 💫 O Futuro Começa Agora
    
    **Esta ferramenta posiciona nossa empresa como:**
    
    - 🏆 **Líder em inovação** no mercado de consórcios
    - 💡 **Referência em transparência** para clientes
    - 📊 **Pioneira em tecnologia** aplicada a investimentos
    - 🎯 **Expert em experiência** do cliente
    """)
    
    st.markdown("""
    <div style='
        background: #2D2D2D;
        padding: 25px;
        border-radius: 10px;
        text-align: center;
        margin: 30px 0;
        border: 1px solid #8B5FBF;
    '>
        <h3 style='color: #BB86FC; margin: 0;'>✨ Esta não é uma simples calculadora - é a ponte entre a dúvida do cliente e a certeza do investimento!</h3>
    </div>
    """, unsafe_allow_html=True)

# Função principal do simulador
def mostrar_simulador():
    # Estilo visual
    st.markdown(f"""
        <style>
            .main {{
                background-color: {COR_FUNDO};
                color: {COR_BRANCO};
            }}
            body {{
                color: {COR_BRANCO};
                background-color: {COR_FUNDO};
            }}
            h1, h2, h3, .stMarkdown {{
                color: {COR_ROXO} !important;
                font-weight: bold !important;
            }}
            .stButton > button {{
                background-color: {COR_ROXO};
                color: white;
                font-weight: bold;
                border-radius: 8px;
            }}
            .stSidebar > div:first-child {{
                background-color: {COR_PRETO};
                color: {COR_BRANCO};
            }}
            .stMetric label {{
                color: {COR_BRANCO};
                font-size: 1.1em;
                font-weight: 600;
            }}
            .result-subtitle {{
                color: {COR_ROXO};
                font-weight: 700;
                font-size: 2.0em;
                margin-bottom: 0.75em;
                margin-top: 1em;
            }}
            .metric-subtitle {{
                color: {COR_ROXO};
                font-weight: 700;
                font-size: 1.2em;
                margin-bottom: 0.15em;
                margin-top: 0.7em;
            }}
            /* ESTILOS PARA SUBTÍTULOS EM BRANCO */
            .sidebar-subtitle {{
                color: {COR_BRANCO} !important;
                font-weight: 700;
                font-size: 1.3em;
                margin-bottom: 0.5em;
                margin-top: 1em;
            }}
            .input-label {{
                color: {COR_BRANCO} !important;
                font-weight: 600;
                font-size: 1.1em;
                margin-bottom: 0.3em;
            }}
            .stSelectbox label, .stNumberInput label {{
                color: {COR_BRANCO} !important;
                font-weight: 600;
                font-size: 1.1em;
            }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"<h1 style='text-align:center;'>📊 Simulador Consórcio - Carta de Crédito</h1>", unsafe_allow_html=True)

    # Entradas - COM SUBTÍTULOS EM BRANCO
    st.sidebar.markdown(f"<div class='sidebar-subtitle'>📥 Dados da simulação</div>", unsafe_allow_html=True)
    
    # Adicionando labels customizados em branco para cada input
    st.sidebar.markdown(f"<div class='input-label'>Valor da Carta de Crédito (R$)</div>", unsafe_allow_html=True)
    valor_carta = st.sidebar.number_input(
        "Valor da Carta de Crédito (R$)", 
        min_value=1000.0, 
        step=500.0, 
        format="%.2f",
        label_visibility="collapsed"
    )
    
    st.sidebar.markdown(f"<div class='input-label'>Número de Parcelas</div>", unsafe_allow_html=True)
    parcelas = st.sidebar.number_input(
        "Número de Parcelas", 
        min_value=1, 
        step=1,
        label_visibility="collapsed"
    )
    
    st.sidebar.markdown(f"<div class='input-label'>Valor da Parcela (R$)</div>", unsafe_allow_html=True)
    valor_parcela = st.sidebar.number_input(
        "Valor da Parcela (R$)", 
        min_value=0.0, 
        step=50.0, 
        format="%.2f",
        label_visibility="collapsed"
    )
    
    st.sidebar.markdown(f"<div class='input-label'>Porcentagem de Venda (%)</div>", unsafe_allow_html=True)
    percentual_venda = st.sidebar.selectbox(
        "Porcentagem de Venda (%)", 
        [20, 25, 30, 40],
        label_visibility="collapsed"
    )
    
    st.sidebar.markdown(f"<div class='input-label'>Valor Embutido (%)</div>", unsafe_allow_html=True)
    valor_embutido = st.sidebar.selectbox(
        "Valor Embutido (%)", 
        [0, 20, 40],
        label_visibility="collapsed"
    )

    # Botão
    if st.sidebar.button("🚀 Simular"):
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

        st.markdown(f"<div class='metric-subtitle'>📊 Rendimento Bruto</div>", unsafe_allow_html=True)
        st.metric("", f"{rendimento_bruto:.2f}%")

        st.markdown(f"<div class='metric-subtitle'>📅 Rendimento Mensal (Comp.)</div>", unsafe_allow_html=True)
        st.metric("", f"{rendimento_mensal:.2f}%")

        if rendimento_mensal > 2:
            st.balloons()
            st.success("🏆 Excelente! Rendimento mensal acima de 2%.")
        elif rendimento_mensal > 1:
            st.info("🎯 Boa escolha! Rendimento razoável.")
        else:
            st.warning("⚠️ Rendimento baixo. Tente ajustar as variáveis.")

        progresso = min(max(rendimento_mensal / 5, 0), 1)
        st.progress(progresso)

        fig = go.Figure()
        fig.add_trace(go.Bar(name='Total Pago', x=['Simulação'], y=[total_pago], marker_color=COR_ROXO))
        fig.add_trace(go.Bar(name='Valor de Venda', x=['Simulação'], y=[valor_venda], marker_color='#BB86FC'))
        fig.add_trace(go.Bar(name='Lucro', x=['Simulação'], y=[lucro], marker_color='#3700B3'))
        fig.update_layout(
            barmode='group',
            title={'text': '💹 Comparativo de Valores', 'font': {'size': 24, 'color': COR_ROXO}, 'x': 0.5},
            xaxis_title={'text': 'Indicadores', 'font': {'size': 18, 'color': COR_ROXO}},
            yaxis_title={'text': 'R$', 'font': {'size': 18, 'color': COR_ROXO}},
            legend=dict(font=dict(size=16, color=COR_ROXO)),
            paper_bgcolor=COR_FUNDO,
            plot_bgcolor=COR_FUNDO,
            font_color=COR_BRANCO
        )
        st.plotly_chart(fig, use_container_width=True)

        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=rendimento_mensal,
            title={'text': "📅 Rendimento Mensal (%)", 'font': {'size': 22, 'color': COR_ROXO}},
            gauge={
                'axis': {'range': [0, 5]},
                'bar': {'color': COR_ROXO},
                'steps': [
                    {'range': [0, 1], 'color': "#3A3A3A"},
                    {'range': [1, 3], 'color': "#7F39FB"},
                    {'range': [3, 5], 'color': "#BB86FC"},
                ],
            },
            domain={'x': [0, 1], 'y': [0, 1]}
        ))
        gauge.update_layout(paper_bgcolor=COR_FUNDO, font_color=COR_BRANCO)
        st.plotly_chart(gauge, use_container_width=True)

        # Explicações
        with st.expander("📘 Como interpretar os resultados?"):
            st.markdown("""
            - **Carta Líquida:** Valor restante da carta após o embutido.
            - **Lucro:** Valor da venda menos o que foi pago.
            - **Rendimento Bruto:** Lucro em relação ao total investido.
            - **Rendimento Mensal:** Equivalente composto ao longo dos meses.
            """)

        # Passo a passo didático
        with st.expander("📋 Passo a Passo da Venda Contemplada"):
            st.markdown("""
            ### 🔄 Etapas para Vender Sua Cota Contemplada

            **1️⃣ Contemplação da Carta**  
            O primeiro passo é ter sua cota contemplada, o que pode acontecer de duas formas:
            - **Por sorteio**, o que geralmente torna a carta **mais atrativa para os compradores**;
            - **Por lance fixo***, uma opção comum e também valorizada no mercado.  
            * *O lance fixo costuma ter boa aceitação entre investidores.*

            **2️⃣ Solicitação do Extrato Financeiro da Cota**  
            Após a contemplação, você solicita à administradora do consórcio o **extrato financeiro detalhado da cota**.  
            🔎 Esse documento mostra tudo: valor da carta, saldo devedor, parcelas pagas e demais informações financeiras.  
            📝 *Importante: A administradora é legalmente obrigada a fornecer esse extrato.*

            **3️⃣ Envio para Análise da Capital Invest**  
            Você envia o extrato para a Capital Invest, que irá analisar cuidadosamente as condições da sua cota.  
            Isso inclui o valor líquido disponível, o histórico de pagamentos e possíveis pendências.

            **4️⃣ Proposta e Pagamento Inicial ao Cliente**  
            Após a análise, fazemos uma **proposta de compra personalizada** da sua carta.  
            ✅ Se você **aceitar**, poderá receber um **pagamento em torno de 20 a 30% do valor da carta**.  
            💡 *Esse valor pode variar conforme as condições específicas da sua cota e a negociação acordada.*
            """)
        st.success("✅ Simulação concluída com sucesso!")

# Função principal
def main():
    # Configuração da página
    st.set_page_config(
        page_title="Simulador Consórcio - Capital Invest",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Abas principais
    tab1, tab2 = st.tabs(["📊 Simulador", "🎯 Storytelling"])
    
    with tab1:
        mostrar_simulador()
        
    with tab2:
        mostrar_storytelling()

if __name__ == "__main__":
    main()


