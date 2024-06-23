from typing import Union

from polyfuzz1.models import TFIDF, BaseMatcher


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

        return self