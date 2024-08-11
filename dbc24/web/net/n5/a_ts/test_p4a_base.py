
import pytest
import numpy as np
import pandas as pd
from rapidfuzz import fuzz
from polyfuzz.models import BaseMatcher


class MyIncorrectModel(BaseMatcher):
    pass

def test_custom_model_incorrect():

    with pytest.raises(TypeError):
        model = BaseMatcher()


class MyCorrectModel(BaseMatcher):
    def match(self, from_list, to_list):
        # Calculate distances
        matches = [[fuzz.ratio(from_string, to_string) / 100 for to_string in to_list] for from_string in from_list]

        # Get best matches
        mappings = [to_list[index] for index in np.argmax(matches, axis=1)]
        scores = np.max(matches, axis=1)

        # Prepare dataframe
        matches = pd.DataFrame({'From': from_list, 'To': mappings, 'Similarity': scores})
        return matches

def test_custom_model_correct(from_list, to_list):
    matcher = MyCorrectModel()
    matches = matcher.match(from_list, to_list)

    assert isinstance(matches, pd.DataFrame)
    assert matches.Similarity.mean() > 0.0
    assert len(matches) == 6
    assert list(matches.columns) == ['From', 'To', 'Similarity']
