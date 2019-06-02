##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
import pandas as pd


df = pd.read_csv('tbl2.tsv', sep='\t')
df['_c5b'] = df['_c5b'].astype(str)

df2 = pd.DataFrame({
    'lista': df.groupby(['_c0']).apply(lambda x: ','.join(sorted(x['_c5a'] + ':' + x['_c5b'])))
}).reset_index()

print(df2)
