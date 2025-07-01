from typing import Dict, List, Iterator, Any

def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по заданной валюте и возвращает итератор.

    """
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        transaction_currency = operation_amount.get("currency", {}).get("code")
        if transaction_currency == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генератор, который возвращает описания транзакций по очереди.

    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> str:
    """
       Генератор номеров банковских карт в формате "XXXX XXXX XXXX XXXX".
"""

    for num in range(start, end + 1):
        yield ' '.join([f"{num:016d}"[i:i+4] for i in range(0, 16, 4)])