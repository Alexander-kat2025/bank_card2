import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected", [
    ("1234567890345234", "1234 56** **** 5234"),
    ("1234567890123456", "1234 56** **** 3456"),
])
def test_get_mask_card_number(card_number, expected):
    """Тест функции маскировки номера карты"""
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_empty():
    """Тест функции маскировки номера карты, если аргумент пустой"""
    with pytest.raises(TypeError) as e_info:
        get_mask_card_number(None)
    assert str(e_info.value) == "Аргумент не передан"


def test_get_mask_card_number_wrong_type():
    """Тест функции маскировки номера карты, если неправильный тип аргумента"""
    with pytest.raises(TypeError) as e_info:
        get_mask_card_number(12345)
    assert str(e_info.value) == "Переданный аргумент должен быть строкой"


def test_get_mask_card_number_wrong_len():
    """Тест функции маскировки номера карты, если неправильная длинна строки"""
    with pytest.raises(ValueError) as e_info:
        get_mask_card_number('12345')
    assert str(e_info.value) == "В номере карты должно быть 16 цифр"


@pytest.mark.parametrize("account_number, expected", [
    ("12345678901234567890", "**7890"),
    ("12345678901234561234", "**1234")
])
def test_get_mask_account(account_number, expected):
    """Тест функции маскировки счета"""
    assert get_mask_account(account_number) == expected


def test_get_mask_account_empty():
    """Тест функции маскировки счета, если аргумент пустой"""
    with pytest.raises(TypeError) as e_info:
        get_mask_account(None)
    assert str(e_info.value) == "Аргумент не передан"


def test_get_mask_account_wrong_type():
    """Тест функции маскировки счета, если неправильный тип аргумента"""
    with pytest.raises(TypeError) as e_info:
        get_mask_account(12345)
    assert str(e_info.value) == "Переданный аргумент должен быть строкой"


def test_get_mask_account_wrong_len():
    """Тест функции маскировки счета, если неправильная длинна строки"""
    with pytest.raises(ValueError) as e_info:
        get_mask_account('12345')
    assert str(e_info.value) == "В номере счета должно быть 20 цифр"
