from transformers import pipeline
import pandas as pd
from tqdm import tqdm

df = pd.read_csv("data/processed/processed_ethiopia_fintech_reviews.csv")

sentiment_pipeline = pipeline()

tqdm.pandas() 
df['sentiment_result'] = df['review'].progress_apply(lambda x: sentiment_pipeline(x)[0])

df['sentiment_label'] = df['sentiment_result'].apply(lambda x: x['label'])
df['sentiment_score'] = df['sentiment_result'].apply(lambda x: x['score'])

df = df.drop(columns=['sentiment_result'])

df.to_csv("data/processed/sentiment_results.csv", index=False)
print("✅ Sentiment analysis done & saved.")
