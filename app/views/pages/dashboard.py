import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from models.database import get_all_dados, get_dados_por_fonte, get_dados_por_categoria

def dashboard_page():
    st.title("🏠 Dashboard")
    st.markdown("---")
    
    dados = get_all_dados()
    
    if not dados:
        st.info("Nenhum dado disponível. Faça upload de CSV ou utilize a simulação.")
        return
    
    dados_df = pd.DataFrame([dict(d) for d in dados])
    
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Total de Registros", len(dados))
    col2.metric("Total Valorizado", f"R$ {dados_df['valor'].sum():,.2f}")
    col3.metric("CDI Médio", f"{dados_df['cdi'].mean():.2%}")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Radar de Eficiência de Custo por Fonte")
        
        dados_fonte = get_dados_por_fonte()
        df_fonte = pd.DataFrame([dict(d) for d in dados_fonte])
        
        fig = go.Figure(data=go.Scatterpolar(
            r=df_fonte['total'],
            theta=df_fonte['fonte'],
            fill='toself',
            name='Eficiência'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(range=[0, df_fonte['total'].max() * 1.2]),
                angularaxis=dict(direction="clockwise")
            ),
            showlegend=True,
            title="Distribuição por Fonte"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📈 Área de Composição por Categoria")
        
        dados_categoria = get_dados_por_categoria()
        df_categoria = pd.DataFrame([dict(d) for d in dados_categoria])
        
        fig_area = go.Figure()
        
        for categoria in df_categoria['categoria'].unique():
            df_cat = df_categoria[df_categoria['categoria'] == categoria]
            fig_area.add_trace(go.Scatter(
                x=df_cat['categoria'],
                y=df_cat['total'],
                mode='lines+markers',
                name=categoria,
                fill='tozeroy'
            ))
        
        fig_area.update_layout(
            title="Composição por Categoria",
            yaxis_title="Valor (R$)",
            xaxis_title="Categoria",
            showlegend=True
        )
        
        st.plotly_chart(fig_area, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("📅 Últimos 10 Registros")
    
    dados_recentes = dados[:10]
    df_recentes = pd.DataFrame([dict(d) for d in dados_recentes])
    
    st.dataframe(df_recentes, width='stretch')