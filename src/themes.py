### src/themes.py
THEME_KEYWORDS = {
    'Account Access Issues': ["login", "otp", "crash", "freeze"],
    'Transaction Performance': ["transfer", "delay", "transaction", "send"],
    'User Interface & Experience': ["ui", "design", "navigation", "layout"],
    'Customer Support': ["support", "help", "response", "service"],
    'Feature Requests': ["feature", "add", "option", "customize"]
}

def assign_theme(review):
    for theme, keywords in THEME_KEYWORDS.items():
        if any(word in review.lower() for word in keywords):
            return theme
    return "Other"


def apply_themes(df):
    df['theme'] = df['review'].apply(assign_theme)
    return df