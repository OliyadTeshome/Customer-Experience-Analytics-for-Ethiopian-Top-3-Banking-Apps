# src/translate.py

from deep_translator import GoogleTranslator
from src.utils import log_step

def translate_to_english(text):
    """
    Translates input text to English using Google Translate.

    Args:
        text (str): Original text (could be in Amharic or English).

    Returns:
        str: Translated text in English.
    """
    if not isinstance(text, str) or text.strip() == "":
        return ""

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