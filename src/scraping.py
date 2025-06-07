from google_play_scraper import reviews, Sort
import pandas as pd
import time

# List of app IDs
apps = {
    'CBE': 'com.combanketh.mobilebanking',
    'BOA': 'com.boa.boaMobileBanking',
    'Dashen': 'com.dashen.dashensuperapp'
}


all_reviews = pd.DataFrame()

for bank_name, app_id in apps.items():
    print(f"Scraping reviews for {bank_name}...")
    
    bank_reviews = []
    count = 0
    batch_size = 200 

    while count < 400:
        result, _ = reviews(
            app_id,
            lang='en',
            country='ET',
            sort=Sort.NEWEST,
            count=batch_size,
            continuation_token=None if count == 0 else continuation_token
        )
        
        bank_reviews.extend(result)
        
        count += len(result)
        print(f"Fetched {count} reviews so far for {bank_name}...")
        
        if len(result) < batch_size:
            break
        
        continuation_token = _

        time.sleep(1)
    
    df_bank = pd.DataFrame(bank_reviews)
    df_bank['bank_name'] = bank_name

    all_reviews = pd.concat([all_reviews, df_bank], ignore_index=True)

all_reviews[['bank_name', 'userName', 'content', 'score', 'at', 'reviewId']].to_csv('data/raw/ethiopia_fintech_reviews.csv', index=False)

print("Scraping completed! Data saved to ethiopia_fintech_reviews.csv")
