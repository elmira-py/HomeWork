import pytest

from src.masks import get_mask_account, get_mask_card_number


#  Тесты для маскировки карты
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("0123456987256252", "0123 45** **** 6252"),
        ("9876543210987654", "9876 54** **** 7654"),
    ],
)
def test_get_mask_card_number_valid(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "invalid_card",
    [
        "",  # пустая строка
        "123",  # слишком коротко
        "123456789012345",  # 15 цифр
        "12345678901234567",  # 17 цифр
        "12345678901234567890",  # 20 цифр (счёт?)
        "123456789012345a",  # не цифры
        "12 34 56 78 90",  # пробелы
    ],
)
def test_get_mask_card_number_invalid(invalid_card: str) -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card)


#    Тесты для маскирования счёта
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("12345678901234567890", "**7890"),
        ("01234567891234567899", "**7899"),
        ("98765432109876543210", "**3210"),
    ],
)
def test_get_mask_account_valid(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "invalid_account",
    [
        "",  # пусто
        "123",  # коротко
        "1234567890123456789",  # 19 цифр
        "123456789012345678901",  # 21 цифра
        "1234567890123456789a",  # не цифры
        "12345678901234567890 ",  # пробел
    ],
)
def test_get_mask_account_invalid(invalid_account: str) -> None:
    with pytest.raises(ValueError):
        get_mask_account(invalid_account)


# def test_get_mask_card_number(mask_card_number):
#         Тестирование правильности маски номера карты.
#    assert get_mask_card_number("0123456987256252") == "0123 45** **** 6252"
#
#    # Тестирование на нестандартные длины номеров
#    with pytest.raises(ValueError):
#        get_mask_card_number("123456789012345a")  # не все цифры
#    with pytest.raises(ValueError):
#        get_mask_card_number("12345678901234567")  # 17 цифр
#    with pytest.raises(ValueError):
#        get_mask_card_number("01234569872562526666")  # 20 цифр
#    with pytest.raises(ValueError):
#        get_mask_card_number("012")  # короткий ввод
#    with pytest.raises(ValueError):
#        get_mask_card_number("")  # пустая строка


# def test_mask_account(mask_account_number):
#     # Тестирование правильности маски номера счета.
#     assert get_mask_account("01234567891234567899") == mask_account_number # **7899
#
#     # Тесты на нестандартные длины счета
#     with pytest.raises(ValueError):
#         get_mask_account("012345678912345678999")  # длинный ввод
#     with pytest.raises(ValueError):
#         get_mask_account("012345")                 # короткий ввод
#     with pytest.raises(ValueError):
#         get_mask_account("0123456789123456789a")   # не все цифры
#     with pytest.raises(ValueError):
#         get_mask_account("")                       #  пустая строка
