# import pdfplumber
# import pandas as pd
# import re
#
# def extract_transactions(pdf_path):
#     transactions = []
#
#     with pdfplumber.open(pdf_path) as pdf:
#         for page in pdf.pages:
#             text = page.extract_text()
#             if not text:
#                 continue
#             lines = text.split("\n")
#             for line in lines:
#                 # Match lines like: 06/25 AMAZON.COM XYZ Merchandise $12.34
#                 match = re.match(r"(\d{2}/\d{2})\s+(.*?)\s+([A-Za-z ]+)\s+\$([\d,.]+)", line)
#                 if match:
#                     date = match.group(1)
#                     merchant = match.group(2).strip()
#                     category = match.group(3).strip()
#                     amount = match.group(4).replace(",", "")
#                     transactions.append([date, merchant, category, amount])
#
#     return pd.DataFrame(transactions, columns=["DATE", "MERCHANT", "CATEGORY", "AMOUNT"])
#
# if __name__ == "__main__":
#     pdf_path = "chase_july.pdf"
#     df = extract_transactions(pdf_path)
#     df.to_csv("parsed_transactions.csv", index=False)
#     print("✅ Saved to parsed_transactions.csv")


import pdfplumber
import pandas as pd
import re
import os

def extract_chase_transactions(pdf_path):
    transactions = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            lines = text.split("\n")
            for line in lines:
                # Match lines like: 07/02     Payment Thank You-Mobile -110.40
                match = re.match(r"(\d{2}/\d{2})\s+(.*?)\s+(-?\d+\.\d{2})$", line)
                if match:
                    date = match.group(1)
                    merchant = match.group(2).strip()
                    amount = match.group(3).strip().replace(",", "")
                    category = "Uncategorized"  # You can infer this later if needed
                    transactions.append([date, merchant, category, amount])

    return pd.DataFrame(transactions, columns=["DATE", "MERCHANT", "CATEGORY", "AMOUNT"])

if __name__ == "__main__":
    filename='chase_july.pdf'
    df = extract_chase_transactions(filename)
    base_name = os.path.splitext(os.path.basename(filename))[0]
    csv_file = f"{base_name}.csv"
    df.to_csv(csv_file, index=False)
    print("Transactions saved to chase_transactions.csv")
