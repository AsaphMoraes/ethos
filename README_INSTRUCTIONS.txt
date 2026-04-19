# Instruções do Projeto Ethos

## 📋 Resumo

Aplicativo web financeiro desenvolvido em Python usando Streamlit, gerenciando dados em SQLite com estrutura MVC, arquivos de página separados e suporte a múltiplos formatos de CSV.

## ✅ Requisitos

1. **Streamlit + PyWebView[Qt]**: Aplicativo web em Python
2. **Leitura de CSVs**: Processamento de arquivos CSV em diversos formatos
3. **Banco de Dados**: Integração com SQLite
4. **Dashboard Interativo**: Visualização de dados com gráficos

## 📄 Funcionalidades Principais

### 1. Dashboard (dashboard.py)
- **KPIs Principais**: Total de registros, valor total e CDI médio
- **Radar de Eficiência**: Gráfico espacial (Spider Chart) por fonte
- **Área de Composição**: Gráfico empilhado por categoria
- **Tabela de Registros**: Últimos 10 registros

### 2. Simulação de Investimentos (simulacao.py)
- Campo: Valor Inicial
- Campo: Valor a cada mês
- Configuração: Número de meses
- Cálculo: Valor final com juros compostos (CDI 10.8% anual)
- Visualização: Gráfico de evolução

### 3. Upload de CSV (upload.py)
- Suporte a 4 formatos pré-configurados
- Comparação automática com formato JSON
- Importação para banco de dados
- Limpeza de dados

### 4. Listagem e Busca (listar_dados.py)
- Visualização completa de registros
- Filtros: Data, Fonte/Nome, Categoria
- Métricas resumo

### 5. Navegação (sidebar.py)
- Sidebar com ícones e texto
- 4 páginas: Dashboard, Simulação, Upload CSV, Listar Dados

### 6. Estrutura MVC
- **Model**: `app/models/database.py` (123 linhas)
- **View**: `app/views/pages/` (4 páginas)
  - `dashboard.py` (88 linhas)
  - `simulacao.py` (71 linhas)
  - `upload.py` (56 linhas)
  - `listar_dados.py` (54 linhas)
  - `sidebar.py` (25 linhas)
- **Controller**: `app/controllers/processamento.py` (78 linhas)

### 7. venv e requirements
- Ambiente virtual configurado
- Dependências documentadas

### 8. CSS Organizado
- `app/views/utils/styles.py` (29 linhas)
- Estilos centralizados e reaproveitáveis

## 🗂️ Estrutura do Projeto

```
ethos/
├── app/
│   ├── controllers/ (C) - Processamento de dados
│   ├── models/ (M) - Banco de dados
│   ├── views/ (V) - Interface Streamlit
│   │   ├── pages/ - 5 arquivos separados
│   │   └── utils/ - CSS e utilitários
│   └── data/formatos/ - Configuração CSV
├── database/ - Banco SQLite
├── venv/ - Ambiente virtual
├── requirements.txt
├── README.md
├── README_INSTRUCTIONS.txt
└── STRUCTURE.md - Documentação técnica
```

## 🚀 Instalação e Execução

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar aplicativo
./venv/bin/streamlit run app/views/streamlit_app.py
```

## 📊 Banco de Dados SQLite

**Tabela**: `dados`
- `id`: INTEGER PRIMARY KEY
- `data`: DATE
- `categoria`: TEXT
- `fonte`: TEXT
- `valor`: REAL
- `cdi`: REAL
- `criado_em`: TIMESTAMP

## 📝 Formatando CSV

Arquivo: `app/data/formatos/csv_formats.json`

```json
{
  "csv_formats": {
    "Formato1": {
      "nome_arquivo": "exemplo.csv",
      "colunas": ["data", "categoria", "fonte", "valor", "cdi"],
      "separador": ",",
      "header": true,
      "data_format": "DD/MM/YYYY"
    }
  }
}
```

**Formatos de data**: DD/MM/YYYY, YYYY-MM-DD, DD-MM-YYYY
**Separadores**: Vírgula (,), Ponto e vírgula (;), Barra (|), Tabulação (\t)

## 🔧 Dependências

- streamlit >= 1.28.0
- plotly >= 5.17.0
- pandas >= 2.1.0
- pywebview >= 5.0.0
- matplotlib >= 3.8.0
- openpyxl >= 3.1.0
- numpy >= 1.26.0
- pillow >= 10.0.0

## 📊 Métricas de Código

- **streamlit_app.py**: 25 linhas (antigo: 332 linhas)
- **Total arquivos**: 15 arquivos Python
- **Páginas separadas**: 4 páginas
- **Código modular**: Cada arquivo com responsabilidade única
- **Código limpo**: Facilidade de manutenção

## 📄 Documentação

- **README.md**: Documentação completa do projeto
- **README_INSTRUCTIONS.txt**: Instruções do projeto
- **STRUCTURE.md**: Documentação técnica detalhada

## 🏗️ Padrões de Design

### MVC (Model-View-Controller)
- Separação clara de responsabilidades
- Arquivos de página independentes
- Lógica separada em controllers

### Modularização
- Páginas como módulos separados
- Utilitários organizados em diretórios
- Configuração em arquivo JSON

### Separation of Concerns
- Interface separada da lógica
- Estilos centralizados
- Dados separados da apresentação

## 📖 Como Adicionar Nova Página

1. Criar arquivo `app/views/pages/nova_pagina.py`
2. Implementar função `nova_pagina_page()`
3. Adicionar entrada em `app/views/pages/sidebar.py`
4. Importar em `app/views/pages/__init__.py`
5. Atualizar `app/views/streamlit_app.py`

## 🔍 Princípios Seguidos

- Single Responsibility Principle
- DRY (Don't Repeat Yourself)
- Clean Code
- Maintainability First
- Modularity

## 📄 Licença

Livre para uso e modificação