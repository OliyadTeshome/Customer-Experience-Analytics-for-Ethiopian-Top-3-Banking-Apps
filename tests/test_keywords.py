# tests/test_keywords.py
import unittest
import pandas as pd
from src import keywords

class TestKeywords(unittest.TestCase):
    def test_extract_keywords_tfidf(self):
        sample_reviews = ["Fast transfer and easy UI", "Slow login and crashes"]
        df = pd.DataFrame({"review": sample_reviews})
        words = keywords.extract_keywords_tfidf(df["review"])
        self.assertTrue(len(words) > 0)