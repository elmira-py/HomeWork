import json
import os
from typing import Any, Dict, List


def load_transactions(filepath: str) -> List[Dict[str, Any]]:
    """Загружаем транзакции из JSON файла"""
    try:
        if not os.path.exists(filepath):
            return []
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            return []
        return data
    except json.JSONDecodeError:
        return []
