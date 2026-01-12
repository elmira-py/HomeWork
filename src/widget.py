from .masks import get_mask_account, get_mask_card_number

"""Импорт функций из masks.py"""


def mask_account_card(info: str) -> str:
    """Функция принимает строку, где указано тип и номер карты или счета и
    возвращает строку с замаскированным номером"""
    if not info.strip():
        return info

    words = info.split()
    number = words[-1]
    name = " ".join(words[:-1])

    if name == "Счет":
        masked = get_mask_account(number)
    else:
        masked = get_mask_card_number(number)

    return f"{name} {masked}"


def get_date(date_string: str) -> str:
    """Функция возвращает строку с датой в формате "ДД.ММ.ГГГГ"""

    """Если строка слишком короткая или не соответствует формату — возвращает пустую строку."""
    if not date_string or len(date_string) < 10:
        return ""

    # Проверяем, что на нужных местах стоят дефисы, например "2024-03-11T02:26:18.671407"
    if date_string[4] != '-' or date_string[7] != '-':
        return ""

    year = date_string[0:4]
    month = date_string[5:7]
    day = date_string[8:10]

    # Проверяем, что год, месяц, день — цифры
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return ""

    return f"{day}.{month}.{year}"