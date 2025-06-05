# tests/test_scraper.py
import unittest
import pandas as pd
from src import scraper

class TestScraper(unittest.TestCase):
    def test_fetch_all_reviews(self):
        app_dict = {"TestApp": "com.example.testapp"}
        df = scraper.fetch_all_reviews(app_dict, n_reviews=10)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn("review", df.columns)