import pdfplumber
import pandas as pd
import re
import os

def extract_transactions(pdf_path):
    transactions = []

    patterns = [
        {
            "name": "discover",
            "regex": re.compile(r"(\d{2}/\d{2})(?:/\d{4})?\s+(.*?)\s+([A-Za-z ]+)\s+\$([\d,]+\.\d{2})"),
            "groups": ["date", "merchant", "category", "amount"]
        },
        {
            "name": "chase",
            "regex": re.compile(r"(\d{2}/\d{2})\s+(.*?)\s+(-?\d+\.\d{2})$"),
            "groups": ["date", "merchant", "amount"]
        }
    ]

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            for line in text.split("\n"):
                line = line.strip()

                for pattern in patterns:
                    match = pattern["regex"].match(line)
                    if match:
                        data = match.groups()
                        date = data[0]
                        merchant = data[1]
                        if "category" in pattern["groups"]:
                            category = data[2]
                            amount = data[3]
                        else:
                            category = "Uncategorized"
                            amount = data[2]

                        amount = amount.replace(",", "")
                        transactions.append([date, merchant, category, amount])
                        break

    return pd.DataFrame(transactions, columns=["DATE", "MERCHANT", "CATEGORY", "AMOUNT"])

def pdf_to_csv():

    pdf_folder = r"C:\Codes\Projects\spend_analyzer\data"
    for file in os.listdir(pdf_folder):
        if file.lower().endswith(".pdf"):
            pdf_file = os.path.join(pdf_folder, file)

            df = extract_transactions(pdf_file)

            base_name = os.path.splitext(file)[0]
            csv_file = os.path.join(pdf_folder, f"{base_name}.csv")
            df.to_csv(csv_file, index=False)