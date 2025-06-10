# src/keywords.py

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def extract_keywords_tfidf(df, text_column='review', max_features=50, ngram_range=(1, 2)):
    """
    Extract top keywords using TF-IDF.
    
    Args:
        df (pd.DataFrame): DataFrame with review text.
        text_column (str): Column containing the review text.
        max_features (int): Max number of keywords.
        ngram_range (tuple): n-gram range, e.g., (1,2) for unigrams and bigrams.

    Returns:
        pd.DataFrame: Keywords and TF-IDF scores.
    """
    # Handle None values and non-string values by converting to empty strings
    texts = df[text_column].astype(str).replace('None', '').replace('nan', '')
    
    # Remove any empty strings
    texts = texts[texts.str.strip().str.len() > 0]
    
    if len(texts) == 0:
        return pd.DataFrame({'keyword': [], 'score': []})
    
    tfidf = TfidfVectorizer(stop_words='english', max_features=max_features, ngram_range=ngram_range)
    tfidf_matrix = tfidf.fit_transform(texts)
    feature_names = tfidf.get_feature_names_out()

    tfidf_scores = tfidf_matrix.sum(axis=0).A1
    keywords_df = pd.DataFrame({'keyword': feature_names, 'score': tfidf_scores})
    keywords_df = keywords_df.sort_values(by='score', ascending=False)

    return keywords_df
