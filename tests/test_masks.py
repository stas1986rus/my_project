import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "num_card, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("700079228960636", "Введено меньше цифр чем на самой карте или совсем пусто!!!"),
        ("aa000s289606361b", "Опечатка, Вы ввели буквы в место цифры!!!"),
        ("70007922896063612", "Введено больше цифр чем на самой карте!!!"),
    ],
)
def test_get_mask_card_number(num_card, expected):
    assert get_mask_card_number(num_card) == expected


@pytest.mark.parametrize(
    "num_account, expected_acc",
    [
        ("73654108430135874305", "**4305"),
        ("7365410843013587", "Вы ввели меньше цифр!!!"),
        ("7365dfc8430ghj874305", "Опечатка, Вы ввели буквы в место цифры!!!"),
        ("736541084301358743050", "Вы ввели больше цифр!!!"),
    ],
)
def test_get_mask_account(num_account, expected_acc):
    assert get_mask_account(num_account) == expected_acc


def test_mask_account_empty():
    assert get_mask_card_number("") == "Введено меньше цифр чем на самой карте или совсем пусто!!!"
    assert get_mask_account("") == "Вы ввели меньше цифр!!!"
