from typing import Union

import masks


def mask_account_card(user_data: Union[str]) -> str:
    """Функция которая умеет обрабатывать информацию как о картах, так и о счетах"""
    word = user_data.split()
    num_card = word[-1]
    num_account = word[-1]
    name_account_card = " ".join(word[0:-1])
    if len(word[-1]) == 16:
        return f"{name_account_card} {masks.get_mask_card_number(num_card)}"
    elif len(word[-1]) == 20:
        return f"{name_account_card} {masks.get_mask_account(num_account)}"


def get_date(date_entry: Union[str]) -> str:
    '''Функция которая принимает на вход строку
    с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку
    с датой в формате "ДД.ММ.ГГГГ"'''
    return f"{date_entry[8:10]}.{date_entry[5:7]}.{date_entry[0:4]}"