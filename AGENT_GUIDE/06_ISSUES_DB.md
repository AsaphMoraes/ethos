# Banco de Dados de Problemas

Este documento rastreia todos os problemas ativos e seu status.

## 📊 Status

- ✅ **Resolvido** - Problema foi solucionado
- ⚠️ **Em Progresso** - Problema sendo solucionado
- ❌ **Não Resolvido** - Problema ainda não solucionado
- 🔒 **Bloqueio** - Problema está bloqueando desenvolvimento

## 📋 Problemas Ativos

### 1. Fontconfig Error - Resolvido

**Data:** 2026-04-18
**Status:** ✅ Resolvido

**Descrição:**
Fontconfig error: Cannot load default config file: (null)

**Causa:**
Qt/PyQt6 não encontrou arquivo de configuração do Fontconfig

**Solução:**
- Script `run.sh` que filtra a saída
- Instalação de fontconfig (solução definitiva)

**Arquivo:** `AGENT_GUIDE/03_PROBLEMS_SOLUTIONS.md`

**Prevenção:**
- Use `./run.sh` para executar
- Ou instale fontconfig
- Nunca confie em `warnings.filterwarnings()` para Qt

**Ação:** ✅ Nenhuma ação necessária

---

### 2. GTK Backend Error - Resolvido

**Data:** 2026-04-18
**Status:** ✅ Resolvido

**Descrição:**
ModuleNotFoundError: No module named 'gi'

**Causa:**
pywebview tentou usar GTK sem PyQt6 instalado

**Solução:**
- Instalar PyQt6: `./venv/bin/pip install PyQt6`
- Ou edge-python

**Arquivo:** `AGENT_GUIDE/03_PROBLEMS_SOLUTIONS.md`

**Prevenção:**
- Sempre instalar PyQt6 ou edge-python
- Usar script `start.sh` que verifica dependências

**Ação:** ✅ Nenhuma ação necessária

---

### 3. Importação e Thread Errors - Resolvido

**Data:** 2026-04-18
**Status:** ✅ Resolvido

**Descrição:**
ModuleNotFoundError: No module named 'models'
Streamlit não inicia corretamente no aplicativo principal

**Causa:**
1. sys.path não incluía diretório raiz do projeto
2. Thread read_output() nunca era iniciada
3. Webview abria antes do Streamlit inicializar
4. Callback on_closing mal configurado

**Solução:**
1. Correção de sys.path em streamlit_app.py
2. Inicialização da thread de leitura de output
3. Delay de 3 segundos antes do webview
4. Correção do callback com lambda

**Arquivo:** `AGENT_GUIDE/03_PROBLEMS_SOLUTIONS.md`

**Prevenção:**
- Sempre verificar sys.path em subprocessos
- Iniciar threads de leitura de output
- Adicionar delays para dependências
- Testar callbacks de eventos

**Ação:** ✅ Nenhuma ação necessária

---

### 4. Performance de Gráficos com Muitos Dados - Pendente

**Data:** 2026-04-18
**Status:** ⚠️ Em Progresso

**Descrição:**
Gráficos podem ser lentos com muitos dados

**Causa:**
- Renderização de todos os dados de uma vez
- Sem paginação ou lazy loading

**Solução:**
- Implementar paginação
- Adicionar lazy loading
- Usar chunking

**Prioridade:** Alta

**Arquivo:** [Criar issue de feature]

**Prevenção:**
- Sempre considerar performance com muitos dados
- Implementar paginação quando necessário

**Ação:**
- [ ] Definir tamanho de paginação (ex: 100 registros)
- [ ] Adicionar paginação nas páginas
- [ ] Testar performance

---

### 5. Compartilhamento de Dados - Pendente

**Data:** 2026-04-18
**Status:** ⚠️ Em Progresso

**Descrição:**
Cada página lê do banco separadamente

**Causa:**
- Sem state management centralizado
- Cada função acessa o banco diretamente

**Solução:**
- Usar streamlit session state
- Criar cache centralizado
- Implementar pattern Singleton para dados

**Prioridade:** Média

**Arquivo:** [Criar issue de feature]

