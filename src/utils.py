import json
from datetime import datetime


def sorting_function(x):
    """Функция сортировки по дате. Возвращает дату в формате datetime"""
    return datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f')


def read_operations():
    """Функция считывает операции в файле operations.json, фильтрует и сортирует, возвращая список"""
    with open('../operations.json', 'r', encoding='utf-8') as file:
        operations = json.load(file)
        executed_operations = []
        needed_keys = ['date', 'from', 'to']
        for operation in operations:
            if all([key in operation.keys() for key in needed_keys]) and operation['state'] == 'EXECUTED':
                executed_operations.append(operation)
    sorted_operations = sorted(executed_operations, key=sorting_function, reverse=True)
    return sorted_operations


def formating_func(transaction):
    """Функция форматирует вывод реквизитов в зависимости от их типа"""
    information = transaction.split(" ")
    name = " ".join([i for i in information if not i.isdigit()])
    op_type = information[-1]
    if information[0] == 'Счет':
        return f"{name} **{op_type[-4:]}"
    return f"{name} {op_type[:4]} {op_type[4:6]}** {'*' * 4} {op_type[-4:]} "


def print_five_last_operations():
    """Функция выводит на экран 5 последних операций"""
    sorted_operations = read_operations()
    for i in range(5):
        operation = sorted_operations[i]
        operation_date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f')
        date_f = operation_date.strftime('%d.%m.%Y')
        amount = operation['operationAmount']
        print(f"{date_f} {operation['description']}")
        print(f"{formating_func(operation['from'])} -> {formating_func(operation['to'])}")
        print(f"{amount['amount']} {amount['currency']['name']}\n")
