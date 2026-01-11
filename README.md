# Домашнее задание по Python

IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, 
который показывает несколько последних успешных банковских операций клиента.

## Установка:
1. Клонируйте репозиторий:
SSH key - git@github.com:elmira-py/HomeWork.git
2. https://github.com/elmira-py/HomeWork.git

## Модуль masks
Содержит функции для наложения масок на конфиденциальные данные:

**get_mask_card_number(card_number: str) -> str**

Маскирует номер банковской карты в формате: XXXX XX** **** XXXX
Пример: 7000792289606361 → 7000 79** **** 6361

**get_mask_account(account_number: str) -> str**

Маскирует номер счета в формате: **XXXX
**Пример:** 73654108430135874305 → **4305

## Модуль widget
Содержит функции для работы с банковскими данными:

**mask_account_card(card_or_account_data: str) -> str**

Автоматически определяет тип данных (карта или счет) и применяет соответствующую маску.
**Пример для карты:** Visa Platinum 7000792289606361 → Visa Platinum 7000 79** **** 6361
**Пример для счета:** Счет 73654108430135874305 → Счет **4305

feature/tests
**def get_date(date_string: str) -> str**
=======
**get_date(data_info: str) -> str**
develop
Функция берёт данные даты и времени в формате "2024-03-11T02:26:18.671407"
и возвращает только дату в формате 'ДД.ММ.ГГГГ'"""

## Модуль processing
 Модуль processing предоставляет функции для фильтрации и сортировки банковских операций.

feature/tests
**filter_by_state(transactions: list, state: str = 'EXECUTED') -> list**
Фильтрует список операций по статусу выполнения.

**Параметры:**

transactions: Список словарей с операциями
=======
**filter_by_state(operations: list, state: str = 'EXECUTED') -> list**
Фильтрует список операций по статусу выполнения.

**Параметры:**

operations: Список словарей с операциями
develop
state: Статус для фильтрации. По умолчанию 'EXECUTED'

**Пример использования:**
```
from processing import filter_by_state

feature/tests
transactions = [
=======
operations = [
develop
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
    ]

# Фильтрация по статусу 'EXECUTED' (по умолчанию)
feature/tests
executed_operations = filter_by_state(transactions)
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]

# Фильтрация по статусу 'CANCELED'
canceled_operations = filter_by_state(transactions, 'CANCELED')
# [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]
```
**sort_by_date(transactions: list, reverse: bool = True) -> list**
Сортирует список операций по дате.

**Параметры:**

transactions: Список словарей с операциями
=======
executed_operations = filter_by_state(operations)
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]

# Фильтрация по статусу 'CANCELED'
canceled_operations = filter_by_state(operations, 'CANCELED')
# [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]
```
**sort_by_date(operations: list, reverse: bool = True) -> list**
Сортирует список операций по дате.

**Параметры:**

operations: Список словарей с операциями
develop
reverse: Порядок сортировки(True (по умолчанию) - по убыванию, False - по возрастанию(сначала самые старые))

Пример использования:
```
feature/tests
transactions = [
=======
operations = [
develop
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]

# Сортировка по убыванию (сначала новые) feature/tests
sorted_desc = sort_by_date(transactions)
# [{'id': 41428829, ...}, {'id': 939719570, ...}]

# Сортировка по возрастанию (сначала старые)
sorted = sort_by_date(transactions, reverse=False)
# [{'id': 939719570, ...}, {'id': 41428829, ...}]
```
## Тестирование
Добавлен раздел "tests" с папками- тестами для каждой функции с параметризацией, также добавлена папка "conftest.py" 
с фикстурами для функций.
Проект полностью покрыт автоматическими тестами с использованием `pytest`.  
Покрытие исходного кода составляет **98%**.

### Запуск тестов
Убедитесь, что установлены зависимости (включая `pytest`), затем выполните:
```bash
pytest
В репозитории сохранён HTML-отчёт о покрытии кода тестами.
Чтобы просмотреть его:

Перейдите в папку htmlcov/
Откройте файл index.html в браузере


# Разработка:
 
=======
sorted_desc = sort_by_date(operations)
# [{'id': 41428829, ...}, {'id': 939719570, ...}]

# Сортировка по возрастанию (сначала старые)
sorted_asc = sort_by_date(operations, reverse=False)
# [{'id': 939719570, ...}, {'id': 41428829, ...}]
```


# Разработка:

 develop
+ Проект находится в активной разработке. В ближайших планах:

+ Добавление новых модулей для расширения функционала

+ Улучшение обработки различных форматов данных

+ Добавление тестов

# Команда проекта
elmira-py - Beginner Python developer

*Проект разработан в рамках учебного курса SkyPro*
