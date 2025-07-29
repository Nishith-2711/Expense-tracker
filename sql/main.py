from insert import insert_transactions
from query import run_query

def main():
    # Step 1: Insert CSV data
    insert_transactions("data/Statement.csv")

    # Step 2: Run custom queries
    results = run_query("SELECT category, SUM(amount) FROM transactions GROUP BY category")
    for category, total in results:
        print(f"{category}: {total:.2f}")

if __name__ == "__main__":
    main()
