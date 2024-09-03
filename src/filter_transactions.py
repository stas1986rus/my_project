import re
from collections import Counter
from typing import Dict, List




def sorting_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """Функция принимает список транзакций (словарей) и слово для сортировки.
    Возвращает список транзакций (словарей), у которых в описании есть указанное слово."""
    new_list = []
    for transaction in transactions:
        if 'description' in transaction and re.findall(search_string, transaction['description']):
            new_list.append(transaction)
    return new_list


def counting_categorys(transactions: List[Dict], categories: List[str]) -> Dict:
    """Функция принимает список транзакций (словарей) и категории (список).
    Возвращает словарь вида категория: количество операций."""
    category_list = []
    for transaction in transactions:
        for category in categories:
            pattern = rf"{category}"
            if re.findall(pattern, transaction["description"], flags=re.IGNORECASE):
                category_list.append(transaction["description"])
    result_category_dict = Counter(category_list)
    return dict(result_category_dict)