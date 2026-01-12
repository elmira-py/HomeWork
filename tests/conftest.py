from typing import List, Dict, Any
import pytest


@pytest.fixture
def mask_card_number() -> str:
    return "0123 45** **** 6252"


@pytest.fixture
def mask_account_number() -> str:
    return "**7899"


@pytest.fixture
def masked_card() -> str:
    return "Visa Platinum 1234 56** **** 3456"


@pytest.fixture
def masked_account() ->str:
    return "Счет **7890"


@pytest.fixture
def data_string() -> str:
    return "17.12.2025"


@pytest.fixture
def transactions()-> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def transactions_mix() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "date": "2023-01-01T00:00:00"},  # без state
        {"id": 2, "state": "EXECUTED"},
        {"id": 3, "state": "PENDING", "date": "2023-01-03T00:00:00"},
    ]
