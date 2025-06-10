from deep_translator import GoogleTranslator
import time
import pandas as pd
from utils import log_step

def translate_reviews(df, review_column='review', new_column='review_translated'):
    """
    Translate reviews from Amharic to English using Google Translate.
    
    Args:
        df (pd.DataFrame): DataFrame containing the reviews
        review_column (str): Name of the column containing reviews to translate
        new_column (str): Name of the column to store translated reviews
        
    Returns:
        pd.DataFrame: DataFrame with added translation column
    """
    log_step("Translating Amharic reviews to English...")
    translator = GoogleTranslator(source='am', target='en')
    
    def translate_text(text):
        try:
            # Add a small delay to avoid hitting rate limits
            time.sleep(0.5)
            # Skip translation if text is empty or None
            if pd.isna(text) or text.strip() == '':
                return text
            # Translate text
            result = translator.translate(text)
            return result
        except Exception as e:
            print(f"Error translating text: {e}")
            return text  # Return original text if translation fails
    
    # Create a new column for translated reviews
    df[new_column] = df[review_column].apply(translate_text)
    
    return df 