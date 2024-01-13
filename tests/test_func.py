from utils.func import new_list,new_list_2

def test_new_list():
    assert [{'A': 1, 'a': 1}, {'C': 3, 'c': 3}, {'B': 2, 'b': 2}] != [{'A': 1, 'a': 1}, {'B': 2, 'b': 2}, {'C': 3, 'c': 3}]


def test_new_list_2():
    assert [{'A': 1, 'a': 1}, {'C': 3, 'c': 3}, {'B': 2, 'b': 2}] != [{'A': 1}, {'B': 2}, {'C': 3}]
