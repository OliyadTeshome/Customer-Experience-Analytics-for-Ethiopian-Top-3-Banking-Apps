import torch
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from typing import Tuple, List, Dict, Optional
from src.utils import log_step
from functools import lru_cache
import numpy as np

# Model configuration
MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"
MAX_LENGTH = 512
BATCH_SIZE = 32
CACHE_SIZE = 1000

# Initialize model and tokenizer
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    _sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model=model,
        tokenizer=tokenizer,
        framework="pt",
        device=0 if torch.cuda.is_available() else -1
    )
    log_step("Successfully loaded sentiment analysis model")
except Exception as e:
    log_step(f"Failed to load sentiment analysis model: {str(e)}", level='error')
    raise

@lru_cache(maxsize=CACHE_SIZE)
def analyze_sentiment(text: str) -> Tuple[str, float]:
    """
    Analyze sentiment of a single text using DistilBERT with caching.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        Tuple[str, float]: (sentiment label, confidence score)
    """
    if not isinstance(text, str) or not text.strip():
        return "NEUTRAL", 0.0
        
    try:
        # Truncate text to max length
        truncated_text = text[:MAX_LENGTH]
        result = _sentiment_pipeline(truncated_text)[0]
        return result['label'], result['score']
    except Exception as e:
        log_step(f"Sentiment analysis failed for text: {text[:50]}... Error: {str(e)}", level='error')
        return "NEUTRAL", 0.0

def analyze_sentiments_batch(
    df: pd.DataFrame,
    text_col: str = 'review',
    batch_size: int = BATCH_SIZE
) -> pd.DataFrame:
    """
    Apply sentiment analysis to a DataFrame in batches for better performance.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        text_col (str): Name of the column containing text to analyze
        batch_size (int): Number of texts to process in each batch
        
    Returns:
        pd.DataFrame: DataFrame with added sentiment_label and sentiment_score columns
    """
    if text_col not in df.columns:
        raise ValueError(f"Column '{text_col}' not found in DataFrame")
        
    log_step(f"Starting batch sentiment analysis on {len(df)} rows...")
    
    # Process in batches
    sentiments = []
    for i in range(0, len(df), batch_size):
        batch = df[text_col].iloc[i:i + batch_size]
        batch_sentiments = batch.apply(analyze_sentiment)
        sentiments.extend(batch_sentiments)
        log_step(f"Processed batch {i//batch_size + 1}/{(len(df) + batch_size - 1)//batch_size}")
    
    # Convert results to DataFrame columns
    df['sentiment_label'] = [s[0] for s in sentiments]
    df['sentiment_score'] = [s[1] for s in sentiments]
    
    # Add sentiment distribution statistics
    sentiment_counts = df['sentiment_label'].value_counts()
    log_step(f"Sentiment distribution: {dict(sentiment_counts)}")
    
    return df

def get_sentiment_stats(df: pd.DataFrame) -> Dict:
    """
    Calculate sentiment analysis statistics.
    
    Args:
        df (pd.DataFrame): DataFrame with sentiment_label and sentiment_score columns
        
    Returns:
        Dict: Dictionary containing sentiment statistics
    """
    if 'sentiment_label' not in df.columns or 'sentiment_score' not in df.columns:
        raise ValueError("DataFrame must contain 'sentiment_label' and 'sentiment_score' columns")
        
    stats = {
        'total_reviews': len(df),
        'sentiment_distribution': df['sentiment_label'].value_counts().to_dict(),
        'average_score': df['sentiment_score'].mean(),
        'score_std': df['sentiment_score'].std(),
        'score_median': df['sentiment_score'].median()
    }
    
    return stats

def clear_sentiment_cache() -> None:
    """Clears the sentiment analysis cache."""
    analyze_sentiment.cache_clear()
    log_step("Sentiment analysis cache cleared")
