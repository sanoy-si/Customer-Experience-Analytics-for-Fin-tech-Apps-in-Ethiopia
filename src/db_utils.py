import oracledb
import pandas as pd

conn = oracledb.connect(user='system', password='oracle', dsn='localhost/XE')
cur = conn.cursor()

df = pd.read_csv('data/processed/processed_ethiopia_fintech_reviews.csv')

banks = df['bank'].unique()
for bank in banks:
    try:
        cur.execute("INSERT INTO Banks (bank_name) VALUES (:1)", [bank])
    except oracledb.DatabaseError:
        pass

conn.commit()

cur.execute("SELECT bank_id, bank_name FROM Banks")
bank_id_map = {name: id for (id, name) in cur.fetchall()}

for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO Reviews (review, rating, review_date, bank_id, source)
        VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4, :5)
    """, (row['review'], row['rating'], row['date'], bank_id_map[row['bank']], row['source']))

conn.commit()
cur.close()
conn.close()
