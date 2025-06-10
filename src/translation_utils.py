from googletrans import Translator
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
    translator = Translator()
    
    def translate_text(text):
        try:
            # Add a small delay to avoid hitting rate limits
            time.sleep(0.5)
            result = translator.translate(text, src='am', dest='en')
            return result.text
        except Exception as e:
            print(f"Error translating text: {e}")
            return text  # Return original text if translation fails
    
    # Create a new column for translated reviews
    df[new_column] = df[review_column].apply(translate_text)
    
    return df 