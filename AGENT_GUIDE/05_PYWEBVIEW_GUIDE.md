# 05_PYWEBVIEW_GUIDE.md

# Guia de PyWebview - Integração e Configuração

## 📚 Visão Geral

Este documento integra a documentação do WEBVIEW_README.md com informações técnicas adicionais sobre PyWebview e configurações.

## 🚀 Executando o Aplicativo

### Método 1: Script start.sh (Linux/Mac)

```bash
./start.sh
```

**Processo:**
1. Verifica venv
2. Verifica dependências (pywebview, PyQt6)
3. Inicia aplicativo com webview

### Método 2: Python direto

```bash
python main.py
```

### Método 3: No ambiente virtual

```bash
source venv/bin/activate
python main.py
```

## ⚙️ Como Funciona

### Estrutura de Execução

```
main.py (webview wrapper)
    ↓
start_streamlit() - Inicia Streamlit em subprocesso
    ↓
webview.create_window() - Cria janela nativa
    ↓
Streamlit roda DENTRO do webview (no porto 8501)
    ↓
Interface exibida nativamente
```

### Processo de Inicialização

1. **Criação do subprocesso**: Streamlit inicia em subprocesso separado
2. **Modo headless**: `--server.headless false` (Streamlit se comunica com webview)
3. **CORS e XSRF**: Desativados para permitir comunicação interna
4. **Webview creation**: Cria janela apontando para localhost:8501
5. **Loop de exibição**: Webview hospeda o Streamlit em iframe
6. **Encerramento**: Ao fechar janela, subprocesso termina

## 🛠️ Configurações do Webview

O `main.py` inclui as seguintes configurações:

- **Backend**: Webview (Qt ou Edge Chromium)
- **Porto**: 8501 (padrão do Streamlit)
- **Modo headless**: false (Streamlit comunicando com webview)
- **CORS**: false (comunicação interna)
- **XSRF**: false (comunicação interna)
- **Debug**: true (modo de depuração)
- **Tamanho**: 1200x800
- **Resizable**: true
- **Fullscreen**: false

### Configurações do Streamlit

```python
streamlit_cmd = [
    streamlit_path,
    "run",
    str(Path(__file__).parent / "app" / "views" / "streamlit_app.py"),
    "--server.port", str(self.port),
    "--server.headless", "false",  # ← IMPORTANTE
    "--server.enableCORS", "false",  # ← IMPORTANTE
    "--server.enableXsrfProtection", "false"  # ← IMPORTANTE
]
```

### Configurações do Webview

```python
window = webview.create_window(
    'Ethos Financeiro',
    f'http://localhost:{streamlit_wrapper.port}',
    width=1200,
    height=800,
    resizable=True,
    fullscreen=False,
    easy_drag=False
)
```

## 🔧 Backends do Webview

O pywebview suporta diferentes backends:

### PyQt6/PySide6 (Linux/Mac/Windows)

**Vantagens:**
- Mais fácil de instalar
- Melhor performance no Linux
- Suporta todos os recursos do Streamlit
- Menos dependências do sistema

**Instalação:**
```bash
./venv/bin/pip install PyQt6
```

**Requisitos:**
- PyQt6 6.11.0 (instalado)
- Qt6 6.11.0
- Sip 13.11.1

### Edge Chromium (Windows/Mac/Linux)

**Vantagens:**
- Boa performance
- Menos dependências do sistema
- Funciona na maioria dos sistemas

**Instalação:**
```bash
./venv/bin/pip install edge-python
```

**Nota:**
- Windows: Melhor opção
- Linux/Mac: Funciona bem
- Menos problemas de dependências do sistema

### CEF (Chromium Embedded Framework)

**Vantagens:**
- Controlável
- Customizável
- Boa performance

**Instalação:**
```bash
./venv/bin/pip install cefpython3
```

### OS Default

O pywebview seleciona automaticamente o melhor backend disponível.

## 📋 Como Usar

### Iniciar o Aplicativo

```bash
python main.py
```

### Aguarda Inicialização

- Aguarde 3 segundos para o Streamlit iniciar
- Uma janela será aberta automaticamente
- A interface estará totalmente funcional

### Navegação

