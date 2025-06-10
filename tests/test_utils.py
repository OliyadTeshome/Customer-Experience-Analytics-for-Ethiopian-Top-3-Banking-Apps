# tests/test_utils.py
import unittest
import os
import torch
from src import utils

class TestUtils(unittest.TestCase):
    def test_ensure_dir(self):
        test_dir = "temp_test_dir"
        utils.ensure_dir(test_dir)
        self.assertTrue(os.path.exists(test_dir))
        os.rmdir(test_dir)

    def test_log_step(self):
        utils.log_step("Test message")  # Just to ensure no crash

    def test_model_cache_path(self):
        model_name = "test/model"
        cache_path = utils.get_model_cache_path(model_name)
        expected_path = os.path.join(utils.MODEL_CACHE_DIR, "test--model")
        self.assertEqual(cache_path, expected_path)

    def test_is_model_cached(self):
        # Test with non-existent model
        self.assertFalse(utils.is_model_cached("non_existent_model"))
        
        # Test caching behavior
        test_model = "test_model"
        self.assertFalse(utils.is_model_cached(test_model))
        # Second call should use cache
        self.assertFalse(utils.is_model_cached(test_model))

    def test_device_info(self):
        device_info = utils.get_device_info()
        if torch.cuda.is_available():
            self.assertTrue(device_info.startswith("Using GPU:"))
        else:
            self.assertEqual(device_info, "Using CPU")

    def test_logging_functions(self):
        # Test translation logging
        utils.log_translation(100)
        utils.log_translation(100, source_lang="am")

        # Test sentiment analysis logging
        utils.log_sentiment_analysis(100)
        utils.log_sentiment_analysis(100, translated=True)

        # Test model loading logging
        utils.log_model_loading("test_model", is_cached=False)
        utils.log_model_loading("test_model", is_cached=True)

if __name__ == "__main__":
    unittest.main()