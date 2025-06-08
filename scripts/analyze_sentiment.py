import pandas as pd
from src.sentiment import analyze_sentiment
from src.database import get_engine

if __name__ == "__main__":
    engine = get_engine()
    
    # Load cleaned data from OracleDB
    df = pd.read_sql("SELECT * FROM bank_reviews_cleaned", con=engine)
    
    # Run sentiment analysis
    df = analyze_sentiment(df, text_column="review_text")
    
    # Save result to disk
    df.to_csv("output/sentiment_results.csv", index=False)
    print("✅ Sentiment analysis completed and saved to output/sentiment_results.csv")
