def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""

    card_number = card_number.replace(" ", "")
    masked_card_number = " ".join(
        card_number[i : i + 4] for i in range(0, len(card_number), 4)
    )
    masked_card_number_list = list(masked_card_number)

    for i in range(len(masked_card_number_list)):
        if 7 <= i <= 13 and masked_card_number_list[i] != " ":
            masked_card_number_list[i] = "*"

    masked_card_number = "".join(masked_card_number_list)
    return masked_card_number


def get_mask_account(card_account: str) -> str:
    """Функция маскировки номера счета"""

    card_account = card_account.replace(" ", "")

    last_part = str(card_account[-4:])
    return f"**{last_part}"