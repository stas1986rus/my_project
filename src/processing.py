from typing import Any


def filter_by_state(operations: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей и опционально значение для ключа
    state и возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.
    """
    filtered_operations = []
    for key in operations:
        if key.get("state") == state:
            filtered_operations.append(key)
    return filtered_operations


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция принимает на вход список словарей и возвращает новый список, в котором исходные
    словари отсортированы по убыванию даты
    """
    operations = sorted(operations, key=lambda new_list_of_dict: new_list_of_dict["date"], reverse=reverse)
    return operations
