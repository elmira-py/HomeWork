import pytest
from src.generators import filter_by_currency, transaction_descriptions,card_number_generator

@pytest.mark.parametrize(
    "currency, expected_count",
    [
        ("USD", 3),
        ("RUB", 2),
        ("EUR", 0) ])     # валюта отсутствует
def test_filter_by_currency_parametrized(usd_transactions, currency, expected_count):
    result = list(filter_by_currency(usd_transactions, currency))
    assert len(result) == expected_count
    if expected_count > 0:
        for t in result:
            assert t["operationAmount"]["currency"]["code"] == currency


#  Тест, где нет operationAmount
def test_filter_by_currency_invalid():
    bad_tx = [{"id": 1}]  # нет operationAmount
    result = list(filter_by_currency(bad_tx, "USD"))
    assert result == []

#  Тест, что генератор не завершается ошибкой при обработке
#  пустого списка или списка без соответствующих валютных операций.
def test_filter_by_currency_empty_input():
    result = list(filter_by_currency([], "USD"))
    assert result == []  #  возвращает пустой список

def test_filter_by_currency_mixed_valid_and_invalid():
    mixed = [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},  # валидная
        {"id": 2}  # битая
    ]
    result = list(filter_by_currency(mixed, "USD"))
    assert len(result) == 1
    assert result[0]["id"] == 1


# Тесты для transaction_descriptions
def test_transaction_descriptions(usd_transactions):
    result = list(transaction_descriptions(usd_transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",      # ← из RUB-транзакции
        "Перевод с карты на карту",
        "Перевод организации"            # ← из второй RUB-транзакции
    ]
    assert result == expected

def test_transaction_descriptions_invalid():    # Нет description
    bad_tx = [{"id": 1}]
    result = list(transaction_descriptions(bad_tx))
    assert result == []

def test_transaction_descriptions_empty_input():    # Тест на пустой список
    result = list(transaction_descriptions([]))
    assert result == []


#  Тесты для  card_number_generator
@pytest.mark.parametrize("start, stop, expected", [
    (11, 13, ["0000 0000 0000 0011",                # базовые случаи
            "0000 0000 0000 0012",
            "0000 0000 0000 0013"]),
    (1234, 1234, ["0000 0000 0000 1234"]),    # совпадение  start и stop
    (1201, 1202, ["0000 0000 0000 1201",
               "0000 0000 0000 1202"]),
    (9999999999999998,9999999999999999,                        # крайние значения диапазона
    ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
    (5, 3,[])])                    # start > stop, должен вернуть пустой список



def test_card_number_generator(start, stop, expected) -> str:
    result = list(card_number_generator(start,stop))
    assert result == expected
