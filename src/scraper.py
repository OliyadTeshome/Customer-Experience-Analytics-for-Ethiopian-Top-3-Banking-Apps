# src/scraper.py

import pandas as pd
from google_play_scraper import reviews, Sort
from src.utils import log_step, format_date

def fetch_reviews_for_app(app_id, app_name, count=400, lang='en', country='us'):
    log_step(f"Fetching reviews for {app_name} ({app_id})...")

    result, _ = reviews(
        app_id,
        lang=lang,
        country=country,
        sort=Sort.NEWEST,
        count=count
    )

    if not result:
        log_step(f"No reviews returned for {app_name} in {lang}-{country}")
        return pd.DataFrame(columns=['review', 'rating', 'date', 'app_name'])

    df = pd.DataFrame(result)[['content', 'score', 'at']]
    df.rename(columns={'content':'review','score':'rating','at':'date'}, inplace=True)
    df['app_name'] = app_name
    df['date'] = df['date'].apply(format_date)
    return df

def fetch_all_reviews(app_dict, count=400):
    all_reviews = []

    for name, app_id in app_dict.items():
        # Try English first, then fallback to Amharic
        df_en = fetch_reviews_for_app(app_id, name, count, lang='en', country='us')
        df_am = fetch_reviews_for_app(app_id, name, count, lang='am', country='et')
        df = pd.concat([df_en, df_am], ignore_index=True)
        all_reviews.append(df)

    combined = pd.concat(all_reviews, ignore_index=True)
    log_step(f"Total reviews fetched: {len(combined)}")
    return combined
