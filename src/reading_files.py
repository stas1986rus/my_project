import csv

import pandas as pd


def reader_file_transaction_csv(file):
    """Функция считывающая cvs файл и возвращающая список словарей"""
    with open(file, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        header = next(reader)
        result = []
        for row in reader:
            row_dict = {
                "id": row[header.index("id")],
                "state": row[header.index("state")],
                "date": row[header.index("date")],
                "operationAmount": {
                    "amount": row[header.index("amount")],
                    "currency": {
                        "name": row[header.index("currency_name")],
                        "code": row[header.index("currency_code")],
                    },
                },
                "description": row[header.index("description")],
                "from": row[header.index("from")],
                "to": row[header.index("to")],
            }
            result.append(row_dict)

    return result


# if __name__ == "__main__":
#     result = reader_file_transaction_csv("../data/transactions.csv")
#     print(result)


def reader_file_transaction_excel(file):
    """Функция считывающая файл в формате excel и возвращающая список словарей"""
    df = pd.read_excel(file)  # читаем из экселя в DataFrame
    result = []
    rows_count = len(df)  # Получение количества строк в DataFrame
    for i in range(0, rows_count):
        row_dict = {
            "id": df.at[i, "id"],
            "state": df.at[i, "state"],
            "date": df.at[i, "date"],
            "operationAmount": {
                "amount": df.at[i, "amount"],
                "currency": {
                    "name": df.at[i, "currency_name"],
                    "code": df.at[i, "currency_code"],
                },
            },
            "description": df.at[i, "description"],
            "from": df.at[i, "from"],
            "to": df.at[i, "to"],
        }
        result.append(row_dict)
    return result


# if __name__ == "__main__":
#     result = reader_file_transaction_excel("../data/transactions_excel.xlsx")
#     print(result)
