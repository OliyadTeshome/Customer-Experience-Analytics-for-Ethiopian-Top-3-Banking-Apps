import unittest
import pandas as pd
from src import sentiment

class TestSentimentAnalysis(unittest.TestCase):
    def test_sentiment_prediction(self):
        test_data = pd.DataFrame({
            "review_id": [1, 2],
            "review_text": ["I love this app!", "This is the worst experience ever."]
        })
        result = sentiment.analyze_sentiment(test_data, text_column="review_text")
        
        self.assertIn("sentiment_score", result.columns)
        self.assertIn("sentiment_label", result.columns)
        self.assertEqual(len(result), 2)
        self.assertIn(result.loc[0, "sentiment_label"], ["POSITIVE", "NEGATIVE"])
        self.assertIn(result.loc[1, "sentiment_label"], ["POSITIVE", "NEGATIVE"])

if __name__ == "__main__":
    unittest.main()
