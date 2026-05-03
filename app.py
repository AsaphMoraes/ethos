import pandas as pd
from pathlib import Path
import os

def data_files():
    _path = os.environ.get("USERPROFILE")
    if not _path:
        raise SystemError("Pasta do usuário não encontrada")
        
    _full_path = Path.joinpath(Path(_path),"Documents","Ethos Documents")
    try:    
        _files_list = os.listdir(_full_path)
        return [Path.joinpath(_full_path, file) for file in _files_list]
        
    except FileNotFoundError:
        os.mkdir(_full_path)
        return None

def data_df():
    _data_files = data_files()
    if not _data_files:
        return None
    return [pd.read_csv(_file) for _file in _data_files]

def filter_df():
    _dfs = data_df()
    _filter_df = []
    if _dfs:
        for _df in _dfs:
            _filter_df.append(_df.drop("Identificador", axis="columns"))
            
    _unify_dfs = pd.concat(_filter_df, ignore_index=True)
    _unify_dfs["Data"] = pd.to_datetime(_unify_dfs["Data"], dayfirst=True)
    _unify_dfs["Valor"] = _unify_dfs["Valor"].astype(float)
    return _unify_dfs.sort_values("Data", ascending=False)
        
    
def main():
    dfs = filter_df()
    print(dfs.dtypes)
    print(dfs)
        #print("Não há arquivos na pasta documentos")

if __name__ == "__main__":
    main()