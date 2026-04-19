# Guia de Desenvolvimento

Este documento é um guia completo para desenvolver, testar e manter o projeto Ethos Financeiro.

## 🚀 Fluxo de Trabalho

### 1. Preparação Inicial

```bash
# 1.1 Acessar diretório do projeto
cd /home/AsaphM/Documentos/github/ethos

# 1.2 Verificar ambiente virtual
which python  # Deve apontar para venv
ls venv/bin/python

# 1.3 Verificar dependências
./venv/bin/pip show pywebview
./venv/bin/pip show PyQt6

# 1.4 Verificar arquivos não modificados
git status  # Deve mostrar apenas novos arquivos
```

### 2. Iniciar Desenvolvimento

```bash
# 2.1 Acessar documentação técnica
cd AGENT_GUIDE

# 2.2 Ler guias necessários
cat 01_CODING_PATTERNS.md
cat 02_PROTECTED_FILES.md
cat 03_PROBLEMS_SOLUTIONS.md

# 2.3 Retornar ao diretório do projeto
cd ..
```

### 3. Desenvolvimento

#### 3.1 Adicionar Nova Página

**Passos:**

1. **Criar arquivo da página:**
```bash
vim app/views/pages/nova_pagina.py
```

**Conteúdo:**
```python
import sys
sys.path.append(str(__file__).parent.parent.parent)

import streamlit as st

def nova_pagina_page():
    st.title("Título da Página")
    st.markdown("---")
    # Conteúdo aqui
```

2. **Adicionar entrada no sidebar:**
```bash
vim app/views/pages/sidebar.py
```

**Conteúdo:**
```python
def get_pages():
    return [
        ("🏠 Dashboard", "house", dashboard_page),
        ("📊 Simulação", "bar-chart", simulacao_page),
        ("📁 Upload CSV", "cloud-upload", upload_page),
        ("📋 Listar Dados", "list", listar_dados_page),
        ("📄 Nova Página", "file-text", nova_pagina_page)  # ← ADICIONAR
    ]
```

3. **Adicionar importação:**
```bash
vim app/views/pages/__init__.py
```

**Conteúdo:**
```python
from .dashboard import dashboard_page
from .simulacao import simulacao_page
from .upload import upload_page
from .listar_dados import listar_dados_page
from .nova_pagina import nova_pagina_page  # ← ADICIONAR
```

4. **Testar:**
```bash
./venv/bin/python main.py
```

#### 3.2 Modificar Banco de Dados

**Passos:**

1. **Verificar estrutura atual:**
```bash
./venv/bin/python -c "
from app.models.database import create_tables, get_connection
conn = get_connection()
cursor = conn.cursor()
cursor.execute('PRAGMA table_info(dados)')
print(cursor.fetchall())
conn.close()
"
```

2. **Modificar estrutura:**
```python
# Em app/models/database.py
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data DATE NOT NULL,
            categoria TEXT NOT NULL,
            fonte TEXT NOT NULL,
            valor REAL NOT NULL,
            cdi REAL NOT NULL,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            nova_coluna TEXT  # ← NOVA COLUNA
        )
    ''')

    conn.commit()
    conn.close()
```

3. **Criar script de migração:**
```bash
vim app/migrations/add_nova_coluna.py
```

**Conteúdo:**
```python
from app.models.database import get_connection

def add_nova_coluna():
    conn = get_connection()
    cursor = conn.cursor()

    # Adicionar coluna se não existir
    cursor.execute("ALTER TABLE dados ADD COLUMN nova_coluna TEXT")

    conn.commit()
    conn.close()
    print("Coluna adicionada com sucesso")

if __name__ == "__main__":
    add_nova_coluna()
```

4. **Executar migração:**
```bash
./venv/bin/python app/migrations/add_nova_coluna.py
```

#### 3.3 Modificar Controller

**Passos:**

1. **Criar nova função:**
```python
# Em app/controllers/processamento.py

def nova_funcao():
    """Descrição da função"""
    pass
```

2. **Importar no streamlit_app.py:**
```python
from controllers.processamento import nova_funcao
```

3. **Usar na página:**
```python
resultado = nova_funcao()
```

#### 3.4 Modificar Interface

**Passos:**

1. **Adicionar novo componente:**
```python
# Em app/views/streamlit_app.py ou pages/

st.slider("Rótulo", 0, 100, 50)
```

2. **Testar layout:**
```bash
./venv/bin/python main.py
```

### 4. Testes

#### 4.1 Testar Imports

```bash
./venv/bin/python -c "
import sys
sys.path.append(str(Path.cwd()))

from app.views.pages import dashboard_page
from app.models.database import get_all_dados
from app.controllers.processamento import processar_csv

print('✅ Todos os imports funcionam')
"
```

#### 4.2 Testar Banco de Dados

```bash
./venv/bin/python -c "
from app.models.database import get_all_dados, create_tables

create_tables()
dados = get_all_dados()

print(f'✅ Banco de dados: {len(dados)} registros')
"
```

#### 4.3 Testar Webview

