import pandas as pd
import numpy as np

series = pd.read_csv('/hundredseriebox.csv')

df_series = pd.DataFrame(series)

#print(df_series.sort_values('score', ascending=False).head(20))

terror = df_series[(df_series['genre'] == 'Terror')]
#print(terror)

df_series['is_american'] = df_series['place'].str.contains('USA')

terror_filter = df_series['genre'] == 'Terror'
american_filter = df_series['is_american']

terror_american = df_series[terror_filter & american_filter] #series de terror americanas

#print(terror_american)

generos = series.groupby('genre')
print(generos['score'].aggregate(np.mean))   #media de score por genero
print(generos['score'].aggregate(np.sum).max())
