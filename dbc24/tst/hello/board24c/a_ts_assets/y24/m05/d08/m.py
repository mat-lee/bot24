


# %%

import json

m = json.load(open('movie_titles.json'))
m1 = m['IMDB']
m2 = m['Netflix']

with open('movie_titles_imdb.json', 'w') as f1:
    json.dump(m1, f1)

with open('movie_titles_netflix.json', 'w') as f2:
    json.dump(m2, f2)

