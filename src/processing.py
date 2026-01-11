def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
feature/tests
    """функция filter_by_state, которая принимает список словарей и опционально значение
    для ключа state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению."""
=======
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
  state соответствует указанному значению. state (по умолчанию 'EXECUTED') """

develop

    filtered = []
    for transaction in transactions:
        if transaction.get("state") == state:
            filtered.append(transaction)
    return filtered


feature/tests
def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок
    сортировки (по умолчанию — убывание). Функция должна возвращать новый список,
    отсортированный по дате (date)."""

    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)
=======
def sort_by_date(transactions: list[dict],reverse: bool = True) -> list[dict]:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок
     сортировки (по умолчанию — убывание). Функция должна возвращать новый список,
     отсортированный по дате (date)."""

    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)

develop
