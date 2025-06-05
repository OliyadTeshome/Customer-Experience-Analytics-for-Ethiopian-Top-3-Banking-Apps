# scripts/run_pipeline.py

from src import scraper, preprocess, sentiment, keywords, themes, utils
import pandas as pd

# Step 0: Setup
data_path = "data"
utils.ensure_dir(data_path)

# Step 1: Scrape reviews
app_dict = {
    "Bank A": "com.bank.a.app",
    "Bank B": "com.bank.b.app",
    "Bank C": "com.bank.c.app"
}

utils.log_step("Scraping reviews from Google Play Store...")
df_raw = scraper.fetch_all_reviews(app_dict)

# Step 2: Preprocess
utils.log_step("Cleaning and preprocessing data...")
df_clean = preprocess.clean_reviews(df_raw)
preprocess.save_clean_reviews(df_clean, f"{data_path}/clean_reviews.csv")

# Step 3: Sentiment Analysis
utils.log_step("Applying sentiment analysis...")
df_sentiment = sentiment.apply_sentiment(df_clean)

# Step 4: Keyword Extraction
utils.log_step("Extracting keywords...")
keywords_list = keywords.extract_keywords_tfidf(df_sentiment['review'])
utils.log_step(f"Top keywords: {keywords_list}")

# Step 5: Theme Assignment
utils.log_step("Assigning themes...")
df_themed = themes.apply_themes(df_sentiment)

# Step 6: Save Final Output
output_path = f"{data_path}/final_reviews.csv"
df_themed.to_csv(output_path, index=False)
utils.log_step(f"Pipeline complete. Final output saved to {output_path}")