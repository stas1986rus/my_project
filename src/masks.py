from typing import Union


def get_mask_card_number(num_card: Union[str, int]) -> str:
    """Принимает на вход номер карты и возвращает ее маску"""

    str_card = str(num_card)
    return f"{str_card[0:4]} {str_card[4:6]}** **** {str_card[-4:]}"


def get_mask_account(num_account: Union[str, int]) -> str:
    """Принимает на вход номер счета и возвращает его маску"""
    str_account = str(num_account)
    return f"**{str_account[-4:]}"
