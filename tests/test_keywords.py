import unittest
import pandas as pd
from src.keywords import extract_keywords_spacy

class TestKeywordExtraction(unittest.TestCase):
    def test_keywords_output(self):
        test_data = pd.DataFrame({
            "review_id": [1],
            "review_text": ["The banking app is very easy to use and fast."]
        })
        result = extract_keywords_spacy(test_data, text_column="review_text", top_n=3)
        
        self.assertIn("review_id", result.columns)
        self.assertIn("keywords", result.columns)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result.loc[0, "keywords"], str)

if __name__ == "__main__":
    unittest.main()
