from typing import Any


def filter_by_state(operations: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    Фильтрует список операций по значению ключа 'state'.

    """
    filtered_operations = []
    for operation in operations:
        if "state" in operation and operation["state"] == state:
            filtered_operations.append(operation)
    return filtered_operations


def sort_by_date(operations: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция сортирует список по дате"""
    return sorted(operations, key=lambda x: x.get("date", ""), reverse=reverse)
