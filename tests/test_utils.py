# tests/test_utils.py
import unittest
import os
from src import utils

class TestUtils(unittest.TestCase):
    def test_ensure_dir(self):
        test_dir = "temp_test_dir"
        utils.ensure_dir(test_dir)
        self.assertTrue(os.path.exists(test_dir))
        os.rmdir(test_dir)

    def test_log_step(self):
        utils.log_step("Test message")  # Just to ensure no crash