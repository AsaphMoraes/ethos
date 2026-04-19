# Problemas e Soluções

Este documento documenta todos os problemas encontrados durante o desenvolvimento e suas soluções correspondentes.

## 📋 Documentação de Problemas

### 1. Fontconfig Error

**Data:** 2026-04-18
**Status:** ✅ Resolvido

**Problema:**
```
Fontconfig error: Cannot load default config file: (null)
```

**Causa:**
- Qt/PyQt6 não encontrou arquivo de configuração do Fontconfig
- Qt ignora Python warnings (`warnings.filterwarnings()`)
- Qt usa seu próprio sistema de logging
- biblioteca Qt não intercepta warnings do Python

**Solução:**
- Criar script `run.sh` que filtra a saída:
```bash
./venv/bin/python main.py 2>&1 | grep -v "Fontconfig error"
```

- Ou instalar fontconfig (solução definitiva):
```bash
sudo apt-get install -y fontconfig libfontconfig1 libfreetype6 fonts-dejavu-core
```

**Arquivo Relacionado:**
- `main.py` (linha 7: warnings.filterwarnings)
- `run.sh` (script de execução)
- `SOLUTION_GTK_ERROR.md`
- `FONTCONFIG_ERROR.md`

**Prevenção:**
- Nunca use `warnings.filterwarnings()` para Qt/PyQt6
- Use `2>&1 | grep -v` ou instalar fontconfig
- Documente soluções no AGENT_GUIDE

---

### 2. GTK Backend Error

**Data:** 2026-04-18
**Status:** ✅ Resolvido

**Problema:**
```
ModuleNotFoundError: No module named 'gi'
Erro ao iniciar webview: You must have either QT or GTK with Python extensions installed
```

**Causa:**
- pywebview tentou usar GTK como backend padrão
- PyQt6 não estava instalado
- gi (PyGObject) não estava instalado

**Solução:**
- Instalar PyQt6 (recomendado):
```bash
./venv/bin/pip install PyQt6
```

- Ou instalar edge-python:
```bash
./venv/bin/pip install edge-python
```

**Arquivo Relacionado:**
- `main.py` (inicialização do webview)
- `requirements.txt` (dependências)
- `ERROR_ANALYSIS.md`
- `SOLUTION_GTK_ERROR.md`

**Prevenção:**
- Sempre instalar PyQt6 ou edge-python
- Verificar `pip show PyQt6` antes de iniciar
- Usar script `start.sh` que verifica dependências

---

### 3. Streamlit dentro Webview

**Data:** 2026-04-18
**Status:** ✅ Implementado

**Problema:**
- Streamlit rodando separado ou em modo headless não comunicava com webview
- Interface não aparecia corretamente

**Causa:**
- Streamlit precisava se comunicar com webview
- Modo headless true impedia comunicação
- CORS/XSRF bloqueavam comunicação

**Solução:**
- Configurar Streamlit com `--server.headless false`
- Desativar CORS: `--server.enableCORS false`
- Desativar XSRF: `--server.enableXsrfProtection false`
- Webview carrega Streamlit como iframe

**Código:**
```python
streamlit_cmd = [
    streamlit_path,
    "run",
    str(Path(__file__).parent / "app" / "views" / "streamlit_app.py"),
    "--server.port", str(self.port),
    "--server.headless", "false",  # ← IMPORTANTE
    "--server.enableCORS", "false",
    "--server.enableXsrfProtection", "false"
]
```

**Arquivo Relacionado:**
- `main.py` (linha 16-26)
- `WEBVIEW_GUIDE.md`
- `WEBVIEW_README.md`

**Prevenção:**
- Sempre usar `--server.headless false`
- Desativar CORS e XSRF para comunicação interna
- Testar comunicação webview-streamlit

---

### 4. Código Modular vs Monolítico

**Data:** 2026-04-18
**Status:** ✅ Resolvido

**Problema:**
- `streamlit_app.py` tinha 332 linhas
- Dificultava leitura e manutenção
- Dificultava testes

**Causa:**
- Todas as páginas em um arquivo
- Funções grandes e monolíticas
- Fácil conflito de código

**Solução:**
- Separar em arquivos por página
- Criar `pages/dashboard.py`
- Criar `pages/simulacao.py`
- Criar `pages/upload.py`
- Criar `pages/listar_dados.py`
- Criar `pages/sidebar.py`
- Criar `utils/styles.py`

**Resultado:**
- streamlit_app.py: 332 → 25 linhas (-92%)
- Total de arquivos: 4 páginas + utilities
- Maior organização e manutenibilidade

**Arquivo Relacionado:**
- `app/views/pages/` (diretório)
- `app/views/streamlit_app.py`
- `STRUCTURE.md`
- `01_CODING_PATTERNS.md`

**Prevenção:**
- Sempre manter arquivos com menos de 100-150 linhas
- Separar funcionalidades por arquivo
- Usar padrão MVC
- Documentar arquitetura

---

### 5. Docstrings Incompletas

**Data:** 2026-04-18
**Status:** ✅ Resolvido

**Problema:**
- Funções sem documentação
- Parâmetros não explicados
- Retornos não documentados

**Causa:**
- Desenvolvimento sem padronização de documentação

