# tests/test_themes.py
import unittest
import pandas as pd
from src import themes

class TestThemes(unittest.TestCase):
    def test_apply_themes(self):
        df = pd.DataFrame({"review": ["The UI is slow", "Login issues"]})
        df_themes = themes.apply_themes(df)
        self.assertIn("theme", df_themes.columns)