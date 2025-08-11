from insert import insert_transactions
from query import run_query
from parser1 import pdf_to_csv

def total_spending():
    total_sum = run_query("Select sum(amount) as 'Total sum' from transactions")
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
    return results

def delete_data():
    results = run_query("delete from transactions")
    return results

def spend_by_month():
    results = run_query("select date_format(date, '%Y-%m') as month, "
                        "sum(amount) as total_spent from transactions group "
                                                         "by month order by "
                                                         "month")
    return results

def main():
    # pdf_to_csv()

    # delete_data()
    pdf_path = r"C:\Codes\Projects\spend_analyzer\data"
    insert_transactions(pdf_path)




if __name__ == "__main__":
    main()