**Solução:**
- Implementar PEP 257 (Docstring Convention)
- Padão de documentação padrão:
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

**Arquivo Relacionado:**
- `01_CODING_PATTERNS.md` (seção Documentação)
- `app/views/pages/*.py` (todas as páginas)
- `app/models/database.py`
- `app/controllers/processamento.py`

**Prevenção:**
- Sempre documentar funções com docstrings
- Usar PEP 257 como padrão
- Verificar com linters
- Manter documentação atualizada

---

### 6. Erros de Importação e Thread no StreamlitWrapper

**Data:** 2026-04-18
**Status:** ✅ Resolvido

**Problema:**
```
ModuleNotFoundError: No module named 'models'
Streamlit inicia mas termina imediatamente no aplicativo principal
```

**Causa:**
1. **Erros de Importação**: `sys.path` não incluía o diretório raiz do projeto, causando `ModuleNotFoundError` para módulos `models`, `utils`, `pages`
2. **Thread não Iniciada**: A função `read_output()` no `StreamlitWrapper` nunca era iniciada como thread, impedindo a captura do output do Streamlit
3. **Timing Issues**: Webview abria imediatamente após `start_streamlit()`, sem dar tempo suficiente para o Streamlit inicializar
4. **Callback Mal Configurado**: O callback `on_closing` estava mal configurado, causando problemas no encerramento

**Solução:**
1. **Correção de Importação** em `app/views/streamlit_app.py`:
   ```python
   project_root = Path(__file__).parent.parent.parent if '__file__' in globals() else Path.cwd()
   sys.path.insert(0, str(project_root))
   sys.path.insert(0, str(project_root / 'app'))
   ```

2. **Inicialização da Thread** em `main.py`:
   ```python
   self.stdout_thread = threading.Thread(target=self.read_output)
   self.stdout_thread.daemon = True
   self.stdout_thread.start()
   ```

3. **Delay antes do Webview**:
   ```python
   import time
   time.sleep(3)
   ```

4. **Correção do Callback**:
   ```python
   window.events.closing += lambda: on_closing(window=window, streamlit_wrapper=streamlit_wrapper)
   ```

5. **Redirecionamento de stderr**:
   ```python
   stderr=subprocess.STDOUT
   ```

**Arquivo Relacionado:**
- `app/views/streamlit_app.py` (linhas 1-10)
- `main.py` (linhas 37-44, 104-106, 117)
- `ERROR_LOG.md`
- `diagnostic_report.md`

**Prevenção:**
- Sempre verificar `sys.path` ao executar scripts como subprocessos
- Iniciar threads de leitura de output quando usar subprocess.Popen
- Adicionar delays adequados antes de abrir interfaces dependentes
- Testar callbacks de eventos com lambdas quando necessário

---

## 🔄 Processo de Documentação

### Quando Documentar

1. **Ao encontrar novo problema:**
   - Documente em `03_PROBLEMS_SOLUTIONS.md`
   - Adicione data e status
   - Explique causa e solução

2. **Ao implementar solução:**
   - Atualize arquivo(s) afetado(s)
   - Adicione referência neste documento
   - Teste a solução

3. **Ao prevenir problema:**
   - Adicione prevenção na seção correspondente
   - Atualize guias de desenvolvimento
   - Crie checklist se necessário

### Formato de Documentação

```markdown
### Número Problema

**Data:** YYYY-MM-DD
**Status:** ✅ Resolvido / ⚠️ Em progresso / ❌ Não resolvido

**Problema:**
```
Mensagem do erro
```

**Causa:**
[Explique a causa]

**Solução:**
```bash
[Comandos de solução]
```

**Código:**
```python
[Código relevante]
```

**Arquivo Relacionado:**
- `arquivo.py` (linha X)

**Prevenção:**
[Explicação de como evitar no futuro]
```

## 📊 Estatísticas de Problemas

### Por Tipo

| Tipo | Quantidade | Resolvido |
|------|-----------|-----------|
| Erros de Dependência | 2 | 2 |
| Erros de Configuração | 1 | 1 |
| Problemas de Arquitetura | 1 | 1 |
| Problemas de Documentação | 1 | 1 |

### Por Data

| Data | Problemas | Resolvidos |
|------|-----------|------------|
| 2026-04-18 | 5 | 5 |

## 🔍 Como Consultar

```bash
cd /home/AsaphM/Documentos/github/ethos/AGENT_GUIDE
grep "Problema:" 03_PROBLEMS_SOLUTIONS.md
grep "Status: ✅ Resolvido" 03_PROBLEMS_SOLUTIONS.md
```

## 🚫 Problemas Não Resolvidos

Atualmente não há problemas não resolvidos.

## 📝 Próximos Problemas Esperados

1. **Performance de gráficos grandes:**
   - Observar problemas com muitos dados
   - Solução: Paginação, lazy loading

2. **Compartilhamento de dados entre páginas:**
   - Problema: Cada página lê do banco separadamente
   - Solução: Context manager ou session state

3. **Testes automatizados:**
   - Problema: Sem testes automatizados
   - Solução: Implementar pytest

---

**Versão**: 1.0.0
**Atualizado**: 2026-04-18
**Total Documentado**: 6 problemas