scripts/
├── run_pipeline.py              # 🔁 Full end-to-end pipeline runner
├── scrape_reviews.py            # 🕸️ Just scraping
├── preprocess_reviews.py        # 🧹 Clean, format, save raw data
├── analyze_sentiment.py         # 💬 Apply sentiment model only
├── extract_keywords.py          # 🔑 TF-IDF / spaCy keyword extraction
├── assign_themes.py             # 🧠 Group into themes
├── generate_report.py           # 📊 Visualizations, Excel/CSV export
└── utils_runner.py              # ⚙️ Any helper or combined runner if needed
