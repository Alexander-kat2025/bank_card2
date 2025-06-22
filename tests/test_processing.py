import pytest
from src.processing import filter_by_state, sort_by_date
from typing import Any

@pytest.mark.parametrize(
    'state, expected',
    [
        ('EXECUTED', 2),
        ('CANCELED', 1),
        ('PENDING', 1),
        ('UNKNOWN', 0)
    ]
)
def test_filter_by_state(operations: list[dict[str, Any]],state: str, expected: int) -> None:
    """Тест фильтрации по статусу"""
    result = filter_by_state(operations, state)

    assert len(result) == expected


def test_sort_by_date_missing_argument(operations: list[dict[str, Any]]) -> None:
    """Тест сортировки по дате без второго аргумента"""
    desc_sorted = sort_by_date(operations)

    assert desc_sorted[0]['date'] >= desc_sorted[-1]['date']


def test_sort_by_date(operations: list[dict[str, Any]]) -> None:
    """Тест сортировки по дате"""
    asc_sorted = sort_by_date(operations, reverse=False)

    assert asc_sorted[0]['date'] <= asc_sorted[-1]['date']
