import os
from config import DIR_DATA

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_transactions_dictionary
from src.reading_files import reader_file_transaction_csv, reader_file_transaction_excel
from src.filter_transactions import sorting_transactions_by_description
from src.widget import get_date, mask_account_card

PATH_TO_FILE_JSON = os.path.join(DIR_DATA, "operations.json")
PATH_TO_FILE_CSV = os.path.join(DIR_DATA, "transactions.csv")
PATH_TO_FILE_EXCEL = os.path.join(DIR_DATA, "transactions_excel.xlsx")


def main():
    """Main function of the Project."""

    while True:
        menu_item = input(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
        )
        if menu_item == "1":
            print("Для обработки выбран JSON-файл.")
            transactions = get_transactions_dictionary(PATH_TO_FILE_JSON)
            break
        elif menu_item == "2":
            print("Для обработки выбран CSV-файл.")
            transactions = reader_file_transaction_csv(PATH_TO_FILE_CSV)
            break
        elif menu_item == "3":
            print("Для обработки выбран XLSX-файл.")
            transactions = reader_file_transaction_excel(PATH_TO_FILE_EXCEL)
            break
        else:
            print("Такого пункта в меню нет, попробуйте еще раз.")

    state_list = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        state = input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.
"""
        ).upper()

        if state not in state_list:
            print(f'Статус операции "{state}" недоступен.')
        else:
            break

    filtered_transactions = filter_by_state(transactions, state)


    while True:
        print("Отфильтровать операции по дате?")
        users_choise_date_sort = input("Введите да/нет сюда: ").lower()
        if users_choise_date_sort in ("да", "нет"):
            break
        else:
            print("Введён некорректный ответ. Повторите ввод ответа.")
    if users_choise_date_sort == "да":

        while True:
            print("Отфильтровать по возрастанию или убыванию?")
            users_choise_sort_direction = input("Введите по возрастанию/по убыванию сюда: ").lower()
            if users_choise_sort_direction in ("по возрастанию", "по убыванию"):
                break
            print("Введён некорректный ответ. Повторите ввод ответа.")
        if users_choise_sort_direction == "по возрастанию":
            reverse = False
        elif users_choise_sort_direction == "по убыванию":
            reverse = True
        filtered_transactions = sort_by_date(filtered_transactions, reverse)
    elif users_choise_date_sort == "нет":
        filtered_transactions = filtered_transactions



    filter_by_rub = input("Выводить только рублевые транзакции? Да/Нет ")
    if filter_by_rub.lower() == "да":
        rub_transactions = filter_by_currency(filtered_transactions, "RUB")
        filtered_transactions = list(rub_transactions)[:-1]

    while True:
        print("Отфильтровать список по определённому слову в описании (description)?")
        users_choise_description = input("Введите да/нет сюда: ").lower()
        if users_choise_description in ("да", "нет"):
            break
        else:
            print("Введён некорректный ответ. Повторите ввод ответа.")
    if users_choise_description == "да":
        users_word_to_filter = input("Введите слово для сортировки сюда: ").lower()
        sorted_by_description = sorting_transactions_by_description(filtered_transactions, users_word_to_filter)
        result_transactions = sorted_by_description
    elif users_choise_description == "нет":
        result_transactions = filtered_transactions



    print("Распечатываю итоговый список транзакций...")
    if len(result_transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"""
        Всего банковских операций в выборке: {len(filtered_transactions)}
        """)
        for tr in result_transactions:
            tr_date = get_date(tr["date"])
            currency = tr["operationAmount"]["currency"]["name"]
            if tr["description"] == "Открытие вклада":
                from_to = mask_account_card(tr["to"])
            else:
                from_to = mask_account_card(tr["from"]) + " -> " + mask_account_card(tr["to"])

            amount = tr["operationAmount"]["amount"]
            print(
                f"""{tr_date} {tr['description']}
{from_to}
Сумма: {round(float(amount))} {currency}
"""
            )


if __name__ == "__main__":
    main()
