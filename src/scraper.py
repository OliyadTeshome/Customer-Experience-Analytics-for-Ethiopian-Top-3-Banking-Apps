### src/scraper.py
from google_play_scraper import reviews
import pandas as pd

def fetch_reviews(app_id, bank_name, count=400):
    result, _ = reviews(app_id, lang='en', country='us', count=count)
    data = pd.DataFrame(result)
    data['bank'] = bank_name
    data['source'] = 'Google Play'
    return data[['reviewId', 'content', 'score', 'at', 'bank', 'source']]


def fetch_all_reviews(app_dict):
    frames = []
    for bank, app_id in app_dict.items():
        df = fetch_reviews(app_id, bank)
        frames.append(df)
    return pd.concat(frames, ignore_index=True)