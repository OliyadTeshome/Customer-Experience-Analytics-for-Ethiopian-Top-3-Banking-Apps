import torch
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Explicitly load tokenizer and model
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Create pipeline using PyTorch backend
_sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, framework="pt")

def analyze_sentiment(text):
    """
    Analyze sentiment of a single text using DistilBERT.
    Returns:
        label (str): sentiment label (POSITIVE, NEGATIVE)
        score (float): confidence score
    """
    if not isinstance(text, str) or not text.strip():
        return "NEUTRAL", 0.5  # Return neutral sentiment for empty/None values
        
    result = _sentiment_pipeline(text[:512])[0]
    return result['label'], result['score']

def analyze_sentiments_batch(df, text_col='review_translated'):
    """
    Apply sentiment analysis to a DataFrame in batch.
    Returns:
        pd.DataFrame with sentiment_label and sentiment_score
    """
    sentiments = df[text_col].apply(analyze_sentiment)
    df['sentiment_label'] = sentiments.apply(lambda x: x[0])
    df['sentiment_score'] = sentiments.apply(lambda x: x[1])
    return df
