import pytest
from src.processing import filter_by_state, sort_by_date
@pytest.fixture
def operations():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 2, 'state': 'CANCELED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 4, 'state': 'PENDING', 'date': '2018-10-14T08:21:33.419441'}
    ]
def test_filter_by_state(operations):
    executed = filter_by_state(operations, 'EXECUTED')
    canceled = filter_by_state(operations, 'CANCELED')
    pending = filter_by_state(operations, 'PENDING')
    unknown = filter_by_state(operations, 'UNKNOWN')
    assert len(executed) == 2
    assert len(canceled) == 1
    assert len(pending) == 1
    assert unknown == []
def test_sort_by_date(operations):
    desc_sorted = sort_by_date(operations)
    asc_sorted = sort_by_date(operations, reverse=False)

    assert desc_sorted[0]['date'] >= desc_sorted[-1]['date']
