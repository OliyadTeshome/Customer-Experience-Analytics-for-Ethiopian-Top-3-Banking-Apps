# tests/test_sentiment.py
import unittest
import pandas as pd
from src import sentiment

class TestSentiment(unittest.TestCase):
    def test_apply_sentiment(self):
        df = pd.DataFrame({"review": ["Awesome app", "Horrible experience"]})
        df_sent = sentiment.apply_sentiment(df)
        self.assertIn("sentiment_label", df_sent.columns)