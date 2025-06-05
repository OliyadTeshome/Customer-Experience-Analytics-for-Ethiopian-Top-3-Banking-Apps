### src/sentiment.py
from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    result = sentiment_model(text[:512])[0]  # Truncate for BERT
    label = result['label'].capitalize()
    score = result['score']
    return label, score


def apply_sentiment(df):
    df[['sentiment_label', 'sentiment_score']] = df['review'].apply(lambda x: pd.Series(analyze_sentiment(x)))
    return df