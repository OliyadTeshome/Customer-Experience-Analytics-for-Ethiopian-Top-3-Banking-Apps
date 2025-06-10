import unittest
import pandas as pd
from src import sentiment

class TestSentimentAnalysis(unittest.TestCase):
    def test_single_sentiment_prediction(self):
        # Test English text
        label, score = sentiment.analyze_sentiment("I love this app!", translate=False)
        self.assertIn(label, ["POSITIVE", "NEGATIVE"])
        self.assertIsInstance(score, float)
        self.assertTrue(0 <= score <= 1)

        # Test non-English text with translation
        label, score = sentiment.analyze_sentiment("አፕሊኬሽኑ በጣም ጥሩ ነው!", translate=True)  # "The app is very good!" in Amharic
        self.assertIn(label, ["POSITIVE", "NEGATIVE"])
        self.assertIsInstance(score, float)
        self.assertTrue(0 <= score <= 1)

    def test_batch_sentiment_prediction(self):
        test_data = pd.DataFrame({
            "review_id": [1, 2],
            "review_text": ["I love this app!", "This is the worst experience ever."]
        })
        
        # Test without translation
        result = sentiment.analyze_sentiments_batch(test_data, text_col="review_text", translate=False)
        self.assertIn("sentiment_score", result.columns)
        self.assertIn("sentiment_label", result.columns)
        self.assertEqual(len(result), 2)
        self.assertIn(result.loc[0, "sentiment_label"], ["POSITIVE", "NEGATIVE"])
        self.assertIn(result.loc[1, "sentiment_label"], ["POSITIVE", "NEGATIVE"])

        # Test with translation
        test_data_mixed = pd.DataFrame({
            "review_id": [1, 2],
            "review_text": ["I love this app!", "አፕሊኬሽኑ በጣም መልካም ነው!"]  # Mixed English and Amharic
        })
        result_translated = sentiment.analyze_sentiments_batch(test_data_mixed, text_col="review_text", translate=True)
        self.assertIn("sentiment_score", result_translated.columns)
        self.assertIn("sentiment_label", result_translated.columns)
        self.assertEqual(len(result_translated), 2)
        self.assertIn(result_translated.loc[0, "sentiment_label"], ["POSITIVE", "NEGATIVE"])
        self.assertIn(result_translated.loc[1, "sentiment_label"], ["POSITIVE", "NEGATIVE"])

    def test_translation(self):
        # Test translation function directly
        amharic_text = "አፕሊኬሽኑ በጣም ጥሩ ነው!"  # "The app is very good!" in Amharic
        translated = sentiment.translate_to_english(amharic_text)
        self.assertIsInstance(translated, str)
        self.assertTrue(len(translated) > 0)

if __name__ == "__main__":
    unittest.main()
