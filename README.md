# Customer Experience Analytics for Ethiopian Top 3 Banking Apps

## 📊 Project Overview

This project analyzes user reviews from the Google Play Store for Ethiopia's top three banking applications:
- Commercial Bank of Ethiopia
- Bank of Abyssinia (BoA Mobile)
- Dashen Bank

The analysis provides actionable insights on customer satisfaction, key pain points, and feature enhancement opportunities to help banks improve their digital user experience.

## 🎯 Key Objectives

- **Data Collection**: Scrape 400+ user reviews per banking app from Google Play Store
- **Text Processing**: 
  - Clean and preprocess reviews
  - Remove duplicates
  - Normalize dates
  - Translate non-English reviews
- **Sentiment Analysis**: 
  - Implement DistilBERT for sentiment classification
  - Support for VADER/TextBlob as alternatives
  - Handle multiple languages including Amharic
- **Theme Extraction**: 
  - Identify key topics and themes
  - Group feedback into actionable categories
- **Data Storage**: Store processed data in Oracle database
- **Reporting**: Generate visualizations and Excel exports

## 📁 Project Structure

```
├── .github/                  # GitHub workflows (CI/CD)
├── .vscode/                  # VSCode settings
├── data/                     # Raw and processed datasets (gitignored)
├── notebooks/               # Jupyter notebooks for analysis
│   ├── 1_scrape_and_explore.ipynb
│   ├── 2_preprocessing_and_cleaning.ipynb
│   ├── 3_sentiment_and_keywords.ipynb
│   └── 4_theming_and_reporting.ipynb
├── outputs/                 # Generated reports and plots
├── scripts/                 # Modular pipeline scripts
│   ├── run_pipeline.py      # End-to-end pipeline
│   ├── scrape_reviews.py    # Review collection
│   ├── preprocess_reviews.py # Data cleaning
│   ├── analyze_sentiment.py # Sentiment analysis
│   ├── extract_keywords.py  # Keyword extraction
│   ├── assign_themes.py     # Theme assignment
│   └── generate_report.py   # Report generation
├── src/                     # Core modules
│   ├── scraper.py          # Google Play scraper
│   ├── preprocess.py       # Data cleaning
│   ├── sentiment.py        # Sentiment analysis
│   ├── keywords.py         # Keyword extraction
│   ├── themes.py           # Theme grouping
│   ├── database.py         # Oracle DB operations
│   └── utils.py            # Helper functions
├── tests/                   # Unit tests
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Oracle Database
- Google Play Store API access

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/customer-experience-analytics.git
cd customer-experience-analytics
```

2. **Create and activate virtual environment:**
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure database:**
- Set up Oracle database credentials in environment variables
- Create required tables using scripts in `src/database.py`

### Running the Analysis

1. **Full pipeline:**
```bash
python scripts/run_pipeline.py
```

2. **Individual components:**
```bash
# Scrape reviews
python scripts/scrape_reviews.py

# Preprocess data
python scripts/preprocess_reviews.py

# Analyze sentiment
python scripts/analyze_sentiment.py

# Generate report
python scripts/generate_report.py
```

3. **Interactive analysis:**
- Open Jupyter notebooks in `notebooks/` directory
- Follow numbered sequence for step-by-step analysis

## 📊 Key Findings

- **Sentiment Distribution:**
  - Dashen Bank shows highest positive sentiment (1330 positive reviews)
  - Commercial Bank of Ethiopia maintains balanced sentiment
  - BoA Mobile has higher negative sentiment (1163 negative reviews)

- **Common Themes:**
  - User Experience
  - Banking & Transactions
  - App Identity
  - Technical Issues
  - Customer Service

## ⚠️ Limitations

- **Data Collection:**
  - Limited to Google Play Store reviews
  - Excludes iOS users
  - May underrepresent non-reviewing users

- **Analysis:**
  - Translation challenges for Amharic reviews
  - Cultural context may be lost
  - Binary sentiment classification may oversimplify feedback

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Oliyad Teshome** - *Initial work* - [Email](mailto:oliyadteshomedida@gmail.com)

## 🙏 Acknowledgments

- 10 Academy for project support
- Ethiopian banking sector stakeholders
- Open source community for tools and libraries

---

*This project is part of an initiative to apply data science and analytics skills to real-world problems in the Ethiopian banking sector.*

