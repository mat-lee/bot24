from typing import Union

from polyfuzz1.linkage import single_linkage
from polyfuzz1.utils import check_matches
from polyfuzz1.models import TFIDF, BaseMatcher, EditDistance
from polyfuzz1.metrics import precision_recall_curve, visualize_precision_recall

class PolyFuzzMatch:
    def __init__(self,
         method: BaseMatcher = None,
         matches = None
        ):

        self.method = method
        self.matches = matches

    def match(self,
              from_list: list[str],
              to_list: list[str] = None
              ):
        self.matches = self.method.match(from_list, to_list)
        return self

    def visualize_precision_recall(self,
                                   kde: bool = False,
                                   save_path: str = None
                                   ):
        """ Calculate and visualize precision-recall curves."""
        # check_matches(self)

        self.min_precisions = {}
        self.recalls = {}
        self.average_precisions = {}

        for name, match in self.matches.items():
            min_precision, recall, average_precision = precision_recall_curve(match)
            self.min_precisions[name] = min_precision
            self.recalls[name] = recall
            self.average_precisions[name] = average_precision

        visualize_precision_recall(self.matches, self.min_precisions, self.recalls, kde, save_path)

class PolyFuzzGroup:
    def __init__(self,
         method: BaseMatcher = None,
         matches = None
        ):

        self.method = method
        self.matches = matches

    def group(self,
              link_min_similarity: float = 0.75,
              group_all_strings: bool = False):
        """ From the matches, group the `To` matches together using single linkage

         Arguments:
             model: you can choose one of the models in `polyfuzz.models` to be used as a grouper
             link_min_similarity: the minimum similarity between strings before they are grouped
                                  in a single linkage fashion
             group_all_strings: if you want to compare a list of strings with itself and then cluster
                                those strings, set this to True. Otherwise, only the strings that
                                were mapped To are clustered.

         Updates:
            self.matches: Adds a column `Group` that is the grouped version of the `To` column
         """
        # check_matches(self)
        self.clusters = {}
        self.cluster_mappings = {}

        model = self.method

        self._create_groups(model, link_min_similarity, group_all_strings)

    def _create_groups(self,
                       model: BaseMatcher,
                       link_min_similarity: float,
                       group_all_strings: bool):
        """ Create groups based on either the To mappings if you compare two different lists of strings, or
        the From mappings if you compare lists of strings that are equal (set group_all_strings to True)
        """

        matches = self.matches

        clusters, cluster_id_map, cluster_name_map = single_linkage(matches, link_min_similarity)

        # Map the `to` list to groups
        df = self.matches
        df["Group"] = df['To'].map(cluster_name_map).fillna(df['To'])
        self.matches = df

        # Track clusters and their ids
        self.clusters = clusters
        self.cluster_mappings = cluster_id_map