**Prevenção:**
- Usar streamlit session state para dados compartilhados
- Criar cache com @st.cache_data

**Ação:**
- [ ] Implementar session state para dados
- [ ] Mover dados para cache centralizado
- [ ] Testar compartilhamento entre páginas

---

### 6. Testes Automatizados - Pendente

**Data:** 2026-04-18
**Status:** ⚠️ Em Progresso

**Descrição:**
Não há testes automatizados

**Causa:**
- Desenvolvimento sem TDD (Test Driven Development)
- Falta de importação de pytest

**Solução:**
- Instalar pytest
- Criar testes para páginas
- Criar testes para banco de dados
- Criar testes para controllers

**Prioridade:** Média

**Arquivo:** [Criar issue de feature]

**Prevenção:**
- Sempre escrever testes
- Usar TDD
- Testar antes de commit

**Ação:**
- [ ] Instalar pytest
- [ ] Criar testes básicos
- [ ] Criar testes de banco de dados
- [ ] Criar testes de controllers
- [ ] Criar testes de páginas

---

### 7. Deploy Automatizado - Pendente

**Data:** 2026-04-18
**Status:** ❌ Não Resolvido

**Descrição:**
Não há script de deploy automatizado

**Causa:**
- Desenvolvimento local
- Falta de CI/CD

**Solução:**
- Criar script de deploy
- Criar arquivo de configuração de deployment
- Implementar CI/CD com GitHub Actions

**Prioridade:** Baixa

**Arquivo:** [Criar issue de feature]

**Prevenção:**
- Planejar deploy desde o início
- Usar contêineres para deployment
- Implementar CI/CD

**Ação:**
- [ ] Criar Dockerfile
- [ ] Criar script de deploy
- [ ] Implementar GitHub Actions

---

## 📊 Estatísticas

### Por Status

| Status | Quantidade | % |
|--------|-----------|---|
| ✅ Resolvido | 3 | 43% |
| ⚠️ Em Progresso | 3 | 43% |
| ❌ Não Resolvido | 1 | 14% |

### Por Prioridade

| Prioridade | Quantidade | % |
|------------|-----------|---|
| Alta | 1 | 20% |
| Média | 2 | 40% |
| Baixa | 1 | 20% |

### Por Data

| Data | Problemas | Resolvidos |
|------|-----------|------------|
| 2026-04-18 | 8 | 3 |

## 🔍 Como Consultar

```bash
cd AGENT_GUIDE
grep "Status:" 06_ISSUES_DB.md
grep "Status: ⚠️" 06_ISSUES_DB.md
grep "Status: ❌" 06_ISSUES_DB.md
```

## 📝 Como Adicionar Novo Problema

```markdown
### X. Nome do Problema - Status

**Data:** 2026-04-18
**Status:** ⚠️ Em Progresso

**Descrição:**
Descrição do problema

**Causa:**
Causa do problema

**Solução:**
Solução proposta

**Prioridade:** [Alta/Média/Baixa]

**Arquivo:** [Arquivo afetado]

**Prevenção:**
Como evitar no futuro

**Ação:**
- [ ] Ação 1
- [ ] Ação 2
```

## 🎯 Próximos Passos

### Prioridade Alta
1. [ ] Compartilhamento de dados
2. [ ] Performance de gráficos
3. [ ] Testes automatizados

### Prioridade Média
4. [ ] Deploy automatizado

### Prioridade Baixa
5. [ ] Outras melhorias

## 🔄 Workflow de Problemas

1. **Identificar problema**
   - Documente em `06_ISSUES_DB.md`
   - Defina status inicial

2. **Implementar solução**
   - Siga `04_DEVELOPMENT_GUIDE.md`
   - Teste a solução

3. **Atualizar status**
   - Mude status para "Resolvido"
   - Remova da lista de problemas ativos

4. **Documentar**
   - Adicione a `03_PROBLEMS_SOLUTIONS.md`
   - Explique causa e solução

---

**Versão**: 1.0.0
**Atualizado**: 2026-04-18
**Total de Problemas**: 8
**Ativos**: 6
**Resolvidos**: 3