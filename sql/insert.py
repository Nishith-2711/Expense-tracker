import pandas as pd
from connection import get_connection
import os

def insert_transactions(folder_path):
    conn = get_connection()
    cursor = conn.cursor()

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(".csv"):
            csv_path = os.path.join(folder_path, file_name)
            df = pd.read_csv(csv_path)

            df.columns = df.columns.str.lower()

            df['date'] = pd.to_datetime(df['date'] + '/2025', format='%m/%d/%Y')
            for _, row in df.iterrows():
                cursor.execute("""
                    INSERT INTO transactions (date, merchant, category, amount)
                    VALUES (%s, %s, %s, %s)
                """, (row['date'].strftime('%Y-%m-%d'), row['merchant'], row['category'], row['amount']))

    conn.commit()
    conn.close()
