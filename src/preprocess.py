### src/preprocess.py
import pandas as pd

def clean_reviews(df):
    df = df.drop_duplicates(subset='content')
    df = df.dropna(subset=['content', 'score', 'at'])
    df['date'] = pd.to_datetime(df['at']).dt.date
    df['date'] = df['date'].astype(str)
    df = df.rename(columns={
        'content': 'review',
        'score': 'rating'
    })
    return df[['reviewId', 'review', 'rating', 'date', 'bank', 'source']]


def save_clean_reviews(df, path='data/clean_reviews.csv'):
    df.to_csv(path, index=False)