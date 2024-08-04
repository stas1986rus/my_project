import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def by_state():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "filter_state, expected",
    [
        ([], []),
        ([{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}], []),
    ],
)
def test_filter_by_specified_state(filter_state, expected):
    assert filter_by_state(filter_state) == expected


def test_filter_by_state(by_state):
    assert filter_by_state(by_state) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_canceled(by_state):
    assert filter_by_state(by_state, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_sort_by_date(by_state):
    assert sort_by_date(by_state) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_reverse(by_state):
    assert sort_by_date(by_state, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.mark.parametrize(
    "filter_state, expected",
    [
        ([], []),
        (
            [{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}],
            [{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}],
        ),
    ],
)
def test_filter_by_specified_date(filter_state, expected):
    assert sort_by_date(filter_state) == expected
