def filter_by_state(operations, state='EXECUTED'):
    """
    Фильтрует список операций по значению ключа 'state'.

    """
    filtered_operations = []
    for operation in operations:
        if 'state' in operation and operation['state'] == state:
            filtered_operations.append(operation)
    return filtered_operations


def sort_by_date(operations, reverse=True):
    '''Функция сортирует список по дате'''
    return sorted(operations, key=lambda x: x.get('date', ''), reverse=reverse)
