from src.masks import get_mask_card_number, get_mask_account
from src.widget import get_date
from src.processing import filter_by_state, sort_by_date

print(get_mask_card_number('7000792289606361'))
print (get_mask_account("234587687879"))
print(get_date("2024-03-11T02:26:18.671407"))

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
executed_operations = filter_by_state(operations)
print("Executed Operations:", executed_operations)

canceled_operations = filter_by_state(operations, state='CANCELED')
print("Canceled Operations:", canceled_operations)

sorted_operations_desc = sort_by_date(operations)
print("Sorted Operations (Descending):", sorted_operations_desc)