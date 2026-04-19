import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from controllers.processamento import simular_cdi

def simulacao_page():
    st.title("📊 Simulação")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        valor_inicial = st.number_input(
            "Valor Inicial",
            min_value=0.0,
            value=1000.0,
            step=100.0,
            format="%.2f"
        )
        
        valor_mensal = st.number_input(
            "Valor a cada Mês",
            min_value=0.0,
            value=500.0,
            step=100.0,
            format="%.2f"
        )
        
        meses = st.slider(
            "Número de Meses",
            min_value=1,
            max_value=120,
            value=12,
            step=1
        )
        
        if st.button("Calcular Simulação"):
            resultado = simular_cdi(valor_inicial, valor_mensal, meses)
            
            st.markdown("---")
            
            col1, col2 = st.columns(2)
            
            col1.metric("Valor Final", f"R$ {resultado['valor_final']:,.2f}")
            col2.metric("Total Investido", f"R$ {(valor_inicial + valor_mensal * meses):,.2f}")
            
            st.markdown("---")
            
            st.subheader("📈 Evolução do Investimento")
            
            historico_df = pd.DataFrame(resultado['historico'])
            
            fig_evolucao = go.Figure()
            fig_evolucao.add_trace(go.Scatter(
                x=historico_df['mes'],
                y=historico_df['valor'],
                mode='lines+markers',
                name='Valor Acumulado',
                line=dict(color='#00d2ff', width=3)
            ))
            
            fig_evolucao.update_layout(
                title="Evolução do Investimento",
                xaxis_title="Mês",
                yaxis_title="Valor (R$)",
                yaxis_tickprefix="R$ "
            )
            
            st.plotly_chart(fig_evolucao, use_container_width=True)