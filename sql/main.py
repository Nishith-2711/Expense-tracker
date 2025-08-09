from insert import insert_transactions
from query import run_query

def total_spending():
    total_sum = run_query("Select sum(amount) from transactions")
    return total_sum

def spending_per_category():
    results = run_query("SELECT category, SUM(amount) as sum_per_category FROM transactions "
                        "GROUP BY category")
    return results

def max_transaction():
    results = run_query("Select * from transactions order by amount desc "
                        "limit 1")
    return results

def min_transaction():
    results = run_query("Select * from transactions order by amount limit 1")
    return results

def avg_spending():
    results = run_query("Select avg(amount) as 'average spent' from transactions")

def delete_data():
    results = run_query("delete from transactions")


def main():
    insert_transactions("../data/Statement.csv")


if __name__ == "__main__":
    main()
