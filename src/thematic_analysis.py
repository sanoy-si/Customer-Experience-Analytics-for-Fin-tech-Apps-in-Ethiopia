from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

df = pd.read_csv("data/processed/sentiment_results.csv")
banks = df['bank'].unique()

for bank in banks:
    print(f"👉 Extracting keywords for {bank}")
    bank_df = df[df['bank'] == bank]

    vectorizer = TfidfVectorizer(max_features=20, ngram_range=(1,2), stop_words='english')
    X = vectorizer.fit_transform(bank_df['review'])

    keywords = vectorizer.get_feature_names_out()

    with open(f"data/processed/{bank.replace(' ', '_')}_keywords.txt", "w") as f:
        for kw in keywords:
            f.write(kw + "\n")

    print(f"✅ Keywords saved for {bank}")
