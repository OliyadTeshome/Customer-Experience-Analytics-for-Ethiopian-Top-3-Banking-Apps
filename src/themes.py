def get_theme_mapping():
    return {
        "User Experience": [
            "user", "friendly", "user friendly", "easy", "easy use", "good", "great",
            "nice", "like", "super", "amazing", "experience", "best", "best app",
            "good app", "super app", "better", "using"
        ],
        "App Performance": [
            "work", "working", "fix", "doesn", "don", "update", "reliable", "fast",
            "time", "developer", "worst"
        ],
        "Banking & Transactions": [
            "bank", "banking", "mobile banking", "banking app", "money", "transaction",
            "transactions", "digital"
        ],
        "App Identity": [
            "dashen", "cbe", "boa", "dashen bank", "apps", "application", "mobile", "app"
        ],
        "Feature Requests": [
            "features", "need", "make"
        ],
        "Other": [
            "ነው"
        ]
    }

def assign_themes_to_keywords(keywords_df):
    theme_map = get_theme_mapping()
    assigned_themes = []

    for keyword in keywords_df['keyword']:
        found = False
        for theme, words in theme_map.items():
            if keyword.lower() in words:
                assigned_themes.append(theme)
                found = True
                break
        if not found:
            assigned_themes.append("Other")

    keywords_df['theme'] = assigned_themes
    return keywords_df
