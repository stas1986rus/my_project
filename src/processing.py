from typing import Any


def filter_by_state(list_of_dictionaries: Any, status="EXECUTED") -> list:
    """Функция возвращает новый список, содержащий только те словари, у которых ключ
    status содержит переданное в функцию значение, по умолчанию значение EXECUTED"""

    new_list = []
    for dictionaries in list_of_dictionaries:
        if dictionaries.get("state") == status:
            new_list.append(dictionaries)
    return new_list


def sort_by_date(list_of_dictionaries: Any, reverse_list=True) -> list:
    """Функция сортировки по дате, поумолчанию от большего к меньшему"""
    sorted_list = sorted(list_of_dictionaries, key=lambda d: d["date"], reverse=reverse_list)
    return sorted_list
