#!/bin/bash

# Script de inicialização do Ethos Financeiro

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "================================"
echo "Iniciando Ethos Financeiro..."
echo "================================"
echo ""

# Verifica se o venv existe
if [ ! -d "venv" ]; then
    echo "Erro: Ambiente virtual não encontrado!"
    echo "Por favor, execute: python3 -m venv venv"
    exit 1
fi

# Verifica se o virtualenv está ativado
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Ativando ambiente virtual..."
    source venv/bin/activate
fi

# Verifica se pywebview está instalado
if ! python -c "import webview" 2>/dev/null; then
    echo "Instalando pywebview..."
    pip install pywebview
fi

# Verifica se streamlit está instalado
if ! python -c "import streamlit" 2>/dev/null; then
    echo "Instalando streamlit..."
    pip install -r requirements.txt
fi

echo ""
echo "Iniciando aplicativo..."
echo "Pressione Ctrl+C para encerrar"
echo ""

# Inicia o webview
python main.py

echo ""
echo "Aplicativo encerrado."