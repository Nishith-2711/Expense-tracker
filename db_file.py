import pandas as pd
import mysql.connector

df = pd.read_csv("data/Statement.csv")
df.columns = df.columns.str.lower()
df['date'] = pd.to_datetime(df['date'] + '/2025', format='%m/%d/%Y')

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="2711",
        database="spend_analyzer"
    )

def insert_data():
    conn = get_connection()
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO transactions (date, merchant, category, amount)
            VALUES (%s, %s, %s, %s)
        """, (
        row['date'].strftime('%Y-%m-%d'), row['merchant'], row['category'],
        row['amount']))
    conn.commit()
    conn.close()
    print("Data inserted.")


def run_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)

    if cursor.description:
        results = cursor.fetchall()
    else:
        results = None
        conn.commit()

    conn.close()
    return results


def main():
    # insert_data()
    rows = run_query("select category, sum(amount) from transactions group by category")

    if rows:
        for row in rows:
            print(row)


if __name__ == "__main__":
    main()