```bash
# Testar importações
./venv/bin/python -c "import webview; import PyQt6; print('✅ PyQt6 OK')"

# Testar execução
./venv/bin/python main.py
```

### 5. Finalizar Desenvolvimento

#### 5.1 Verificar Mudanças

```bash
# Verificar arquivos modificados
git status

# Verificar diff
git diff

# Verificar logs
git log -5
```

#### 5.2 Testar Funcionalidades

1. **Testar cada página:**
   - Dashboard
   - Simulação
   - Upload CSV
   - Listar Dados
   - Nova Página

2. **Testar filtros:**
   - Filtro por data
   - Filtro por fonte
   - Filtro por categoria

3. **Testar gráficos:**
   - Radar de Eficiência
   - Área de Composição

4. **Testar upload:**
   - Upload de CSV
   - Processamento
   - Importação

5. **Testar simulação:**
   - Valor inicial
   - Valor mensal
   - Número de meses
   - Cálculo do CDI

6. **Testar encerramento:**
   - Fechar webview
   - Verificar se Streamlit encerra
   - Verificar sem processos residuais

#### 5.3 Atualizar Documentação

```bash
# Atualizar problemas e soluções
vim AGENT_GUIDE/03_PROBLEMS_SOLUTIONS.md

# Atualizar guia de desenvolvimento
vim AGENT_GUIDE/04_DEVELOPMENT_GUIDE.md

# Atualizar README
vim README.md
```

#### 5.4 Limpar e Commit

```bash
# Limpar processos residuais
pkill -f streamlit

# Criar commit
git add .
git commit -m "Descrição da mudança"

# Verificar status final
git status
```

## 📋 Checklist de Desenvolvimento

### Antes de Iniciar

- [ ] Acessar AGENT_GUIDE
- [ ] Ler guias relevantes
- [ ] Verificar arquivos não modificados
- [ ] Verificar dependências instaladas

### Durante Desenvolvimento

- [ ] Seguir padrões de código
- [ ] Não modificar arquivos protegidos
- [ ] Documentar mudanças
- [ ] Testar regularmente
- [ ] Manter console limpo

### Ao Terminar

- [ ] Verificar todas as funcionalidades
- [ ] Testar encerramento
- [ ] Atualizar documentação
- [ ] Limpar processos residuais
- [ ] Verificar status git
- [ ] Fazer commit

## 🛠️ Ferramentas e Scripts Úteis

### Scripts Disponíveis

```bash
# Executar com filtro de warnings
./run.sh

# Executar automatizado
./start.sh

# Verificar dependências
./venv/bin/pip show pywebview
./venv/bin/pip show PyQt6

# Verificar arquivos git
git status
git diff

# Limpar processos
pkill -f streamlit
```

### Comandos Úteis

```bash
# Verificar estrutura de banco de dados
./venv/bin/python -c "from app.models.database import get_connection; import sqlite3; conn = get_connection(); print(conn.execute('SELECT * FROM dados LIMIT 1').fetchone())"

# Listar todos os arquivos do projeto
find app -name "*.py" | wc -l

# Contar linhas de código
find app -name "*.py" -exec wc -l {} + | tail -1

# Verificar versões
./venv/bin/python --version
./venv/bin/pip --version
```

## 📚 Referências Rápidas

### Comandos Comuns

```bash
# Executar app
./venv/bin/python main.py

# Verificar status
git status

# Criar commit
git add . && git commit -m "msg"

# Criar branch
git checkout -b feature/nova-funcionalidade

# Ir para diretório AGENT_GUIDE
cd AGENT_GUIDE
```

### Arquivos Importantes

```
app/views/streamlit_app.py         # Arquivo principal
app/views/pages/                   # Páginas do app
app/models/database.py             # Banco de dados
app/controllers/processamento.py   # Lógica de negócios
AGENT_GUIDE/                       # Documentação
```

## 🚫 Erros Comuns e Como Evitar

### 1. Import Errors

**Erro:**
```
ModuleNotFoundError: No module named 'gi'
```

**Solução:**
```bash
./venv/bin/pip install PyQt6
```

### 2. Fontconfig Warnings

**Erro:**
```
Fontconfig error: Cannot load default config file
```

**Solução:**
```bash
./run.sh
```

### 3. Imports Errados

**Erro:**
```
ModuleNotFoundError: No module named 'controllers'
```

**Solução:**
```python
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
```

## 📞 Quando Precisar de Ajuda

### 1. Verificar Documentação

```bash
cd AGENT_GUIDE
cat 01_CODING_PATTERNS.md
cat 02_PROTECTED_FILES.md
cat 03_PROBLEMS_SOLUTIONS.md
cat 04_DEVELOPMENT_GUIDE.md
```

### 2. Verificar Problemas Ativos

```bash
cd AGENT_GUIDE
cat 06_ISSUES_DB.md
```

### 3. Verificar Status do Projeto

```bash
cd AGENT_GUIDE
cat README.md
```

---

**Versão**: 1.0.0
**Atualizado**: 2026-04-18
**Utilize sempre este guia durante desenvolvimento**