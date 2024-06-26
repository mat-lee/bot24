
import pytest
from polyfuzz.linkage import single_linkage
from polyfuzz.models import TFIDF


@pytest.mark.parametrize("min_similarity", [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1.])
def test_linkage(min_similarity, from_list, to_list):

    model = TFIDF(cosine_method="sparse")
    matches = model.match(from_list, to_list)
    clusters, cluster_mapping, cluster_name_map = single_linkage(matches, min_similarity)

    assert isinstance(clusters, dict)
    assert isinstance(cluster_mapping, dict)
    assert isinstance(cluster_name_map, dict)

    if min_similarity == 1.:
        assert clusters == {}
        assert cluster_mapping == {}
        assert cluster_name_map == {}

    elif min_similarity >= 0.8:
        assert max(cluster_mapping.values()) == 1
        assert len(cluster_name_map) == 2

    elif min_similarity >= 0.6:
        assert max(cluster_mapping.values()) > 1
        assert len(cluster_name_map) == 3
