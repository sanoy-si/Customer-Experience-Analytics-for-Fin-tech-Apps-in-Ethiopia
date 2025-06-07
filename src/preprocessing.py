import pandas as pd

input_csv = "data/raw/ethiopia_fintech_reviews.csv"
df = pd.read_csv(input_csv)
print(f"Original size: {df.shape[0]} rows")


df = df.drop_duplicates()
print(f"After deduplication: {df.shape[0]} rows")

df = df.dropna()
print(f"After dropping missing data: {df.shape[0]} rows")


df['date'] = pd.to_datetime(df['at'], errors='coerce').dt.strftime('%Y-%m-%d')
df = df.dropna(subset=['date'])

df = df.rename(columns={
    'content': 'review',
    'score': 'rating',
    'bank_name': 'bank'
})

df = df.drop(columns=['userName', 'reviewId', 'at'])
df['source'] = 'Google Play'

output_csv = "data/processed/processed_ethiopia_fintech_reviews.csv"
df.to_csv(output_csv, index=False)
print(f"Saved cleaned data to {output_csv}")

