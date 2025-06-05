# scripts/assign_themes.py

from src import themes, utils
import pandas as pd

utils.log_step("Loading sentiment reviews...")
df = pd.read_csv("data/sentiment_reviews.csv")

utils.log_step("Applying themes...")
df_themed = themes.apply_themes(df)
df_themed.to_csv("data/themed_reviews.csv", index=False)
utils.log_step("Saved themed data to data/themed_reviews.csv")