import logging
import os
from typing import Union

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))

# Создаем путь до файла логов относительно текущей директории
rel_log_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_log_file_path = os.path.abspath(rel_log_file_path)


# Добавляем логгер, который записывает логи в файл.
logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(num_card: Union[str, int]) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""
    logger.info("Запуск функции маскирующей номер Вашей карта!!!")
    str_card = str(num_card)
    if len(str_card) < 16 or "":
        logger.warning("Не хватает цифр!!!")
        return "Введено меньше цифр чем на самой карте или совсем пусто!!!"
    elif str_card.isdigit() == 0:
        logger.warning("Присутствуют буквы в номере карты!!!")
        return "Опечатка, Вы ввели буквы в место цифры!!!"
    elif len(str_card) > 16:
        logger.warning("Введено больше цифр!!!")
        return "Введено больше цифр чем на самой карте!!!"
    logger.info("Корректный ввод!!!")
    return f"{str_card[0:4]} {str_card[4:6]}** **** {str_card[-4:]}"


def get_mask_account(num_account: Union[str, int]) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    logger.info("Запуск функции маскирующей номер Вашего счёта!!!")
    str_account = str(num_account)
    if len(str_account) < 20 or "":
        logger.warning("Не хватает цифр!!!")
        return "Вы ввели меньше цифр!!!"
    elif str_account.isdigit() == 0:
        logger.warning("Присутствуют буквы в номере счёта!!!")
        return "Опечатка, Вы ввели буквы в место цифры!!!"
    elif len(str_account) > 20:
        logger.warning("Введено больше цифр!!!")
        return "Вы ввели больше цифр!!!"
    logger.info("Корректный ввод!!!")
    return f"**{str_account[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))  # правильный ввод номера карты
    print(get_mask_card_number("700079228960"))  # мало цифр в вводе номера карты
    print(get_mask_card_number("70ab792289606361"))  # есть буквы в вводе номера карты
    print(get_mask_card_number("70007922896063611234"))  # много цифр в вводе номера карты

    print(get_mask_account("73654108430135874305"))
    print(get_mask_account("7365410843013587"))
    print(get_mask_account("73654108ab0135874305"))
    print(get_mask_account("736541084301358743051234"))
