# scripts/analyze_sentiment.py

from src import sentiment, utils
import pandas as pd

utils.log_step("Loading cleaned data...")
df = pd.read_csv("data/clean_reviews.csv")

utils.log_step("Running sentiment analysis...")
df_sent = sentiment.apply_sentiment(df)
df_sent.to_csv("data/sentiment_reviews.csv", index=False)
utils.log_step("Saved sentiment-labeled data to data/sentiment_reviews.csv")