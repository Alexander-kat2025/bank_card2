from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Функция обрабатывает информацию о картах и счетах, выводит замаскированный номер"""
    parts = info.split()
    type_info = " ".join(parts[:-1])
    number = parts[-1]

    if "счет" in type_info.lower():
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{type_info} {masked_number}"


def get_date(date_string: str) -> str:
    """Функция принимает на вход строку с датой"""
    date_object = datetime.fromisoformat(date_string)
    formatted_date = date_object.strftime("%d.%m.%Y")

    return formatted_date


# if __name__ == '__main__':
#     print(get_date("2024-03-11T02:26:18.671407"))
