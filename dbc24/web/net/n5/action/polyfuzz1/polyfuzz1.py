from typing import Union

from polyfuzz1.linkage import single_linkage
from polyfuzz1.utils import check_matches
from polyfuzz1.models import TFIDF, BaseMatcher, EditDistance
from polyfuzz1.metrics import precision_recall_curve, visualize_precision_recall


class PolyFuzz1:
    """
    PolyFuzz class for Fuzzy string matching, grouping, and evaluation.
    """

    def __init__(self,
         method: Union[str,
                 BaseMatcher,
                 list[BaseMatcher]] = "TF-IDF",
         verbose: bool = False):

        self.method = method

        self.matches = None

    def match(self,
              from_list: list[str],
              to_list: list[str] = None,
              top_n: int = 1):

        if isinstance(self.method, str):
            if self.method in ["TF-IDF", "TFIDF"]:
                self.method = TFIDF(min_similarity=0, top_n=top_n)
                self.matches = {"TF-IDF": self.method.match(from_list, to_list)}
            elif self.method in ["EditDistance", "Edit Distance"]:
                self.method = EditDistance()
                self.matches = {"EditDistance": self.method.match(from_list, to_list)}

        # Custom models
        elif isinstance(self.method, BaseMatcher):
            self.matches = {self.method.model_id: self.method.match(from_list, to_list)}
            # logger.info(f"Ran model with model id = {self.method.model_id}")

        return self

    def visualize_precision_recall(self,
                                   kde: bool = False,
                                   save_path: str = None
                                   ):
        """ Calculate and visualize precision-recall curves."""
        check_matches(self)

        self.min_precisions = {}
        self.recalls = {}
        self.average_precisions = {}

        for name, match in self.matches.items():
            min_precision, recall, average_precision = precision_recall_curve(match)
            self.min_precisions[name] = min_precision
            self.recalls[name] = recall
            self.average_precisions[name] = average_precision

        visualize_precision_recall(self.matches, self.min_precisions, self.recalls, kde, save_path)

    def group(self,
              model: Union[str, BaseMatcher] = None,
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
        check_matches(self)
        self.clusters = {}
        self.cluster_mappings = {}

        # Standard models - quick access
        if isinstance(model, str):
            if model in ["TF-IDF", "TFIDF"]:
                model = TFIDF(n_gram_range=(3, 3), min_similarity=link_min_similarity)
            elif self.method in ["EditDistance", "Edit Distance"]:
                model = RapidFuzz()
            elif self.method in ["Embeddings", "Embedding"]:
                model = Embeddings(min_similarity=link_min_similarity)
            else:
                raise ValueError("Please instantiate the model with one of the following methods: \n"
                                 "* 'TF-IDF'\n"
                                 "* 'EditDistance'\n"
                                 "* 'Embeddings'\n"
                                 "* Or None if you want to automatically use TF-IDF")

        # Use TF-IDF if no model is specified
        elif not model:
            model = TFIDF(n_gram_range=(3, 3), min_similarity=link_min_similarity)

        # Group per model
        for name, match in self.matches.items():
            self._create_groups(name, model, link_min_similarity, group_all_strings)

    def _create_groups(self,
                       name: str,
                       model: BaseMatcher,
                       link_min_similarity: float,
                       group_all_strings: bool):
        """ Create groups based on either the To mappings if you compare two different lists of strings, or
        the From mappings if you compare lists of strings that are equal (set group_all_strings to True)
        """

        if group_all_strings:
            strings = list(self.matches[name].From.dropna().unique())
        else:
            strings = list(self.matches[name].To.dropna().unique())

        # Create clusters
        matches = model.match(strings)
        clusters, cluster_id_map, cluster_name_map = single_linkage(matches, link_min_similarity)

        # Map the `to` list to groups
        df = self.matches[name]
        df["Group"] = df['To'].map(cluster_name_map).fillna(df['To'])
        self.matches[name] = df

        # Track clusters and their ids
        self.clusters[name] = clusters
        self.cluster_mappings[name] = cluster_id_map

class PolyFuzz1A(PolyFuzz1):
    def __init__(self):
        super().__init__()