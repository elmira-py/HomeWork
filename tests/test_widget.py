import pytest

from src.widget import mask_account_card, get_date


#   Тесты для mask_account_card


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
        ("MasterCard 0123456987256252", "MasterCard 0123 45** **** 6252"),
        ("Maestro 9876543210987654", "Maestro 9876 54** **** 7654"),
        ("Счет 78901234567890123456", "Счет **3456"),
        ("Счет 01234567891234567899", "Счет **7899"),
    ],
)
def test_mask_account_card_valid(input_str: str, expected: str) -> None:
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize(
    "invalid_str",
    [
        "",  # пустая строка
        "   ",  # только пробелы
        "Visa 12345",  # меньше 16 цифр
        "Счет 1234567890",  # меньше 20 цифр
        "Счет 1234567890123456789012345",  # больше 20 цифр
        "BankCard ABC123",  # не цифры в номере
    ],
)
def test_mask_account_card_invalid(invalid_str: str) -> None:
    if invalid_str.strip() == "":
        assert mask_account_card(invalid_str) == invalid_str
    else:
        # Если ошибка → ValueError:
        with pytest.raises(ValueError):
            mask_account_card(invalid_str)


@pytest.mark.parametrize(
    "iso_date, expected",
    [
        ("2025-12-17T15:30:00.123456", "17.12.2025"),
        ("2023-01-05T09:15:45", "05.01.2023"),
        ("2024-07-21", "21.07.2024"),
        ("2024-03-01T00:00:00", "01.03.2024"),
    ],
)
def test_get_date_valid(iso_date: str, expected: str) -> None:
    assert get_date(iso_date) == expected


@pytest.mark.parametrize(
    "invalid_date",
    ["", "hello", "2024/03/11", "2024-3-1", "17.12.2025", "not a date"],  # уже в целевом формате, но не ISO
)
def test_get_date_invalid(invalid_date: str) -> None:
    #  при ошибке
    assert get_date(invalid_date) == ""


# def test_mask_account_card():
#
#     # Тест для банковской карты
#     assert mask_account_card("Visa Platinum 1234567890123456") == "Visa Platinum 1234 56** **** 3456"
#     assert mask_account_card("MasterCard 0123456987256252") == "MasterCard 0123 45** **** 6252"
#
#     # Тест для счёта
#     assert mask_account_card("Счет 12345678901234567890") ==  "Счет **7890"
#     assert mask_account_card("Счет 01234567891234567899") ==  "Счет **7899"
#
#     # Тест с пустой строкой или пробелами
#     assert mask_account_card("") == ""
#     assert mask_account_card("   ") == "   "
#     # Тест с некорректным номером счёта
#     with pytest.raises(ValueError):
#         mask_account_card("Visa 12345")  # меньше 16 цифр
#     with pytest.raises(ValueError):
#         mask_account_card("Счет 1234567890")  # меньше 20 цифр
#     with pytest.raises(ValueError):
#         mask_account_card("Счет 123456789023232323232")  # больше 20 цифр
#
#
# def test_get_date(data_string):
#     assert get_date("2025-12-17T15:30:00.123456") == data_string #"17.12.2025"
#     assert get_date("2023-01-05T09:15:45") == "05.01.2023"
#     assert get_date("2024-07-21") == "21.07.2024"
#
#     # Некорректные данные/ отсутствует дата
#     assert get_date("") == ""
#     assert get_date("hello") == ""
#     assert get_date("2024/03/11") == ""
#     assert get_date("2024-3-1") == ""
