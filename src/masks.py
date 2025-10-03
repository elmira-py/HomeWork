def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты и возвращает ее маску, где видны только первые 6 цифр и
    последние 4"""
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр и только цифры")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(number_account: str) -> str:
    """Функция принимает на вход номер счета (20 цифр) и возвращает его маску в формате **XXXX, где
     XXXX - последние 4 цифры счета"""
    if len(number_account) != 20 or not number_account.isdigit():
        raise ValueError("Номер счета должен содержать только 20 цифр")

    return f"**{number_account[-4:]}"
