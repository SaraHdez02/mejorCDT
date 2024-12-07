import pandas as pd

def read_csv(path):
    return pd.read_csv(path, delimiter=';',
                       dtype={
                           'consecutivo': str,
                           'banco': str,
                           'minplazo': int,
                           'maxplazo': int,
                           'tasa': float
                       },
                       converters={
                           'minmonto': lambda x: int(x.replace('.', '')),
                           'maxmonto': lambda x: int(x.replace('.', ''))
                       },
                       parse_dates=['fecha'])
