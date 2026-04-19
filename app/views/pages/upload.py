import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
import pandas as pd

import streamlit as st
from controllers.processamento import carregar_formatos, processar_csv
from models.database import get_all_dados, clear_dados

def upload_page():
    st.title("📁 Upload de CSV")
    st.markdown("---")
    
    formatos = carregar_formatos()
    
    st.subheader("Formatos Suportados")
    
    action = st.menu_button(
        "Selecione um formato",
        formatos.keys()
    )

    if action == "Selecione um formato":
        st.warning("Por favor, selecione um formato")
    if action:
        st.write(f"**Arquivo:** {formatos[action]['nome_arquivo']}")
        st.write(f"**Colunas:** {', '.join(formatos[action]['colunas'])}")
        st.write(f"**Separador:** {formatos[action]['separador']}")
        st.write(f"**Formato Data:** {formatos[action]['data_format']}")
            
    
    st.markdown("---")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        uploaded_file = st.file_uploader(
            "Selecione um arquivo CSV",
            type=['csv'],
            help="Suporta múltiplos formatos de CSV"
        )
        
        if uploaded_file:
            st.success(f"Arquivo carregado: {uploaded_file.name}")
            
            if st.button("Processar e Importar"):
                resultado = processar_csv(uploaded_file)
                
                if resultado['sucesso']:
                    st.success(resultado['mensagem'])
                else:
                    st.error(resultado['mensagem'])
    
    with col2:
        if st.button("Limpar Banco de Dados"):
            clear_dados()
            st.success("Banco de dados limpo com sucesso!")
    
    st.markdown("---")
    
    if uploaded_file and st.button("Ver dados importados"):
        dados = get_all_dados()
        if dados:
            st.dataframe(pd.DataFrame([dict(d) for d in dados]))
        else:
            st.warning("Nenhum dado importado ainda.")