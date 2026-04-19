# Registro de Erros e Soluções - Aplicativo Ethos

## Erros Críticos Resolvidos

### 1. **ModuleNotFoundError: No module named 'models'**
- **Arquivo**: `app/views/streamlit_app.py`
- **Descrição**: Erro de importação ao executar Streamlit
- **Causa**: `sys.path` não incluía o diretório raiz do projeto
- **Solução**: 
  ```python
  # Adicionar caminhos absolutos ao sys.path
  project_root = Path(__file__).parent.parent.parent if '__file__' in globals() else Path.cwd()
  sys.path.insert(0, str(project_root))
  sys.path.insert(0, str(project_root / 'app'))
  ```

### 2. **Streamlit não inicia no aplicativo principal**
- **Arquivo**: `main.py`
- **Descrição**: Processo Streamlit inicia mas termina imediatamente
- **Causas**:
  - Thread `read_output()` nunca era iniciada
  - Webview abria antes do Streamlit inicializar completamente
  - Callback `on_closing` mal configurado
- **Soluções**:
  ```python
  # 1. Iniciar thread de leitura de output
  self.stdout_thread = threading.Thread(target=self.read_output)
  self.stdout_thread.daemon = True
  self.stdout_thread.start()
  
  # 2. Adicionar delay antes de abrir webview
  import time
  time.sleep(3)
  
  # 3. Corrigir callback do evento closing
  window.events.closing += lambda: on_closing(window=window, streamlit_wrapper=streamlit_wrapper)
  
  # 4. Redirecionar stderr para stdout
  stderr=subprocess.STDOUT
  ```

### 3. **Fontconfig Warning (Não crítico)**
- **Mensagem**: `Fontconfig error: Cannot load default config file: No such file: (null)`
- **Impacto**: Apenas warning visual, não afeta funcionalidade
- **Solução**: Adicionado no início do `main.py`:
  ```python
  import warnings
  warnings.filterwarnings('ignore', message='.*fontconfig.*')
  ```

## Erros Potenciais Futuros

### 1. **Problemas com Portas**
- **Cenário**: Porta 8501 já em uso
- **Prevenção**: Verificar porta disponível antes de iniciar
- **Solução Sugerida**:
  ```python
  import socket
  def find_available_port(start_port=8501, max_attempts=10):
      for port in range(start_port, start_port + max_attempts):
          with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
              if s.connect_ex(('localhost', port)) != 0:
                  return port
      return start_port
  ```

### 2. **Dependências Ausentes**
- **Cenário**: Usuário sem todas as dependências instaladas
- **Prevenção**: Script de verificação de dependências
- **Solução Implementada**: `test_app.py` verifica imports

### 3. **Problemas com Webview/Qt**
- **Cenário**: Ambiente sem Qt ou WebEngine
- **Sintomas**: `webview.start()` falha
- **Solução Alternativa**: Modo fallback para abrir no navegador padrão

## Logs de Debug Implementados

### 1. **Arquivo `test_app.py`**
- Verifica dependências
- Testa Streamlit isoladamente
- Testa aplicativo principal

### 2. **Arquivo `run_debug.py`**
- Executa aplicativo com logging detalhado
- Captura stdout/stderr em tempo real
- Testa acesso à interface web

### 3. **Modo Debug no Webview**
- `webview.start(gui='qt', debug=True)`
- Habilita DevTools remoto na porta 8228

## Procedimento de Troubleshooting

### Passo 1: Verificar Dependências
```bash
python test_app.py
```

### Passo 2: Testar Streamlit Isoladamente
```bash
streamlit run app/views/streamlit_app.py --server.port 8501
```

### Passo 3: Executar com Debug
```bash
python run_debug.py
```

### Passo 4: Verificar Logs
```bash
tail -f app_debug.log
```

## Códigos de Erro

| Código | Descrição | Ação Recomendada |
|--------|-----------|------------------|
| ERR-001 | Importação falhou | Verificar `sys.path` e estrutura de diretórios |
| ERR-002 | Porta ocupada | Usar `find_available_port()` |
| ERR-003 | Streamlit não inicia | Verificar thread `read_output()` e delay |
| ERR-004 | Webview falha | Verificar Qt/WebEngine instalados |

## Melhorias Implementadas

1. **Thread Management**: Thread de leitura de output agora iniciada corretamente
2. **Error Handling**: Melhor tratamento de exceções em `main.py`
3. **Logging**: Sistema de logging mais detalhado
4. **Timing**: Delay adequado antes de abrir webview
5. **Callback Fix**: Correção do callback `on_closing`

## Status Atual
✅ **APLICATIVO FUNCIONAL**
- Streamlit inicia corretamente na porta 8501
- Webview abre interface gráfica
- Todas as páginas carregam sem erros de importação
- Threads gerenciadas corretamente
- Callbacks funcionando