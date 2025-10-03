from .masks import get_mask_card_number, get_mask_account

"""Импорт функций из masks.py"""


def mask_account_card(info: str) -> str:
    """Функция принимает строку, где указано тип и номер карты или счета и
    возвращает строку с замаскированным номером"""
    if not info.strip():  #
        return info

    words = info.split()  #
    number = words[-1]
    name = " ".join(words[:-1])

    if name == "Счет":
        masked = get_mask_account(number)
    else:
        masked = get_mask_card_number(number)

    return f"{name} {masked}"


def get_date(date_incorrect: str) -> str:
    """Функция возвращает строку с датой в формате "ДД.ММ.ГГГГ"""
    year = date_incorrect[0:4]
    month = date_incorrect[5:7]
    day = date_incorrect[8:10]
    return f"{day}.{month}.{year}"
