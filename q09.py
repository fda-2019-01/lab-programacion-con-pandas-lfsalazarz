##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 
import pandas as pd


df = pd.read_csv('tbl0.tsv', sep='\t')
df['_c2'] = df['_c2'].astype(str)
df2 = pd.DataFrame({'lista' : df.groupby( ["_c1"] ).apply(lambda x: ':'.join(sorted(x['_c2']))) }).reset_index()
df2.columns = ['_c0', 'lista']
print(df2)
