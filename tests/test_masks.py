import pytest


from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    # Тестирование правильности маски номера карты.
    assert get_mask_card_number("0123456987256252") == "0123 45** **** 6252"

    # Тестирование на нестандартные длины номеров
    with pytest.raises(ValueError):
        get_mask_card_number("123456789012345a")  # не все цифры
    with pytest.raises(ValueError):
        get_mask_card_number("12345678901234567")  # 17 цифр
    with pytest.raises(ValueError):
        get_mask_card_number("01234569872562526666") # 20 цифр
    with pytest.raises(ValueError):
        get_mask_card_number("012")          # короткий ввод
    with pytest.raises(ValueError):
        get_mask_card_number("")             # пустая строка


def test_mask_account():
    # Тестирование правильности маски номера счета.
    assert get_mask_account("01234567891234567899") == "**7899"

    # Тесты на нестандартные длины счета
    with pytest.raises(ValueError):
        get_mask_account("012345678912345678999")  # длинный ввод
    with pytest.raises(ValueError):
        get_mask_account("012345")                 # короткий ввод
    with pytest.raises(ValueError):
        get_mask_account("0123456789123456789a")   # не все цифры
    with pytest.raises(ValueError):
        get_mask_account("")                       #  пустая строка