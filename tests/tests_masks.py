import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number, expected", [
    ("1234 5678 9012 3456", "1234 56** **** 3456"),
    ("1234567890123456", "1234 56** **** 3456"),
    ("1234 5678 9012 345", "123 45** **** 2345"),
    ("1234 5678 9012 34567", "1234 567** **** 4567"),
    ("1234 5678 9012", "12** **** 9012"),
   ("", "")
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize("account_number, expected", [
    ("12345678901234567890", "**7890"),
    ("1234567890", "**7890"),
    ("123456", "**3456"),
    ("", ""),
    ("abcd1234efgh5678", "**5678")
])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected
