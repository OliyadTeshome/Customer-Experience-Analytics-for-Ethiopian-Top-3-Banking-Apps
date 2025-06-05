# scripts/generate_report.py

from src import utils
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

utils.log_step("Loading themed data...")
df = pd.read_csv("data/themed_reviews.csv")

# Plot sentiment distribution
sns.countplot(x="sentiment_label", data=df)
plt.title("Sentiment Distribution")
plt.savefig("outputs/sentiment_distribution.png")
plt.clf()

# Save Excel report
df.to_excel("outputs/final_report.xlsx", index=False)
utils.log_step("Report saved to outputs/final_report.xlsx and sentiment plot saved")