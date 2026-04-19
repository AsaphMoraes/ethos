import streamlit as st
from pathlib import Path
import sys
import os

# Adicionar caminhos ao sys.path - caminho absoluto para o diretório raiz do projeto
project_root = Path(__file__).parent.parent.parent if '__file__' in globals() else Path.cwd()
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / 'app'))

from models.database import create_tables
from utils.styles import apply_styles
from pages.dashboard import dashboard_page
from pages.simulacao import simulacao_page
from pages.upload import upload_page
from pages.listar_dados import listar_dados_page

st.set_page_config(
    page_title="App Financeiro",
    page_icon="💰",
    layout='wide'
)

apply_styles()
create_tables()

pg = st.navigation([
    st.Page(dashboard_page,title="Dashboard",icon="🏠"),
    st.Page(simulacao_page,title="Simulação",icon="📊"),
    st.Page(upload_page,title="Upload",icon="📁"),
    st.Page(listar_dados_page,title="Listar Dados",icon="📋")
], position='sidebar')

pg.run()