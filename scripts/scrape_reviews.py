import pandas as pd
from google_play_scraper import reviews
from src.database import get_engine
from src.utils import log_step

# List of Ethiopian banking apps (replace with actual package names)
APPS = {
    "CBE": "com.cbe.mobilebanking",
    "Dashen": "com.m2i.dashenbank",
    "BOA": "com.boa.mobilebanking"
}

def scrape_app_reviews(app_id, bank_name, count=400):
    result, _ = reviews(
        app_id,
        lang="en",
        country="et",
        count=count,
        filter_score_with=None
    )
    df = pd.DataFrame(result)
    df["bank"] = bank_name
    return df

def clean_reviews(df):
    df = df.rename(columns={
        "reviewId": "review_id",
        "content": "review_text",
        "score": "rating",
        "userName": "user_name",
        "at": "review_date"
    })
    df = df[["review_id", "user_name", "review_text", "rating", "review_date", "bank"]]
    df.drop_duplicates(subset=["review_id"], inplace=True)
    df.dropna(subset=["review_text"], inplace=True)
    return df

if __name__ == "__main__":
    log_step("Starting review scraping...")

    all_reviews = []
    for bank_name, app_id in APPS.items():
        log_step(f"Scraping reviews for {bank_name}...")
        bank_reviews = scrape_app_reviews(app_id, bank_name)
        all_reviews.append(bank_reviews)

    df_all = pd.concat(all_reviews, ignore_index=True)
    df_clean = clean_reviews(df_all)

    # Save to OracleDB
    engine = get_engine()
    df_clean.to_sql("bank_reviews_cleaned", con=engine, if_exists="replace", index=False)

    log_step(f"Scraping complete. {len(df_clean)} reviews saved to OracleDB.")
