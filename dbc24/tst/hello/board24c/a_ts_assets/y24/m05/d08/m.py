


# %%
import os
import json
import pandas as pd
from polyfuzz import PolyFuzz

m_imdb = json.load(open('../d09/movie_titles_imdb.json'))
m_netflix = json.load(open('../d09/movie_titles_netflix.json'))
m1 = m_netflix[:3000]
m2 = m_netflix[3000:]

with open('movie_titles_netflix_a.json', 'w') as f1:
    json.dump(m1, f1)

with open('movie_titles_netflix_b.json', 'w') as f2:
    json.dump(m2, f2)


class QuickMatch():
    def __init__(self, path0, path1, path2):
        list1 = json.load(open(path1))
        list2 = json.load(open(path2))

        # For each list, separate values by their starting letter
        series_list1 = self.list_to_alphabet_series(list1)
        series_list2 = self.list_to_alphabet_series(list2)

        # Get the match score of each list
        match_scores = self.match_letter_series(series_list1, series_list2, 0.5)

        match_scores.to_json(os.path.join(path0, "match_scores.json"))

    @staticmethod
    def list_to_alphabet_series(list):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphabet_list = [[] for _ in range(len(alphabet) + 1)]

        # Make list where each index stores names for each letter
        for value in list:
            if value[0] in alphabet or value[0] in alphabet.upper():
                alphabet_list[alphabet.index(value[0].lower())].append(value)
            else:  # Special characters
                alphabet_list[-1].append(value)

        series_list = []
        for i, letter in enumerate(alphabet):
            series = pd.Series(alphabet_list[i])
            series_list.append(series)

        # Special characters
        series_list.append(pd.Series(alphabet_list[-1]))

        return series_list

    @staticmethod
    def match_letter_series(to_table, from_table, threshold):
        match_list = []
        for from_idx in range(len(from_table)):
            from_list = from_table[from_idx].tolist()
            for to_idx in range(len(to_table)):
                to_list = to_table[to_idx].tolist()
                model = PolyFuzz('TF-IDF').match(from_list, to_list)
                df = model.get_matches()
                # Remove values below a threshold
                df = df[df['Similarity'] > threshold]
                match_list.append(df)

        dataframe = pd.concat(match_list)
        dataframe.reset_index(inplace=True)
        return dataframe

if __name__ == "__main__":
    q = QuickMatch('../d10/',
                    '../d08/movie_titles_netflix_a.json',
                   '../d08/movie_titles_netflix_b.json')