import pandas as pd
from src.database import get_engine
from src.sentiment import analyze_sentiment
from src.keywords import extract_keywords_spacy
from src.themes import assign_themes  # assuming you put theme logic here
import os

if __name__ == "__main__":
    engine = get_engine()
    
    print("🔹 Loading data from OracleDB...")
    df = pd.read_sql("SELECT * FROM bank_reviews_cleaned", con=engine)

    print("🔹 Running Sentiment Analysis...")
    df = analyze_sentiment(df, text_column="review_text")

    print("🔹 Extracting Keywords...")
    keywords_df = extract_keywords_spacy(df, text_column="review_text", top_n=5)
    df = df.merge(keywords_df[["review_id", "keywords"]], on="review_id", how="left")

    print("🔹 Assigning Themes...")
    df = assign_themes(df)  # your rule-based logic

    print("🔹 Saving output to output/final_analysis.csv")
    os.makedirs("output", exist_ok=True)
    df[["review_id", "review_text", "sentiment_score", "sentiment_label", "keywords", "themes"]].to_csv(
        "output/final_analysis.csv", index=False
    )

    print("✅ Pipeline complete!")
