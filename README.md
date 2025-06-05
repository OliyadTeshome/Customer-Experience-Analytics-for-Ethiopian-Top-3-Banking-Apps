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
│ ├── run_pipeline.py
│ ├── scrape_reviews.py
│ ├── preprocess_reviews.py
│ ├── analyze_sentiment.py
│ ├── extract_keywords.py
│ ├── assign_themes.py
│ └── generate_report.py
├── src/                      # Source modules for each processing step
│ ├── scraper.py
│ ├── preprocess.py
│ ├── sentiment.py
│ ├── keywords.py
│ ├── themes.py
│ ├── database.py
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
