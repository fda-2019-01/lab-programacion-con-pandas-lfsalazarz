##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 
import pandas as pd


df = pd.read_csv('tbl0.tsv', sep='\t')
df['ano'] = df['_c3'].map(lambda x: x.split('-')[0])
print(df)
