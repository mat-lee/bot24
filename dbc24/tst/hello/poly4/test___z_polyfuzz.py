
import pytest
from polyfuzz.models import EditDistance, TFIDF, RapidFuzz, SentenceEmbeddings
# sentence_model = SentenceEmbeddings("all-MiniLM-L6-v2")

import numpy as np
import pandas as pd
from rapidfuzz import fuzz

from polyfuzz import PolyFuzz
from polyfuzz.models import BaseMatcher


class MyModel(BaseMatcher):
    def match(self, from_list, to_list, **kwargs):
        # Calculate distances
        matches = [[fuzz.ratio(from_string, to_string) / 100
                    for to_string in to_list] for from_string in from_list]

        # Get best matches
        mappings = [to_list[index] for index in np.argmax(matches, axis=1)]
        scores = np.max(matches, axis=1)

        # Prepare dataframe
        matches = pd.DataFrame({'From': from_list,
                                'To': mappings,
                                'Similarity': scores})
        return matches
