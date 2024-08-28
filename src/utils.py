import json
import logging
import os
from typing import Any

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_log_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_log_file_path = os.path.abspath(rel_log_file_path)


# Добавляем логгер, который записывает логи в файл.
logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions_dictionary(path: str) -> dict | Any:
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    logger.info("Запуск программы!!!")
    try:
        with open(path, "r", encoding="utf-8") as operations:
            try:
                list_trans = json.load(operations)
                logger.info("Путь до файла json верный")
                return list_trans
            except json.JSONDecodeError:
                logger.error("Файл повреждён")
                list_trans = []
                return list_trans
    except FileNotFoundError:
        logger.warning("Импортируемый список пуст или отсутствует.")
        list_trans = []
        return list_trans


if __name__ == "__main__":
    print(get_transactions_dictionary("C:/Users/user/PycharmProjects/my_project/data/operations.json"))
    print(get_transactions_dictionary(""))
    print(get_transactions_dictionary("C:/Users/user/PycharmProjects/my_project/data/wrong_operations.json"))
