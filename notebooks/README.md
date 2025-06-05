# notebooks/

This directory contains modular Jupyter notebooks for interactive exploration and analysis during the project lifecycle.

notebooks/
├── 01_scrape_and_explore.ipynb
├── 02_preprocessing_and_cleaning.ipynb
├── 03_sentiment_and_keywords.ipynb
└── 04_theming_and_reporting.ipynb
---

## 📘 Notebook List

### 1. `1_scrape_and_explore.ipynb`
Purpose: Scrape app reviews and explore the raw data.

**Contents:**
- Import and use src.scraper to fetch reviews.
- Load into DataFrame and preview (head, shape).
- Check language distribution, rating distribution.
- Save to CSV for downstream steps.
---

### 2. `2_preprocessing_and_cleaning.ipynb`
Purpose: Explore data cleaning steps and test preprocessing logic.

**Contents:**
- Load scraped reviews.
- Deduplicate, handle missing values.
- Normalize timestamps (e.g., YYYY-MM-DD).
- Text cleaning: lowercasing, removing emojis, punctuation, etc.
- Save cleaned data.
---

### 3. `3_sentiment_and_keywords.ipynb`
Purpose: Apply sentiment model(s) and extract keywords for thematic analysis.

**Contents:**
- Apply VADER, TextBlob, or DistilBERT sentiment models.
- Visualize sentiment distribution.
- Try TF-IDF or spaCy keyword extraction.
- Print top n-grams, keyword scores.
- Save updated DataFrame.
---

## 4. `4_theming_and_reporting.ipynb`
Purpose: Assign themes and explore insights for business reporting.

""Contents:""
- Group keywords into themes manually or using topic modeling (LDA, etc.).
- Label each review with a theme (rule-based or lookup).
- Visualize:
    - Themes by rating (bar plots)
    - Word clouds
    - Sentiment by theme per bank
- Export charts and final CSV or Excel report.
```

## 📌 Tip
While the `scripts/` folder automates everything end-to-end, the notebooks let you iterate and explore visually during development or presentation.

You can absolutely reuse this notebook documentation in your project `README.md`.