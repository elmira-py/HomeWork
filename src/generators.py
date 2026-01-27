from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Создайте функцию filter_by_currency, которая принимает на вход список словарей,
    представляющих транзакции. Функция должна возвращать итератор, который поочередно
    выдает транзакции, где валюта операции соответствует заданной (например, USD)."""
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        except KeyError:
            continue


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Напишите генератор transaction_descriptions, который принимает список словарей
    с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        try:
            yield transaction["description"]
        except KeyError:
            continue


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Создайте генератор card_number_generator, который выдает номера банковских карт
    в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать
    номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров."""
    for card_number in range(start, stop + 1):
        #  Преобразуем число в строку из 16 цифр с нулями в начале
        card_number = str(card_number).zfill(16)
        # Разбиваем строку на блоки по 4 цифры
        str_number = [card_number[0:4], card_number[4:8], card_number[8:12], card_number[12:16]]
        # Собираем строку через пробел
        result = " ".join(str_number)
        yield result


# if __name__ == "__main__":
#     for card_number in card_number_generator(1, 5):
#         print(card_number)
