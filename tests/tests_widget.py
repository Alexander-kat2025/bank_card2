import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("info, expected", [
    ("Карта 1234 5678 9012 3456", "Карта 1234 56**  **** 3456"),
    ("Счет 12345678901234567890", "Счет **7890"),
    ("Карта 1234 5678 9012 345", "Карта 123 45** **** 2345"),
    ("Счет 123456", "Счет **3456"),
    ("Карта abcd efgh ijkl mnop", "Карта **** **** **** ****")
])
def test_mask_account_card(info, expected):
    assert mask_account_card(info) == expected

def test_get_date_valid_and_invalid():
    assert get_date("2019-07-03T18:35:29.512364") == "(ДД.ММ.ГГГГ) 03.07.2019"
    assert get_date("2020-01-01T00:00:00") == "(ДД.ММ.ГГГГ) 01.01.2020"

    import pytest
    with pytest.raises(ValueError):
        get_date("invalid-date")

    with pytest.raises(ValueError):
        get_date("")
