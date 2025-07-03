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


def card_number_generator(start: int, stop: int) -> str:
    """
       Генератор номеров банковских карт в формате "XXXX XXXX XXXX XXXX
       с проверкой нумеровки карты не меньше 0 и не больше 9999999999999999".
"""

    if start < 1:
        raise ValueError("start должен быть не меньше 1")
    if stop > 9999999999999999:
        raise ValueError("stop должен быть не больше 9999999999999999")
    if start > stop:
        raise ValueError("start не может быть больше stop")

    for number in range(start, stop + 1):
        yield number