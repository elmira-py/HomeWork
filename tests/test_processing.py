import pytest

from src.processing import filter_by_state, sort_by_date

# Тесты для filter_by_state


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 0),
        ("PENDING", 0),
        ("UNKNOWN", 0),
    ],
)
def test_filter_by_state_parametrized(transactions: list[dict], state: str, expected_count: int) -> None:
    result = filter_by_state(transactions, state)
    assert len(result) == expected_count
    assert all(item["state"] == state for item in result)


def test_filter_by_state_missing_key(transactions_mix: list[dict]) -> None:
    result = filter_by_state(transactions_mix, "EXECUTED")
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_filter_by_state_empty_input() -> None:
    assert filter_by_state([]) == []


# Тесты для sort_by_date


def test_sort_by_date() -> None:
    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    ) == (
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    )


def test_sort_by_date_() -> None:
    # Проверка на пустой список
    assert sort_by_date([]) == []
    # Сортировка по убыванию
    assert sort_by_date(
        [
            {"id": 2, "date": "2023-01-02T00:00:00"},
            {"id": 1, "date": "2023-01-01T00:00:00"},
            {"id": 3, "date": "2023-01-03T00:00:00"},
        ]
    ) == (
        [
            {"id": 3, "date": "2023-01-03T00:00:00"},
            {"id": 2, "date": "2023-01-02T00:00:00"},
            {"id": 1, "date": "2023-01-01T00:00:00"},
        ]
    )
    # Сортировка по возрастанию
    assert sort_by_date(
        [{"id": 2, "date": "2023-01-02T00:00:00"}, {"id": 1, "date": "2023-01-01T00:00:00"}], reverse=False
    ) == ([{"id": 1, "date": "2023-01-01T00:00:00"}, {"id": 2, "date": "2023-01-02T00:00:00"}])


def test_sort_by_date_incorrect() -> None:
    # Тест на одинаковые даты
    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        ]
    ) == (
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        ]
    )
    # Нестандартная дата
    assert sort_by_date([{"id": 1, "date": "01/01/2020"}, {"id": 2, "date": "02/01/2019"}]) == [
        {"id": 2, "date": "02/01/2019"},
        {"id": 1, "date": "01/01/2020"},
    ]
    assert sort_by_date([{"id": 1, "date": "01.01.2025"}, {"id": 2, "date": "20.05.2024"}]) == [
        {"id": 2, "date": "20.05.2024"},
        {"id": 1, "date": "01.01.2025"},
    ]

    # Тест на не корректную дату
    with pytest.raises(TypeError):
        sort_by_date([{"id": 1, "date": "2023-01-01T00:00:00"}, {"id": 2, "date": None}])
    with pytest.raises(KeyError):
        sort_by_date([{"id": 3, "state": "EXECUTED"}])


# def test_filter_by_state(transactions):
#     assert filter_by_state(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     ) == transactions
#     #([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     #{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},])
#
#
# def test_filter_by_state_():
#     # Проверка на пустой список
#     assert filter_by_state([]) == []
#     # Нет "state"
#     assert filter_by_state([{"id": 594226727, "date": "2018-09-12T21:27:25.241689"}]) == []
#     # Некорректный "state"
#     assert filter_by_state([{"id": 1, "state": "ABRACADABRA", "date": "2019-07-03T18:35:29.512364"}]) == []
#     assert filter_by_state([{"id": 2, "state": "NONE", "date": "2018-06-30T02:08:58.425572"}]) == []
