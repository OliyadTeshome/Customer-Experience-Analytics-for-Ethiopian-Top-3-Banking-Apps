# src/translate.py

from deep_translator import GoogleTranslator
from src.utils import log_step
<<<<<<< HEAD

def translate_to_english(text):
    """
    Translates input text to English using Google Translate.

    Args:
        text (str): Original text (could be in Amharic or English).

    Returns:
        str: Translated text in English.
=======
import time
from typing import Optional, Dict
import pandas as pd
from functools import lru_cache

# Rate limiting settings
RATE_LIMIT_DELAY = 1  # seconds between translations
MAX_RETRIES = 3
CACHE_SIZE = 1000  # Number of translations to cache

@lru_cache(maxsize=CACHE_SIZE)
def translate_to_english(text: str, retry_count: int = 0) -> str:
    """
    Translates input text to English using Google Translate with rate limiting and caching.

    Args:
        text (str): Original text (could be in Amharic or English)
        retry_count (int): Number of retry attempts made

    Returns:
        str: Translated text in English
>>>>>>> Task-2
    """
    if not isinstance(text, str) or text.strip() == "":
        return ""

<<<<<<< HEAD
    try:
        translated = GoogleTranslator(source='auto', target='en').translate(text)
        return translated
    except Exception as e:
        log_step(f"Translation failed: {e}")
        return text  # fallback to original text on failure

def translate_column(df, column="review_text"):
    """
    Apply translation to an entire DataFrame column.

    Args:
        df (pd.DataFrame): DataFrame with review text.
        column (str): Column to translate.

    Returns:
        pd.Series: Series of translated texts.
    """
    log_step("Translating text to English...")
    return df[column].apply(translate_to_english)
=======
    # Check if text is already in English (simple heuristic)
    if all(ord(c) < 128 for c in text):
        return text

    try:
        # Rate limiting
        time.sleep(RATE_LIMIT_DELAY)
        
        translated = GoogleTranslator(source='auto', target='en').translate(text)
        if translated:
            log_step(f"Successfully translated text: {text[:50]}...")
            return translated
        return text

    except Exception as e:
        if retry_count < MAX_RETRIES:
            log_step(f"Translation attempt {retry_count + 1} failed: {str(e)}", level='warning')
            time.sleep(RATE_LIMIT_DELAY * (retry_count + 1))  # Exponential backoff
            return translate_to_english(text, retry_count + 1)
        else:
            log_step(f"Translation failed after {MAX_RETRIES} attempts: {str(e)}", level='error')
            return text

def translate_column(df: pd.DataFrame, column: str = "review_text", batch_size: int = 100) -> pd.Series:
    """
    Apply translation to a DataFrame column with batching for better performance.

    Args:
        df (pd.DataFrame): DataFrame with review text
        column (str): Column to translate
        batch_size (int): Number of rows to process in each batch

    Returns:
        pd.Series: Series of translated texts
    """
    log_step(f"Starting translation of {len(df)} rows in batches of {batch_size}...")
    
    translated_texts = []
    for i in range(0, len(df), batch_size):
        batch = df[column].iloc[i:i + batch_size]
        batch_translations = batch.apply(translate_to_english)
        translated_texts.extend(batch_translations)
        log_step(f"Translated batch {i//batch_size + 1}/{(len(df) + batch_size - 1)//batch_size}")
    
    return pd.Series(translated_texts, index=df.index)

def clear_translation_cache() -> None:
    """Clears the translation cache."""
    translate_to_english.cache_clear()
    log_step("Translation cache cleared")
>>>>>>> Task-2
