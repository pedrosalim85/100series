import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

series = pd.read_csv('C:/Users/Pedro/Desktop/PROGRAMACAO/DADOS/series/hundredseriebox.csv')

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
#print(generos['score'].aggregate(np.mean))   #media de score por genero

'''
series_json = df_series.to_json()

 Salve o JSON em um arquivo (por exemplo, 'dados.json')
with open('series.json', 'w') as arquivo:
    arquivo.write(series_json)
'''

generos = ['fantasy', 'terror', 'sitcom', 'comedy', 'war', 'drama', 'mafia', 'crime', 'thriller', 'history', 'apocalipse', 'mistery']
score = df_series['score']

fantasy = []
terror = []
sitcom = []
comedy = []
war = []
drama = []
mafia = []
crime = []
thriller = []
history = []
apocalipse = []
mistery =[]

for genre, nota in zip(df_series['genre'], df_series['score']):
    if genre == 'Fantasy':
        fantasy.append(nota)
    elif genre == 'Terror':
        terror.append(nota)
    elif genre == 'Sitcom':
        sitcom.append(nota)
    elif genre == 'Comedy':
        comedy.append(nota)
    elif genre == 'War':
        war.append(nota)
    elif genre == 'Drama':
        drama.append(nota)
    elif genre == 'Mafia':
        mafia.append(nota)
    elif genre == 'Crime':
        crime.append(nota)
    elif genre == 'Thriller':
        thriller.append(nota)
    elif genre == 'History':
        history.append(nota)
    elif genre == 'Apocalipse':
        apocalipse.append(nota)
    elif genre == 'Mistery':
        mistery.append(nota)
    else:
        pass

genres = []
genres.append(fantasy)
genres.append(terror)
genres.append(sitcom)
genres.append(comedy)
genres.append(war)
genres.append(drama)
genres.append(mafia)
genres.append(crime)
genres.append(thriller)
genres.append(history)
genres.append(apocalipse)
genres.append(mistery)



fig, ax = plt.subplots()
ax.boxplot(genres, labels=generos)

plt.ylabel('Score')


plt.tight_layout()
plt.show()
