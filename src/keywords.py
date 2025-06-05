### src/keywords.py
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

nlp = spacy.load("en_core_web_sm")

def extract_keywords_tfidf(corpus, top_n=10):
    tfidf = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
    X = tfidf.fit_transform(corpus)
    indices = X.sum(axis=0).A1.argsort()[::-1][:top_n]
    keywords = [tfidf.get_feature_names_out()[i] for i in indices]
    return keywords


def spacy_tokenize(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]