def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""


    if card_number is None:
        raise TypeError('Аргумент не передан')
    if not isinstance(card_number, str):
        raise TypeError("Переданный аргумент должен быть строкой")
    if len(card_number) != 16:
        raise ValueError("В номере карты должно быть 16 цифр")


    masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    return masked_card_number


def get_mask_account(card_account: str) -> str:
    """Функция маскировки номера счета"""

    if card_account is None:
        raise TypeError('Аргумент не передан')
    if not isinstance(card_account, str):
        raise TypeError("Переданный аргумент должен быть строкой")
    if len(card_account) != 20:
        raise ValueError("В номере счета должно быть 20 цифр")


    masked_account = f"**{card_account[-4:]}"

    return masked_account


# if __name__ == '__main__':
#     print(get_mask_account('12345678912345678912'))
#     print(get_mask_account(12345678912345678912))

