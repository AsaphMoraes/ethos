import sqlite3
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
DB_PATH = BASE_DIR / "database" / "dados.db"

def get_connection():
    os.makedirs(DB_PATH.parent, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

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
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def add_dados(data, categoria, fonte, valor, cdi):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO dados (data, categoria, fonte, valor, cdi)
        VALUES (?, ?, ?, ?, ?)
    ''', (data, categoria, fonte, valor, cdi))
    conn.commit()
    conn.close()

def get_all_dados():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dados ORDER BY data DESC')
    dados = cursor.fetchall()
    conn.close()
    return dados

def get_dados_filtrados(filtro_data=None, filtro_nome=None, filtro_categoria=None):
    conn = get_connection()
    cursor = conn.cursor()
    
    query = 'SELECT * FROM dados WHERE 1=1'
    params = []
    
    if filtro_data:
        query += ' AND data LIKE ?'
        params.append(f'%{filtro_data}%')
    
    if filtro_nome:
        query += ' AND fonte LIKE ?'
        params.append(f'%{filtro_nome}%')
    
    if filtro_categoria:
        query += ' AND categoria LIKE ?'
        params.append(f'%{filtro_categoria}%')
    
    query += ' ORDER BY data DESC'
    
    cursor.execute(query, params)
    dados = cursor.fetchall()
    conn.close()
    return dados

def get_dados_por_fonte():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT fonte, SUM(valor) as total
        FROM dados
        GROUP BY fonte
        ORDER BY total DESC
    ''')
    dados = cursor.fetchall()
    conn.close()
    return dados

def get_dados_por_categoria():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT categoria, SUM(valor) as total
        FROM dados
        GROUP BY categoria
        ORDER BY total DESC
    ''')
    dados = cursor.fetchall()
    conn.close()
    return dados

def get_dados_por_fonte_e_data():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT fonte, data, SUM(valor) as total
        FROM dados
        GROUP BY fonte, data
        ORDER BY data DESC
    ''')
    dados = cursor.fetchall()
    conn.close()
    return dados

def clear_dados():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM dados')
    conn.commit()
    conn.close()