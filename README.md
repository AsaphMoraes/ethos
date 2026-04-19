# Ethos Financeiro

![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.56+-red.svg)
![PyWebView](https://img.shields.io/badge/PyWebView-6.2+-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3.45+-yellow.svg)

Aplicativo desktop financeiro desenvolvido em Python com interface web moderna, arquitetura MVC e suporte a múltiplos formatos de CSV.

## 🚀 Visão Geral

O **Ethos** é um aplicativo desktop que combina a simplicidade do Streamlit com a experiência nativa do PyWebView, oferecendo uma solução completa para gestão e análise de dados financeiros.

### ✨ Principais Características

- **Interface Desktop Nativa**: Aplicativo standalone com PyWebView (Qt backend)
- **Arquitetura MVC**: Separação clara entre Model, View e Controller
- **Multi-formato CSV**: Suporte a 4 formatos pré-configurados de arquivos CSV
- **Dashboard Interativo**: Visualizações com Plotly e gráficos em tempo real
- **Simulação de Investimentos**: Cálculos de juros compostos com CDI
- **Banco de Dados SQLite**: Armazenamento local e persistente
- **Interface Modular**: Páginas separadas para melhor manutenção

## 📁 Estrutura do Projeto

```
ethos/
├── app/                          # Aplicação principal
│   ├── controllers/              # Lógica de processamento
│   │   └── processamento.py      # Processamento de CSV
│   ├── models/                   # Modelos de dados
│   │   └── database.py           # Banco de dados SQLite
│   ├── views/                    # Interface do usuário
│   │   ├── pages/                # Páginas do Streamlit
│   │   │   ├── dashboard.py      # Dashboard principal
│   │   │   ├── simulacao.py      # Simulação de investimentos
│   │   │   ├── upload.py         # Upload de CSV
│   │   │   ├── listar_dados.py   # Listagem de dados
│   │   │   └── __init__.py
│   │   ├── utils/                # Utilitários
│   │   │   └── styles.py         # Estilos CSS
│   │   └── streamlit_app.py      # Aplicativo Streamlit principal
│   └── data/                     # Dados e configurações
│       └── formatos/             # Formatos de CSV
│           └── csv_formats.json  # Configuração de formatos
├── database/                     # Banco de dados SQLite
│   └── dados.db                  # Arquivo do banco de dados
├── AGENT_GUIDE/                  # Documentação técnica completa
├── logs/                         # Logs de execução
├── venv/                         # Ambiente virtual Python
├── main.py                       # Ponto de entrada do aplicativo
├── requirements.txt              # Dependências do projeto
├── start.sh                      # Script de inicialização
└── README.md                     # Este arquivo
```

## 🛠️ Instalação e Configuração

### Pré-requisitos

- Python 3.14 ou superior
- Qt 6.11+ (para PyWebView)
- Fontconfig (opcional, para evitar warnings)

### Instalação Passo a Passo

1. **Clone o repositório**:
   ```bash
   git clone <repositorio>
   cd ethos
   ```

2. **Crie e ative o ambiente virtual**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Instale o PyQt6 (backend do PyWebView)**:
   ```bash
   pip install PyQt6
   ```

### Métodos de Execução

#### Método 1: Script de Inicialização (Recomendado)
```bash
./start.sh
```
O script `start.sh` verifica dependências, ativa o ambiente virtual e inicia o aplicativo.

#### Método 2: Execução Direta
```bash
source venv/bin/activate
python main.py
```

## 🎯 Funcionalidades Detalhadas

### 1. Dashboard Principal (`🏠 Dashboard`)

**KPIs Principais:**
- Total de registros no banco de dados
- Valor total acumulado (R$)
- CDI médio dos investimentos

**Visualizações:**
- **Radar de Eficiência**: Gráfico polar mostrando distribuição por fonte
- **Área de Composição**: Gráfico empilhado por categoria
- **Tabela de Registros**: Últimos 10 registros com todos os detalhes

### 2. Simulação de Investimentos (`📊 Simulação`)

**Parâmetros Configuráveis:**
- Valor inicial do investimento
- Valor mensal adicional
- Período em meses

**Cálculos:**
- Juros compostos baseados no CDI (10.8% ao ano)
- Projeção de crescimento mensal
- Valor final estimado

**Visualização:**
- Gráfico de linha mostrando evolução do patrimônio
- Detalhamento mês a mês

### 3. Upload de CSV (`📁 Upload`)

**Formatos Suportados:**
- **Padrao1**: `data, categoria, fonte, valor, cdi` (separador: `,`)
- **Padrao2**: `data, fonte, valor, cdi, categoria` (separador: `;`)
- **Padrao3**: `categoria, data, valor, cdi, fonte` (separador: `|`)
- **Padrao4**: `fonte, data, categoria, valor, cdi` (separador: `\t`)

**Funcionalidades:**
- Seleção interativa de formato
- Upload de arquivo CSV
- Processamento automático com validação
- Importação para banco de dados SQLite
- Opção para limpar banco de dados

### 4. Listagem de Dados (`📋 Listar Dados`)

**Filtros Disponíveis:**
- Por data (busca parcial)
- Por fonte/nome (busca parcial)
- Por categoria (busca parcial)

**Visualização:**
- Tabela completa com todos os registros
- Ordenação por data (mais recentes primeiro)
- Métricas de resumo

## 🗃️ Banco de Dados

### Estrutura da Tabela `dados`

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `id` | INTEGER PRIMARY KEY AUTOINCREMENT | Identificador único |
| `data` | DATE | Data do registro (YYYY-MM-DD) |
| `categoria` | TEXT | Categoria do investimento |
| `fonte` | TEXT | Fonte/instituição financeira |
| `valor` | REAL | Valor monetário (R$) |
| `cdi` | REAL | Taxa CDI (decimal, ex: 0.108) |
| `criado_em` | TIMESTAMP DEFAULT CURRENT_TIMESTAMP | Data de criação |

### Operações do Banco de Dados

- **Criação automática de tabelas**: Executada na inicialização do app
- **Inserção em lote**: Processamento de múltiplos registros de CSV
- **Consultas otimizadas**: Filtros combinados e ordenação
- **Agregações**: Somas por fonte e categoria

## 🔧 Arquitetura Técnica

### Model-View-Controller (MVC)

**Model (`app/models/database.py`):**
- Gerencia conexões com SQLite
- Define schema do banco de dados
- Implementa operações CRUD
- Fornece funções de agregação

**View (`app/views/pages/`):**
- Páginas Streamlit independentes
- Interface de usuário responsiva
- Componentes reutilizáveis
- Estilos centralizados

**Controller (`app/controllers/processamento.py`):**
- Processamento de arquivos CSV
- Validação de dados
- Transformação de formatos
- Integração com o Model

### PyWebView + Streamlit

**Fluxo de Execução:**
1. `main.py` inicia o Streamlit como subprocesso
2. Streamlit roda na porta 8501 em modo headless
3. PyWebView cria janela desktop com Qt backend
4. Janela carrega interface Streamlit via URL local
5. Threads separadas gerenciam output e eventos

**Vantagens:**
- Interface web moderna com experiência desktop
- Fácil desenvolvimento com Streamlit
- Performance nativa com PyWebView
- Cross-platform (Linux, Windows, macOS)

## 📊 Formatos de CSV

### Configuração (`app/data/formatos/csv_formats.json`)

```json
{
  "csv_formats": {
    "Padrao1": {
      "nome_arquivo": "formato_padrao_1.csv",
      "colunas": ["data", "categoria", "fonte", "valor", "cdi"],
      "separador": ",",
      "header": true,
      "data_format": "DD/MM/YYYY"
    }
  }
}
```

### Campos Obrigatórios

1. **data**: Data no formato especificado
2. **categoria**: Categoria do investimento (ex: "Renda Fixa", "Ações")
3. **fonte**: Instituição financeira (ex: "Banco X", "Corretora Y")
4. **valor**: Valor monetário (ex: 1000.50)
5. **cdi**: Taxa CDI em decimal (ex: 0.108 para 10.8%)

### Formatos de Data Suportados

- `DD/MM/YYYY` (ex: 19/04/2026)
- `YYYY-MM-DD` (ex: 2026-04-19)
- `DD-MM-YYYY` (ex: 19-04-2026)

### Separadores Suportados

- Vírgula (`,`)
- Ponto e vírgula (`;`)
- Barra vertical (`|`)
- Tabulação (`\t`)

## 🚀 Desenvolvimento

### Adicionando Nova Página

1. **Crie o arquivo da página**:
   ```python
   # app/views/pages/nova_pagina.py
   import streamlit as st
   
   def nova_pagina_page():
       st.title("Nova Página")
       # Sua implementação aqui
   ```

2. **Adicione à navegação**:
   ```python
   # Em app/views/streamlit_app.py
   from pages.nova_pagina import nova_pagina_page
   
   # Adicione ao navigation
   pg = st.navigation([
       # ... páginas existentes
       st.Page(nova_pagina_page, title="Nova Página", icon="⭐"),
   ])
   ```

### Adicionando Novo Formato de CSV

1. **Edite o arquivo de configuração**:
   ```json
   {
     "csv_formats": {
       "NovoFormato": {
         "nome_arquivo": "novo_formato.csv",
         "colunas": ["data", "fonte", "categoria", "valor", "cdi"],
         "separador": ";",
         "header": true,
         "data_format": "DD/MM/YYYY"
       }
     }
   }
   ```

2. **O formato estará automaticamente disponível na interface**

### Estilos Customizados

Os estilos estão centralizados em `app/views/utils/styles.py`:

```python
STYLES = """
<style>
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .stSidebar {
        background-color: #1e1e1e;
    }
    /* Adicione seus estilos aqui */
</style>
"""
```

## 🔍 Troubleshooting

### Problemas Comuns e Soluções

#### 1. Fontconfig Warning
```
Fontconfig error: Cannot load default config file: No such file: (null)
```
**Solução**: Use `./run.sh` ou instale fontconfig:
```bash
sudo apt-get install fontconfig libfontconfig1
```

#### 2. PyWebView não inicia
```
ModuleNotFoundError: No module named 'gi'
```
**Solução**: Instale PyQt6:
```bash
pip install PyQt6
```

#### 3. Streamlit não inicia no aplicativo
**Solução**: Verifique se a thread de output está sendo iniciada em `main.py`

#### 4. Importação de módulos falha
**Solução**: Verifique `sys.path` em `app/views/streamlit_app.py`

### Logs e Debug

- **Logs de execução**: `logs/` directory
- **Modo debug do PyWebView**: `webview.start(gui='qt', debug=True)`
- **Output do Streamlit**: Capturado em tempo real pelo `StreamlitWrapper`

## 📚 Documentação Técnica

A pasta `AGENT_GUIDE/` contém documentação completa:

- **01_CODING_PATTERNS.md**: Padrões de código
- **02_PROTECTED_FILES.md**: Arquivos protegidos
- **03_PROBLEMS_SOLUTIONS.md**: Problemas e soluções
- **04_DEVELOPMENT_GUIDE.md**: Guia de desenvolvimento
- **05_PYWEBVIEW_GUIDE.md**: Guia do PyWebView
- **06_ISSUES_DB.md**: Banco de dados de problemas
- **07_DIAGNOSTIC_REPORT.md**: Relatório de diagnóstico
- **08_ERROR_LOG.md**: Registro de erros

## 📦 Dependências

```txt
streamlit>=1.28.0      # Framework web
plotly>=5.17.0         # Gráficos interativos
pandas>=2.1.0          # Manipulação de dados
pywebview>=5.0.0       # Interface desktop
matplotlib>=3.8.0      # Gráficos estáticos
openpyxl>=3.1.0        # Suporte a Excel
numpy>=1.26.0          # Computação numérica
pillow>=10.0.0         # Processamento de imagens
PyQt6>=6.11.0          # Backend do PyWebView (opcional)
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## ✨ Agradecimentos

- [Streamlit](https://streamlit.io/) por simplificar aplicações web em Python
- [PyWebView](https://pywebview.flowrl.com/) por trazer aplicações web para o desktop
- [Plotly](https://plotly.com/python/) por gráficos interativos incríveis
- Comunidade Python por todas as bibliotecas incríveis

---

**Desenvolvido com ❤️ para simplificar a gestão financeira**

*Última atualização: Abril 2026*