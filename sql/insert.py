import pandas as pd
from connection import get_connection

def insert_transactions(csv_path):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.lower()
    df['date'] = pd.to_datetime(df['date'] + '/2025', format='%m/%d/%Y')

    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO transactions (date, merchant, category, amount)
            VALUES (%s, %s, %s, %s)
        """, (row['date'].strftime('%Y-%m-%d'), row['merchant'], row['category'], row['amount']))

    conn.commit()
    conn.close()
