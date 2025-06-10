import torch
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from transformers import MarianMTModel, MarianTokenizer
from . import utils

# Log device information
utils.log_step(utils.get_device_info())

# Translation model setup
translation_model_name = "Helsinki-NLP/opus-mt-mul-en"  # Multilingual to English model
utils.log_model_loading(translation_model_name, utils.is_model_cached(translation_model_name))
translation_tokenizer = MarianTokenizer.from_pretrained(translation_model_name)
translation_model = MarianMTModel.from_pretrained(translation_model_name)

# Sentiment model setup
sentiment_model_name = "distilbert-base-uncased-finetuned-sst-2-english"
utils.log_model_loading(sentiment_model_name, utils.is_model_cached(sentiment_model_name))
tokenizer = AutoTokenizer.from_pretrained(sentiment_model_name)
model = AutoModelForSequenceClassification.from_pretrained(sentiment_model_name)

# Create pipeline using PyTorch backend
_sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, framework="pt")

def translate_to_english(text):
    """
    Translate text to English using MarianMT model.
    Args:
        text (str): Input text in any supported language
    Returns:
        str: Translated English text
    """
    utils.log_translation(len(text))
    # Tokenize and translate
    inputs = translation_tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    translated = translation_model.generate(**inputs)
    translated_text = translation_tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

def analyze_sentiment(text, translate=True):
    """
    Analyze sentiment of a single text using DistilBERT.
    Args:
        text (str): Input text
        translate (bool): Whether to translate non-English text to English first
    Returns:
        label (str): sentiment label (POSITIVE, NEGATIVE)
        score (float): confidence score
    """
    if translate:
        text = translate_to_english(text)
        utils.log_sentiment_analysis(len(text), translated=True)
    else:
        utils.log_sentiment_analysis(len(text), translated=False)
    
    result = _sentiment_pipeline(text[:512])[0]
    return result['label'], result['score']

def analyze_sentiments_batch(df, text_col='review', translate=True):
    """
    Apply sentiment analysis to a DataFrame in batch.
    Args:
        df (pd.DataFrame): Input DataFrame
        text_col (str): Column name containing text to analyze
        translate (bool): Whether to translate non-English text to English first
    Returns:
        pd.DataFrame with sentiment_label and sentiment_score
    """
    utils.log_step(f"Processing batch of {len(df)} reviews")
    sentiments = df[text_col].apply(lambda x: analyze_sentiment(x, translate=translate))
    df['sentiment_label'] = sentiments.apply(lambda x: x[0])
    df['sentiment_score'] = sentiments.apply(lambda x: x[1])
    utils.log_step("Batch processing completed")
    return df
