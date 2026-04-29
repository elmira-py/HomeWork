from unittest.mock import mock_open, patch

from src.utils.data_loader import load_transactions


@patch("src.utils.data_loader.json.load")
@patch("src.utils.data_loader.open", new_callable=mock_open)
@patch("src.utils.data_loader.os.path.exists")
def test_load_transactions_success(mock_exists, mock_file, mock_json_load):
    """
    Тест: функция загружает транзакции из файла.

    Мы заменяем:
    - os.path.exists → возвращает True (файл есть)
    - open → мокируем открытие файла
    - json.load → возвращает тестовые данные
    """
    # Настраиваем моки
    mock_exists.return_value = True  # Файл существует
    mock_json_load.return_value = [{"id": 1, "amount": 100}]  # Тестовые данные

    # Вызываем функцию
    result = load_transactions("data/operations.json")

    # Проверяем результат
    assert len(result) == 1
    assert result[0]["id"] == 1
    assert result[0]["amount"] == 100

    # Проверяем, что моки были вызваны правильно
    mock_exists.assert_called_once_with("data/operations.json")
    mock_json_load.assert_called_once()


@patch("src.utils.data_loader.os.path.exists")
def test_load_transactions_file_not_found(mock_exists):
    """
    Тест: файл не существует → возвращается пустой список.
    """
    # Настраиваем мок: файл не существует
    mock_exists.return_value = False

    # Вызываем функцию
    result = load_transactions("nonexistent.json")

    # Проверяем результат
    assert result == []
    mock_exists.assert_called_once_with("nonexistent.json")


@patch("src.utils.data_loader.json.load")
@patch("src.utils.data_loader.open", new_callable=mock_open)
@patch("src.utils.data_loader.os.path.exists")
def test_load_transactions_not_list(mock_exists, mock_file, mock_json_load):
    """
    Тест: внутри файла не список (а словарь) → возвращается пустой список.
    """
    # Настраиваем моки
    mock_exists.return_value = True
    mock_json_load.return_value = {"id": 1}  # Словарь вместо списка!

    # Вызываем функцию
    result = load_transactions("data/operations.json")

    # Проверяем результат
    assert result == []
