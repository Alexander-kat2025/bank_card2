import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("info, expected", [
    ("Счет 12345678901234561234", "Счет **1234"),
    ("Счет 12345678901234567890", "Счет **7890"),
    ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
    ('Maestro 7000792289606361', 'Maestro 7000 79** **** 6361')
])
def test_mask_account_card(info: str, expected: str) -> None:
    """Тест маскировки счета или номера карты"""
    assert mask_account_card(info) == expected


def test_get_date() -> None:
    """Тест преобразования строки даты"""
    assert get_date("2019-07-03T18:35:29.512364") == "03.07.2019"
