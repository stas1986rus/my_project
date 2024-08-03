from typing import Union


def get_mask_card_number(num_card: Union[str, int]) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""

    str_card = str(num_card)
    if len(str_card) < 16:
        return "Введено меньше цифр чем на самой карте или совсем пусто!!!"
    elif str_card.isdigit() == 0:
        return "Опечатка, Вы ввели буквы в место цифры!!!"
    elif len(str_card) > 16:
        return "Введено больше цифр чем на самой карте!!!"
    elif str_card == "":
        return "Введено меньше цифр чем на самой карте или совсем пусто!!!"

    return f"{str_card[0:4]} {str_card[4:6]}** **** {str_card[-4:]}"


def get_mask_account(num_account: Union[str, int]) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    str_account = str(num_account)
    if len(str_account) < 20:
        return "Вы ввели меньше цифр!!!"
    elif str_account.isdigit() == 0:
        return "Опечатка, Вы ввели буквы в место цифры!!!"
    elif len(str_account) > 20:
        return "Вы ввели больше цифр!!!"
    elif str_account == "":
        return ""

    return f"**{str_account[-4:]}"
