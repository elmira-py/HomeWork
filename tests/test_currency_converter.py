from unittest.mock import Mock, patch

from src.external_api.currency_converter import convert_to_rub


def test_convert_usd_to_rub():
    """Тест: конвертация USD → RUB."""
    with patch("src.external_api.currency_converter.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {"rates": {"RUB": 82.5}}
        mock_get.return_value = mock_response

        transaction = {"amount": 100, "currency": "USD"}
        result = convert_to_rub(transaction)

        assert result == 8250.0
        mock_get.assert_called_once()


def test_convert_eur_to_rub():
    """Тест: конвертация EUR → RUB."""
    with patch("src.external_api.currency_converter.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {"rates": {"RUB": 90.0}}
        mock_get.return_value = mock_response

        transaction = {"amount": 50, "currency": "EUR"}
        result = convert_to_rub(transaction)

        assert result == 4500.0
        mock_get.assert_called_once()


def test_convert_rub_no_api_call():
    """Тест: рубли не требуют запроса к API."""
    transaction = {"amount": 1000, "currency": "RUB"}
    result = convert_to_rub(transaction)

    assert result == 1000.0


def test_convert_error_handling():
    """Тест: если API вернул ошибку → функция возвращает исходную сумму."""
    with patch("src.external_api.currency_converter.requests.get") as mock_get:
        mock_get.side_effect = Exception("Connection Error")

        transaction = {"amount": 100, "currency": "USD"}
        result = convert_to_rub(transaction)

        assert result == 100.0
        mock_get.assert_called_once()
