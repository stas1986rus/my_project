import os
from unittest.mock import patch

import pytest
from dotenv import load_dotenv

from src.external_api import convert_from_i_to_rub

load_dotenv()
api_key = os.getenv("API_KEY")


@pytest.fixture
def get_rub_transaction():
    return 123.45


@pytest.fixture
def get_usd_transaction():
    return 123.45


transaction = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": 123.45, "currency": {"name": "руб.", "code": "RUB"}},
}

transaction_usr = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": 2.0, "currency": {"name": "USD.", "code": "USD"}},
}


transaction_r = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": 2.0, "currency": {"name": "USD", "code": "r"}},
}


def test_convert_from_rub_to_rub(get_rub_transaction):
    assert convert_from_i_to_rub(transaction) == 123.45


def test_convert_from_not_to_rub(get_usd_transaction):
    assert convert_from_i_to_rub(transaction_r) == "Неизвесная волюта"


@patch("requests.request")
@patch("src.external_api.api_key", "temporary_key")
def test_convert_from_not_rub_to_rub(mock_get):
    mock_get.return_value.json.return_value = {"result": 174.62}
    assert convert_from_i_to_rub(transaction_usr) == 174.62
    mock_get.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=2.0",
        headers={"apikey": "temporary_key"},
    )
