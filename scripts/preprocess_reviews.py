# scripts/preprocess_reviews.py

from src import preprocess, utils
import pandas as pd

utils.log_step("Loading raw reviews...")
df = pd.read_csv("data/raw_reviews.csv")

utils.log_step("Cleaning reviews...")
df_clean = preprocess.clean_reviews(df)
df_clean.to_csv("data/clean_reviews.csv", index=False)
utils.log_step("Saved cleaned data to data/clean_reviews.csv")