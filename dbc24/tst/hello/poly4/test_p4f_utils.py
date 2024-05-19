
import pytest
import pandas as pd
from polyfuzz.models._utils import cosine_similarity


@pytest.mark.parametrize("method", ["sparse", "knn", "sklearn"])
def test_extract_best_matches(method, from_vector, to_vector, from_list, to_list):

    matches = cosine_similarity(from_vector, to_vector, from_list, to_list, method=method)

    assert isinstance(matches, pd.DataFrame)
    assert matches.Similarity.mean() > 0.0
    assert len(matches) == 6
    assert list(matches.columns) == ['From', 'To', 'Similarity']


@pytest.mark.parametrize("method", ["sparse", "knn", "sklearn"])
def test_extract_best_matches_same_list(method, from_vector, to_vector, from_list, to_list):

    matches = cosine_similarity(from_vector, to_vector, from_list, to_list, method=method)

    assert isinstance(matches, pd.DataFrame)
    assert matches.Similarity.mean() > 0.0
    assert len(matches) == 6
    assert list(matches.columns) == ['From', 'To', 'Similarity']
