# Padrões de Código

Este documento define os padrões de código que devem ser seguidos durante o desenvolvimento do projeto Ethos Financeiro.

## 📋 Padrões Gerais

### 1. Nomenclatura

**Arquivos:**
- Usar `snake_case`
- Prefixos significativos para módulos
- Exemplo: `processamento.py`, `database.py`, `streamlit_app.py`

**Variáveis:**
- Usar `snake_case` em Python
- Nomes descritivos e self-explanatory
- Exemplo: `valor_inicial`, `dados_filtrados`, `processo_streamlit`

**Funções:**
- Usar `snake_case`
- Verbos no início do nome
- Exemplo: `get_dados()`, `processar_csv()`, `iniciar_streamlit()`

**Classes:**
- Usar `PascalCase` ou `Capitalize`
- Nomes descritivos
- Exemplo: `StreamlitWrapper`, `Configuracao`

### 2. Estrutura de Módulos

```python
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import streamlit as st
import pandas as pd
from controllers.processamento import funcao_processamento
from models.database import funcao_database

# Imports de terceiros na ordem:
# 1. Bibliotecas padrão
# 2. Bibliotecas de terceiros
# 3. Imports do projeto

# Funções e classes
def minha_funcao():
    pass

class MinhaClasse:
    pass

# Execução principal
if __name__ == "__main__":
    minha_funcao()
```

### 3. Indentação e Formatação

- **Indentação:** 4 espaços (PEP 8)
- **Limite de linhas:** 79 caracteres (recomendado para compatibilidade)
- **Imports:** Sempre em separados por bloco de 1 linha

```python
# Import padrão
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import streamlit as st

# Função correta
def minha_funcao():
    resultado = processamento()
    return resultado

# Função incorreta
def minha_funcao():
    resultado=processamento()
    return resultado  # Sem espaço
```

## 🎯 Padrões Específicos

### 1. Padrões de Interface Streamlit

**Configuração da Página:**
```python
st.set_page_config(
    page_title="Título",
    page_icon="Emoji",
    layout="wide"
)
```

**Seções com Divisores:**
```python
st.title("Título")
st.markdown("---")

# Conteúdo aqui

st.markdown("---")
```

**Grupos de KPIs:**
```python
col1, col2, col3 = st.columns(3)

col1.metric("KPI 1", valor)
col2.metric("KPI 2", valor)
col3.metric("KPI 3", valor)

st.markdown("---")
```

### 2. Padrões de Banco de Dados

**Conexões:**
```python
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
```

**Querys:**
```python
cursor.execute('''
    SELECT * FROM tabela WHERE condicao
''')
```

**Commit/Close:**
```python
conn.commit()
conn.close()
```

### 3. Padrões de Controladores

**Funções de Serviço:**
```python
def processar_csv(arquivo_csv):
    try:
        # Processamento aqui
        return {'sucesso': True, 'mensagem': 'OK'}
    except Exception as e:
        return {'sucesso': False, 'mensagem': str(e)}
```

**Importações:**
```python
from models.database import get_all_dados
```

### 4. Padrões de Webview

**Inicialização:**
```python
streamlit_wrapper = StreamlitWrapper()
streamlit_wrapper.start_streamlit()
```

**Encerramento:**
```python
def on_closing(window):
    streamlit_wrapper.stop()
    return False
```

## 🚫 Anti-Padrões

### 1. Imports Incorrectos

**INCORRETO:**
```python
from .processamento import processar_csv
```

**CORRETO:**
```python
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from controllers.processamento import processar_csv
```

### 2. Códigos Duplicados

**INCORRETO:**
```python
# Código duplicado em múltiplas páginas
def carregar_dados():
    dados = get_all_dados()
    return dados
```

**CORRETO:**
```python
# Usar função única no models
def carregar_dados():
    dados = get_all_dados()
    return dados
```

### 3. Funções Muito Longas

**INCORRETO:**
```python
def pagina_longa():
    # 100 linhas de código
    pass
```

**CORRETO:**
```python
def pagina_longa():
    setup()
    processamento()
    exibicao()

def setup():
    pass

def processamento():
    pass

def exibicao():
    pass
```

## 📊 Métricas de Código

- **Complexidade:** Mantemba abaixo de 10
- **Linhas por função:** Abaixo de 50 (ideal: 20-30)
- **Linhas por arquivo:** Abaixo de 200 (ideal: 100-150)
- **Funções por arquivo:** Abaixo de 10 (ideal: 5-8)

## 🔍 Verificações Automáticas

### PyLint Checks

```bash
# Verificar padrões
./venv/bin/pylint app/views/streamlit_app.py

# Verificar todos os arquivos
./venv/bin/pylint app/**/*.py
```

### Mypy Checks

```bash
# Verificar tipos
./venv/bin/mypy app/views/streamlit_app.py
```

## 📝 Documentação

**Padrão de Docstring:**
```python
def minha_funcao(parametro1, parametro2):
    """
    Descrição curta da função.

    Args:
        parametro1: Descrição do parâmetro
        parametro2: Descrição do parâmetro

    Returns:
        Tipo do retorno
    """
    pass
```

**Comentários:**
```python
# Comentário explicativo
# Noções importantes

def funcao():
    # Isso é uma linha importante
    pass
```

## 🎨 Padrões de Interface

### Cores e Estilos

```python
# Cores recomendadas para gráficos
azul_escuro = '#2c3e50'
azul_claro = '#3498db'
verde = '#27ae60'
vermelho = '#e74c3c'
```

### Espaçamento

```python
# Espaçamento entre elementos
st.markdown("---")  # Linha divisória
col1, col2, col3 = st.columns(3)  # 1 espaço
st.title("Título")  # 1 espaço
```

## 📚 Recursos de Referência

- [PEP 8 - Guia de Estilo Python](https://www.python.org/dev/peps/pep-0008/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [PyQt6 Documentation](https://www.riverbankcomputing.com/software/pyqt/)

---

**Versão**: 1.0.0
**Atualizado**: 2026-04-18
**Aplicável**: Todos os desenvolvedores