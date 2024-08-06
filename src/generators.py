def filter_by_currency(transactions_list, currency):
    """Фильтрует банковские операции по заданной валюте"""
    if len(transactions_list) > 0:
        filtered_transactions = filter(
            lambda transactions_list: transactions_list.get("operationAmount").get("currency").get("code") == currency,
            transactions_list,
        )
        return filtered_transactions
    else:
        return "Список пустой!"


def transaction_descriptions(transactions_list):
    """Выводит описание операций"""
    if len(transactions_list) > 0:
        for element in transactions_list:
            yield element.get("description")
    else:
        yield "Список пустой!"


def card_number_generator(start, stop):
    """Генерирует номера карт в заданном диапазоне"""
    while start <= stop:
        str_number = str(start)
        while len(str_number) < 16:
            str_number = "0" + str_number
        formatted_card_number = (
            str_number[0:4] + " " + str_number[4:8] + " " + str_number[8:12] + " " + str_number[12:16]
        )
        yield formatted_card_number
        start += 1
