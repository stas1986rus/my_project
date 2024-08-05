from typing import Any


def filter_by_state(filter_state: Any, state="EXECUTED") -> Any:
    """Функция принимает список словарей и возвращает новый список словарей содержащий только
    те словари, у которых ключ state соответствует указанному значению"""
    new_filter_state = []

    for dictionary_state in filter_state:
        if dictionary_state["state"] == state:
            new_filter_state.append(dictionary_state)
    return new_filter_state

    if filter_state == []:
        return []
    elif dictionary_state["state"] != state:
        return []


def sort_by_date(list_of_dictionaries: Any, reverse_list=True) -> list:
    """Функция сортировки по дате, поумолчанию от большего к меньшему"""
    sorted_list = sorted(list_of_dictionaries, key=lambda d: d["date"], reverse=reverse_list)
    return sorted_list
    if list_of_dictionaries == []:
        return []
    elif list_of_dictionaries["date"] == list_of_dictionaries["date"]:
        return list_of_dictionaries
