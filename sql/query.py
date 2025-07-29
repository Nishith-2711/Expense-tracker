from connection import get_connection

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
