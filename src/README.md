src/
├── __init__.py
├── scraper.py              # google-play-scraper logic
├── preprocess.py           # cleaning, deduplication, date normalization
├── sentiment.py            # DistilBERT and VADER/TextBlob support
├── keywords.py             # TF-IDF, n-gram, and spaCy keyword extraction
├── themes.py               # Group keywords into themes
├── utils.py                # Logging, file saving, constants