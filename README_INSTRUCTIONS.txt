0 - Aplicativo com Streamlit e PyWebView[Qt]
1 - Aplicativo que faz a leitura de arquivos CSVs, formata para um padrão
   O padrão deve ser o banco de dados no SQLite.
2 - O aplicativo deve possuir página dashboard com os seguintes gráficos:
   - Radar de Eficiência de Custo por Fonte (Spider chart)
   - Área de Composição por Categoria (Stacked Area)
3 - O aplicativo deve possuir página simulação que deve ter campos:
   - Valor inicial
   - Valor a cada mês
   e retornar valor final dos campos e agregar o CDI
4 - O aplicativo deve possuir página de upload de CSV que aceitam diversos formatos
   (todos os formatos devem ser comparados com os formatos salvos em 1 arquivo JSON a parte)
   e manda para o banco de dados
5 - O aplicativo deve possuir página para mostrar todos os dados do banco de dados
   e uma uma pesquisa com filtro de data, nome e categoria
6 - As páginas devem ser acessadas através de uma sidebar de navigation com formato
   ícones e texto
7 - Utilize venv e diretórios para organizar o código seguindo padrões MVC
   e crie o requirements
