from typing import Any, Dict

import requests


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """Конвертирует сумму транзакции в рубли.

    Использует ExchangeRate-API Open Access (без ключа):
    https://www.exchangerate-api.com/docs/free

    Примечание:
    - Поддерживает любую базовую валюту (USD, EUR, RUB и др.)
    - Не требует API-ключа
    - Для использования openexchangerates.org раскомментируйте API_KEY в .env
    """
    # Получаем сумму и валюту из транзакции
    amount = transaction.get("amount", 0)
    currency = transaction.get("currency", "").upper()

    # Если уже рубли — не конвертируем
    if currency == "RUB":
        return float(amount)

    # Если валюта поддерживается — делаем запрос к бесплатному API
    if currency in ("USD", "EUR"):
        try:
            # Бесплатный API без ключа, поддерживает любую базовую валюту
            url = f"https://open.er-api.com/v6/latest/{currency}"
            response = requests.get(url, timeout=5)
            response.raise_for_status()

            data = response.json()

            # Получаем курс к рублю
            if "rates" in data and "RUB" in data["rates"]:
                rate = data["rates"]["RUB"]
                return round(amount * rate, 2)
            else:
                return float(amount)

        except requests.exceptions.ConnectionError:
            print("Connection Error. Please check your network connection.")
        except requests.exceptions.HTTPError:
            print("HTTP Error. Please check the URL.")
        except requests.exceptions.Timeout:
            print("Request timed out. Please check your internet connection.")
        except requests.exceptions.TooManyRedirects:
            print("Too many redirects. Please check the URL.")
        except requests.exceptions.RequestException:
            print("An error occurred. Please try again later.")
        except Exception:
            print("Unexpected error occurred")

    # Если валюта не поддерживается или ошибка — возвращаем как есть
    return float(amount)
