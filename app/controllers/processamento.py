import pandas as pd
import json
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))
from models.database import add_dados

FORMATOS_PATH = Path(__file__).parent.parent / "data" / "formatos" / "csv_formats.json"

def carregar_formatos():
    with open(FORMATOS_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)['csv_formats']

def processar_csv(arquivo_csv):
    try:
        df = pd.read_csv(arquivo_csv)
        formatos = carregar_formatos()
        
        encontrado_formato = None
        
        for nome_formato, formato in formatos.items():
            colunas_padrao = set(formato['colunas'])
            colunas_arquivo = set(df.columns)
            
            if colunas_padrao.issubset(colunas_arquivo):
                encontrado_formato = (nome_formato, formato)
                break
        
        if not encontrado_formato:
            return {'sucesso': False, 'mensagem': 'Formato CSV não reconhecido'}
        
        nome_formato, formato = encontrado_formato
        
        for _, row in df.iterrows():
            try:
                data = row[formato['colunas'][0]]
                categoria = row[formato['colunas'][1]]
                fonte = row[formato['colunas'][2]]
                valor = float(row[formato['colunas'][3]])
                cdi = float(row[formato['colunas'][4]])
                
                if pd.notna(data) and pd.notna(categoria) and pd.notna(fonte):
                    data_formatada = str(data).split(' ')[0]
                    if 'DD' in formato['data_format'] or 'dd' in formato['data_format']:
                        partes = data_formatada.split('/')
                        if len(partes) == 3:
                            data_formatada = f'{partes[2]}-{partes[1]}-{partes[0]}'
                    elif 'YYYY' in formato['data_format']:
                        partes = data_formatada.split('-')
                        if len(partes) == 3:
                            data_formatada = f'{partes[2]}/{partes[1]}/{partes[0]}'
                    
                    add_dados(data_formatada, str(categoria), str(fonte), valor, cdi)
            except Exception as e:
                print(f"Erro ao processar linha: {e}")
        
        return {'sucesso': True, 'mensagem': f'Dados importados do formato {nome_formato} com sucesso'}
    
    except Exception as e:
        return {'sucesso': False, 'mensagem': f'Erro ao processar CSV: {str(e)}'}

def simular_cdi(valor_inicial, valor_mensal, meses):
    valor_atual = float(valor_inicial)
    cdi_anual = 0.108
    cdi_mensal = cdi_anual / 12
    
    historico = []
    
    for mes in range(1, meses + 1):
        valor_atual += float(valor_mensal)
        valor_atual *= (1 + cdi_mensal)
        historico.append({
            'mes': mes,
            'valor': valor_atual
        })
    
    return {
        'valor_final': valor_atual,
        'historico': historico
    }