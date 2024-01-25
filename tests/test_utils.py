from src.utils import sorting_function, read_operations, formating_func, print_five_last_operations


def test_sorting_function():
    assert str(sorting_function({'date': '2019-08-26T10:50:58.294041'})) == "2019-08-26 10:50:58.294041"


def test_formating_func_card():
    assert formating_func("Maestro 1596837868705199") == 'Maestro 1596 83** **** 5199'


def test_formating_func_account():
    assert formating_func("Счет 35383033474447895560") == 'Счет **5560'


def test_read_operations():
    assert str(type(read_operations())) == "<class 'list'>"


def test_print_five_last_operations():
    assert print_five_last_operations() is None
