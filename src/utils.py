import json
from typing import Any

def get_transactions_dictionary(path: str) -> dict | Any:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(path, "r", encoding="utf-8") as operations:
            try:
                list_trans = json.load(operations)
                return list_trans
            except json.JSONDecodeError:
                list_trans = []
                return list_trans
    except FileNotFoundError:
        list_trans = []
        return list_trans
