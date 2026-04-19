import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

import streamlit as st
import pandas as pd
from models.database import get_all_dados, get_dados_filtrados

def listar_dados_page():
    st.title("📋 Listar Dados")
    st.markdown("---")
    
    dados = get_all_dados()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        filtro_data = st.text_input("Filtrar por Data", placeholder="DD/MM/YYYY ou YYYY-MM-DD")
    
    with col2:
        filtro_nome = st.text_input("Filtrar por Fonte", placeholder="Nome da fonte")
    
    with col3:
        filtro_categoria = st.text_input("Filtrar por Categoria", placeholder="Nome da categoria")
    
    st.markdown("---")
    
    dados_filtrados = get_dados_filtrados(filtro_data, filtro_nome, filtro_categoria)
    
    if dados_filtrados:
        df = pd.DataFrame([dict(d) for d in dados_filtrados])
        
        total = df['valor'].sum()
        cdi_medio = df['cdi'].mean() * 100
        
        col1, col2 = st.columns(2)
        
        col1.metric("Registros Encontrados", len(dados_filtrados))
        col2.metric("Valor Total", f"R$ {total:,.2f}")
        
        st.markdown("---")
        
        st.subheader("Resultado da Busca")
        st.dataframe(df, use_container_width=True)
        
        st.markdown("---")
        
        st.subheader("Resumo Estatístico")
        
        col1, col2, col3 = st.columns(3)
        
        col1.metric("Média por Fonte", f"R$ {df.groupby('fonte')['valor'].mean().mean():,.2f}")
        col2.metric("CDI Médio", f"{cdi_medio:.2f}%")
        col3.metric("Maior Valor", f"R$ {df['valor'].max():,.2f}")
    else:
        st.warning("Nenhum dado encontrado com os filtros informados.")