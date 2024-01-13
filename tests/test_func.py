from utils.func import new_list,new_list_2

def test_new_list():
    assert [{'date': 1, 'A': 1}, {'date': 3, 'C': 3}, {'date': 2, 'B': 2}] != [{'date': 1, 'A': 1}, {'date': 2, 'B': 2}, {'date': 3, 'C': 3} ]

def test_new_list_2():
    assert [{'date': 1, 'A': 1}, {'date': 3, 'C': 3}, {'date': 2, 'B': 2}] != [{'date': 1}, {'date': 3}, {'date': 2}]

