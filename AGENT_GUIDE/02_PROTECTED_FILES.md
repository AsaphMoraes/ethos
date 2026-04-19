# Arquivos Protegidos

Este documento lista todos os arquivos que NÃO devem ser modificados diretamente durante o desenvolvimento normal.

## 🚫 Arquivos do Sistema Git

Estes arquivos são gerenciados pelo Git e devem permanecer inalterados:

### .git/*
- `.git/config` - Configurações do repositório
- `.git/HEAD` - Ponteiro para branch atual
- `.git/index` - Área de staging
- `.git/refs/` - Referências de commits
- `.git/hooks/` - Hooks do Git
- `.git/FETCH_HEAD` - Ponteiro do último fetch

### .kilo/*
- `.kilo/package.json`
- `.kilo/bun.lock`
- `.kilo/agent-manager.json`
- `.kilo/node_modules/` (diretório)

## 📦 Dependências

### requirements.txt
- **Status:** PROTEGIDO
- **Motivo:** Contém todas as dependências do projeto
- **Ação:** SEMPRE usar `./venv/bin/pip install -r requirements.txt`
- **Como adicionar dependência:** `./venv/bin/pip install pacote` (instala no venv)

### venv/
- **Status:** PROTEGIDO
- **Motivo:** Ambiente virtual do projeto
- **Ação:** NÃO apagar ou modificar
- **Como criar novo venv:** `python3 -m venv venv` (de novo no diretório do projeto)

## 🗄️ Banco de Dados

### database/dados.db
- **Status:** PROTEGIDO
- **Motivo:** Banco de dados SQLite
- **Ação:** Usar funções de database.py
- **Como limpar:** Chamar `clear_dados()` na interface ou executar `rm database/dados.db`
- **Nota:** O arquivo é criado automaticamente na primeira execução

## 📝 Configurações de Ambiente

### app/data/formatos/csv_formats.json
- **Status:** PROTEGIDO
- **Motivo:** Configuração de formatos de CSV
- **Ação:** Adicionar novos formatos seguindo o padrão existente
- **Como adicionar:** Editar e adicionar novos formatos à seção `csv_formats`
- **Nota:** Valida automaticamente com os arquivos CSV

### venv/bin/python
- **Status:** PROTEGIDO
- **Motivo:** Interpreter Python do ambiente virtual
- **Ação:** SEMPRE usar `./venv/bin/python`

## 🏗️ Estrutura de Arquivos do Projeto

### app/__init__.py
- **Status:** PROTEGIDO
- **Motivo:** Pacote Python
- **Ação:** Nunca alterar conteúdo

### app/views/pages/__init__.py
- **Status:** PROTEGIDO
- **Motivo:** Agrupamento de páginas
- **Ação:** Nunca alterar conteúdo

### app/data/formatos/__init__.py
- **Status:** PROTEGIDO
- **Motivo:** Pacote Python
- **Ação:** Nunca alterar conteúdo

## 🛠️ Scripts de Construção

### start.sh
- **Status:** PROTEGIDO
- **Motivo:** Script de inicialização automatizada
- **Ação:** Nunca alterar conteúdo
- **Como usar:** `./start.sh`

### run.sh
- **Status:** PROTEGIDO
- **Motivo:** Script de execução com filtro de warnings
- **Ação:** Nunca alterar conteúdo
- **Como usar:** `./run.sh`

### ethos.desktop
- **Status:** PROTEGIDO
- **Motivo:** Atalho desktop Linux
- **Ação:** Nunca alterar conteúdo

## 📄 Documentação Principal

### README.md
- **Status:** PROTEGIDO
- **Motivo:** Documentação principal do projeto
- **Ação:** Atualizar para refletir mudanças importantes

### README_INSTRUCTIONS.txt
- **Status:** PROTEGIDO
- **Motivo:** Instruções do projeto
- **Ação:** Atualizar se houver mudanças importantes

### STRUCTURE.md
- **Status:** PROTEGIDO
- **Motivo:** Documentação técnica da estrutura
- **Ação:** Atualizar se houver mudanças na estrutura

## 📚 Documentação Técnica (AGENT_GUIDE)

### AGENT_GUIDE/*.md
- **Status:** PARCIALMENTE PROTEGIDO
- **Motivo:** Guias de desenvolvimento
- **Ação:**
  - **02_PROTECTED_FILES.md** - PROTEGIDO (nunca alterar)
  - **03_PROBLEMS_SOLUTIONS.md** - EDITÁVEL (adicionar novos problemas)
  - **04_DEVELOPMENT_GUIDE.md** - EDITÁVEL (atualizar quando necessário)
  - **06_ISSUES_DB.md** - EDITÁVEL (mudar status de problemas)

## 🔒 Regras de Proteção

### 1. Nunca Modifique Sem Justificativa

- Cada arquivo protegido tem um motivo para ser assim
- Se precisar modificar, documente em `06_ISSUES_DB.md`

### 2. Sempre Backup

- Para arquivos não protegidos, faça backup antes de modificar
- Git faz backup automático

### 3. Verifique Antes de Modificar

```bash
# Verificar arquivos modificados
git status

# Verificar diff
git diff

# Verificar logs
git log
```

## 🚫 O Que NÃO Fazer

### ❌ NÃO apagar arquivos do venv
```bash
# INCORRETO
rm -rf venv
```

### ❌ NÃO editar diretamente csv_formats.json sem entender
```bash
# INCORRETO
vim app/data/formatos/csv_formats.json
```

### ❌ NÃO apagar database/dados.db (apenas use funções de limpeza)
```bash
# INCORRETO
rm database/dados.db
```

## ✅ O Que Fazer

### ✅ Para instalar novas dependências
```bash
./venv/bin/pip install pacote_novo
```

### ✅ Para mudar configurações de Streamlit
- Edite `app/views/streamlit_app.py`

### ✅ Para mudar formatos de CSV
- Edite `app/data/formatos/csv_formats.json`

### ✅ Para adicionar nova página
- Crie `app/views/pages/nova_pagina.py`
- Adicione entrada em `app/views/pages/sidebar.py`

### ✅ Para limpar banco de dados
- Use a interface ou execute:
```bash
./venv/bin/python -c "from app.models.database import clear_dados; clear_dados()"
```

## 📋 Checklist de Proteção

Antes de começar desenvolvimento, verifique:

- [ ] Arquivos do Git não foram modificados
- [ ] Dependências não foram adicionadas manualmente
- [ ] venv não foi apagado
- [ ] Database não foi modificado manualmente
- [ ] Scripts de construção não foram alterados

## 🔍 Como Verificar

### Verificar arquivos modificados
```bash
cd /home/AsaphM/Documentos/github/ethos
git status
```

### Verificar arquivos não protegidos
```bash
git diff
```

### Verificar logs recentes
```bash
git log -5
```

## 📞 Quando Dúvidas

Se tiver dúvida sobre algum arquivo:

1. Consulte este documento
2. Verifique se é um arquivo protegido
3. Se for protegido, consulte `06_ISSUES_DB.md`
4. Se ainda tiver dúvida, pergunte

---

**Versão**: 1.0.0
**Atualizado**: 2026-04-18
**Regra de Ouro**: SEMPRE verifique antes de modificar