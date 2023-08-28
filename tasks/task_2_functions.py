'''
Задание 2.
Функции, методы, тайпинги.
'''


# Реализовать функцию, которая принимает строку и возвращает ее в обратном порядке.
def reverse_string(string: str) -> str:
    return string[::-1]


# Реализовать функцию, которая принимает два параметра: число и степень - и возвращает это число,
# возведенное в степень.
# В случае, если степень не задана пользователем, используется значение 2.0.
def power_number(number, power=2.0):
    return number ** power


# Реализовать функцию, которая принимает произвольный набор параметров и возвращает кортеж, содержащий
# типы переданных параметров.
from typing import get_type_hints


def get_param_return_tuple(*args, **kwargs) -> tuple:
    return tuple(map(type, args)) + tuple(map(type, kwargs.values()))


# Реализовать функцию, которая принимает произвольный набор именованных параметров и возвращает их
# группировку по типу в виде словаря.
# Например, если входные параметры заданы как `a=34, b='some text', c=2, d=1.3, e={1: 2}, f=-3.0`,
# то необходимо вернуть словарь следующего вида:
# {
#   int: [['a', 34], ['c', 2]],
#   str: [['b', 'some text']],
#   float: [['d', 1.3], ['f', -3.0]],
#   dict: [['e', {1: 2}]]
# }
def group_by_type(**kwargs):
    types = {}
    for key, value in kwargs.items():
        types[type(value)] = types.get(type(value), []) + [[key, value]]
    return types


# Реализовать функцию, которая принимает строку и произвольный набор неименованных и именованных параметров.
# Строка может содержать произвольный набор подстрок вида **, *index* или *name*.
# Вместо ** в строку должен быть подставлен символ *.
# Вместо *index* должен быть подставлен неименованный параметр с индексом index. Должна поддерживаться
# отрицательная индексация.
# Вместо *name* должен быть подставлен именованный параметр с именем name.

def format_string(string, *args, **kwargs):
    string = string.replace('**', '*')
    parts = string.split('*')
    for i in range(len(parts)):
        if parts[i] in kwargs:
            parts[i] = str(kwargs[parts[i]])
        elif parts[i].isdigit():
            index = int(parts[i])
            if index < 0:
                index += len(args)
            parts[i] = str(args[index])
    return ''.join(parts)
