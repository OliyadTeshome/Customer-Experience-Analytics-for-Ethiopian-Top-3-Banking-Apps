# scripts/extract_keywords.py

from src import keywords, utils
import pandas as pd

utils.log_step("Loading sentiment reviews...")
df = pd.read_csv("data/sentiment_reviews.csv")

utils.log_step("Extracting keywords...")
keywords_list = keywords.extract_keywords_tfidf(df['review'])
print("Top keywords:", keywords_list)