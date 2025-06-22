import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("info, expected", [
    ("Счет 12345678901234561234", "Счет **1234"),
    ("Счет 12345678901234567890", "Счет **7890"),

])
def test_mask_account_card(info, expected):
    assert mask_account_card(info) == expected

def test_get_date():
    """Тест преобразования строки даты"""
    assert get_date("2019-07-03T18:35:29.512364") == "03.07.2019"



def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("invalid-date")

    with pytest.raises(ValueError):
        get_date("")
