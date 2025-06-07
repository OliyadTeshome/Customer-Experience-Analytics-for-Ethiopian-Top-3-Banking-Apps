# tests/test_preprocess.py
import unittest
import pandas as pd
from src import preprocess

class TestPreprocess(unittest.TestCase):
    def test_clean_reviews(self):
        df = pd.DataFrame({"content": ["Great app!!", "Bad UI :("], "rating": [5, 1]})
        df_clean = preprocess.clean_reviews(df)
        self.assertIn("cleaned_review", df_clean.columns)