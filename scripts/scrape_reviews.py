# scripts/scrape_reviews.py

from src import scraper, utils

app_dict = {
    "Bank A": "com.bank.a.app",
    "Bank B": "com.bank.b.app",
    "Bank C": "com.bank.c.app"
}

utils.log_step("Scraping reviews...")
df_raw = scraper.fetch_all_reviews(app_dict)
df_raw.to_csv("data/raw_reviews.csv", index=False)
utils.log_step("Scraping complete. Saved to data/raw_reviews.csv")