1. **Dashboard**: KPIs principais, Radar de Eficiência, Área de Composição, Últimos Registros
2. **Simulação**: Valor inicial, Valor mensal, Número de meses, Gráfico de evolução
3. **Upload CSV**: 4 formatos suportados, Processamento, Importação
4. **Listar Dados**: Filtros, Tabela, Métricas resumo

### Encerramento

1. Clique no botão de fechar na janela
2. O processo do Streamlit é encerrado automaticamente
3. Graceful shutdown (timeout de 5 segundos)
4. Sem processos residuais

## 🎯 Backends Compatíveis

### Linux

**PyQt6** (Recomendado):
```bash
pip install PyQt6
```

**Edge Chromium**:
```bash
pip install edge-python
```

**KDE** (automático):
```bash
# pywebview detecta automaticamente
```

### macOS

**PyQt6**:
```bash
pip install PyQt6
```

**Edge Chromium**:
```bash
pip install edge-python
```

**Safari** (automático):
```bash
# pywebview detecta automaticamente
```

### Windows

**Edge Chromium** (Recomendado):
```bash
pip install edge-python
```

**CEF**:
```bash
pip install cefpython3
```

**PyQt6**:
```bash
pip install PyQt6
```

## 🚀 Configurações Avançadas

### Forçar Backend

**PyQt6:**
```python
window = webview.create_window(
    ...,
    backend='qt'
)
```

**Edge:**
```python
window = webview.create_window(
    ...,
    backend='edge'
)
```

**CEF:**
```python
window = webview.create_window(
    ...,
    backend='cef'
)
```

### Ajustar Tamanho da Janela

```python
window = webview.create_window(
    ...,
    width=1400,  # Ajustar largura
    height=900   # Ajustar altura
)
```

### Desabilitar Debug

```python
webview.start(debug=False)  # Modo de produção
```

### Mudar Porto

```python
self.port = 8502  # Em main.py - linha 14
```

## 🛠️ Solução de Problemas

### Streamlit não inicia

```bash
# Verificar porto
lsof -i :8501

# Tentar outra porta
self.port = 8502

# Verificar arquivo
ls app/views/streamlit_app.py
```

### Webview não abre

```bash
# Verificar backend
python -c "import webview; import PyQt6; print('OK')"

# Verificar URL
curl http://localhost:8501

# Reiniciar aplicativo
```

### Erro de import

```bash
# Verificar PYTHONPATH
export PYTHONPATH=/home/AsaphM/Documentos/github/ethos:$PYTHONPATH
python main.py
```

### Performance lenta

```bash
# Desativar debug
webview.start(debug=False)

# Usar Edge ou CEF
backend='edge'  # Ou 'cef'
```

## 📊 Comparativo de Soluções

| Solução | Dificuldade | Performance | Recomendado |
|---------|-------------|-------------|-------------|
| PyQt6 | Fácil | Ótima | ✅✅✅ Linux/Mac |
| Edge | Fácil | Ótima | ✅✅ Windows |
| CEF | Média | Boa | ✅ Desenvolvimento |
| OS Auto | Simples | Boa | ✅ Automático |

## 🔍 Monitoramento

### Verificar se Streamlit está rodando

```bash
lsof -i :8501
```

### Verificar processo webview

```bash
ps aux | grep webview
```

### Verificar subprocesso Streamlit

```python
streamlit_wrapper.process.poll()  # 0 = encerrado, None = rodando
```

## 🎯 Boas Práticas

### 1. Instale o backend correto

- Linux: PyQt6
- Windows: Edge
- Desenvolvimento: CEF ou PyQt6

### 2. Use o script start.sh

- Verifica dependências automaticamente
- Mensagens de erro claras
- Script de inicialização automatizado

### 3. Verifique inicialização

- Aguarde 3 segundos
- Verifique logs no terminal
- Verifique se janela abriu

### 4. Trate erros

- Script handle automaticamente
- Logs completos de inicialização
- Mensagens de status claras

## 📚 Referências

- [PyWebView Documentation](https://pywebview.flowrl.com/)
- [PyQt6 Documentation](https://www.riverbankcomputing.com/software/pyqt/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

**Versão**: 1.0.0
**Atualizado**: 2026-04-18
**Backend**: PyQt6 6.11.0
**Status**: Integrado do WEBVIEW_README.md