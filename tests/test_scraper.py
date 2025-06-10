# tests/test_scraper.py
import unittest
from unittest.mock import patch
import pandas as pd
from src import scraper

class TestScraper(unittest.TestCase):
    @patch("src.scraper.fetch_reviews_for_app")
    def test_fetch_all_reviews(self, mock_fetch):
        # Setup mock to return a small DataFrame
        mock_df = pd.DataFrame({
            "review": ["Great app", "Needs improvement"],
            "rating": [5, 3],
            "date": ["2025-01-01", "2025-01-02"],
            "app_name": ["TestApp", "TestApp"]
        })
        mock_fetch.return_value = mock_df

        app_dict = {"TestApp": "com.example.testapp"}
        df = scraper.fetch_all_reviews(app_dict, count=10)

        # Check return type
        self.assertIsInstance(df, pd.DataFrame)
        # Check expected columns
        expected_cols = {"review", "rating", "date", "app_name"}
        self.assertTrue(expected_cols.issubset(df.columns))
        # Check mock was called once per app
        expected_calls = [
            call("com.example.testapp", "TestApp", 10, lang='en', country='us'),
            call("com.example.testapp", "TestApp", 10, lang='am', country='et')
        ]
        mock_fetch.assert_has_calls(expected_calls, any_order=True)
        
if __name__ == "__main__":
    unittest.main()
