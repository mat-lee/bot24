
import pandas as pd
from rapidfuzz import fuzz
from polyfuzz.models import EditDistance


def test_distance(from_list, to_list):
    matcher = EditDistance()
    matches = matcher.match(from_list, to_list)

    assert isinstance(matches, pd.DataFrame)
    assert matches.Similarity.mean() > 0.0
    assert len(matches) == 6
    assert list(matches.columns) == ['From', 'To', 'Similarity']


def test_custom_scorer(from_list, to_list):
    matcher = EditDistance(scorer=fuzz.ratio)
    matches = matcher.match(from_list, to_list)

    assert isinstance(matches, pd.DataFrame)
    assert matches.Similarity.mean() > 0.0
    assert len(matches) == 6
    assert list(matches.columns) == ['From', 'To', 'Similarity']


def test_no_normalization(from_list, to_list):
    matcher = EditDistance(normalize=False)
    matches = matcher.match(from_list, to_list)

    assert isinstance(matches, pd.DataFrame)
    assert matches.Similarity.mean() > 50
    assert len(matches) == 6
    assert list(matches.columns) == ['From', 'To', 'Similarity']
