# Customer Experience Analytics for Ethiopian Top 3 Banking Apps

## Project Overview

This project collects and analyzes user reviews from the Google Play Store for the top 3 Ethiopian banking apps. It provides insights on customer satisfaction, key pain points, and feature enhancement opportunities to help banks improve their digital user experience.

---

## Objectives

- **Scrape** 400+ user reviews per bank app from the Google Play Store.
- **Preprocess** reviews: clean text, remove duplicates, normalize dates.
- **Analyze Sentiment** using DistilBERT and optionally VADER/TextBlob.
- **Extract Themes** by identifying keywords and grouping feedback into actionable categories.
- **Store** cleaned and enriched review data in an Oracle database.
- **Report** results with visualizations and Excel exports.

- Support business scenarios:
  - Retaining Users
  - Enhancing Features
  - Managing Complaints

---

## Project Structure

```
├── .github/                  # GitHub workflows (CI/CD)
├── .vscode/                  # VSCode settings
├── data/                     # Raw and processed datasets (not tracked in git)
├── outputs/                  # Generated reports and plots
├── scripts/                  # Modular scripts to run parts of the pipeline
│ ├── run_pipeline.py         # Full end-to-end pipeline runner
│ ├── scrape_reviews.py       # Just scraping
│ ├── preprocess_reviews.py   # Clean, format, save raw data
│ ├── analyze_sentiment.py    # Apply sentiment model only
│ ├── extract_keywords.py     # TF-IDF / spaCy keyword extraction
│ ├── assign_themes.py        # Group into themes
│ └── generate_report.py      # Visualizations, Excel/CSV export
├── src/                      # Source modules for each processing step
│ ├── _init_.py
│ ├── scraper.py              # google-play-scraper logic
│ ├── preprocess.py           # cleaning, deduplication, date normalization
│ ├── sentiment.py            # DistilBERT and VADER/TextBlob support
│ ├── keywords.py             # TF-IDF, n-gram, and spaCy keyword extraction
│ ├── themes.py               # Group keywords into themes
│ ├── database.py             # Store the DataFrame into OracleDB
│ └── utils.py
├── tests/                    # Unit tests for src modules
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── .gitignore                # Files/folders to ignore in git
```

## ⚙️ How to Run the Project

1. **Clone the repository:**

```powershell
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```

2. **Create and activate a Python virtual environment:**

```powershell
py -m venv venv
.\venv\Scripts\activate
```

3. **Install required packages:**

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Run the full pipeline:**

```powershell
py scripts\run_pipeline.py
```

## 🧪 Run Tests
```powershell
python -m unittest discover tests
```

# Continuous Integration

- The project uses GitHub Actions to run unit tests on every push/pull request.
- See .github/workflows/unittests.yml for configuration.
- Test results and build status badges can be added to this README for quick visibility.

## 🔌 Dependencies

Key Python packages:
- `google-play-scraper`
- `textblob`, `nltk`
- `pandas`, `numpy`, `matplotlib`, `seaborn`, `wordcloud`
- `sqlalchemy`, `cx_Oracle`
- `openpyxl`

# 📩 Contact
Maintained by Oliyad Teshome – oliyadteshomedida@gmail.com

---
*This project is part of an initiative to apply data engineering and analytics skills to real-world problems in the Ethiopian banking sector.*
