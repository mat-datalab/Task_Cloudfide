import pandas

def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:

    if not new_column or not all(c.isalpha() or c == '_' for c in new_column) or new_column in df.columns:
        return pandas.DataFrame()
    
    for col in df.columns:
        if not col or not all(c.isalpha() or c == '_' for c in col):
            return pandas.DataFrame()
    
    df_copy = df.copy()

    try:
        result = df_copy.eval(role)
        df_copy[new_column] = result
    except Exception:
        return pandas.DataFrame()
    return df_copy