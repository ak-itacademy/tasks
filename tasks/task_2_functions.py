'''
Задание 2.
Функции, методы, тайпинги.
'''


from typing import Tuple, Optional


# Реализовать функцию, которая принимает строку и возвращает ее в обратном порядке.
def str_reverse(string: str, ) -> str:
    return string[::-1]


# test = input("Enter same text -> ")
# print(str_reverse(test))


# Реализовать фунекцию, которая принимает два параметра: число и степень - и возвращает это число,
# возведенное в степень.
# В случае, если степень не задана пользователем, используется значение 2.0.
def power_func(value: float, power=2.0) -> float:
    return value ** power


# value = float(input("Enter value -> "))
# power = float(input("Enter power -> "))
# print(power_func(value, power))


# Реализовать функцию, которая принимает произвольный набор параметров и возвращает кортеж, содержащий
# типы переданных параметров.
def type_func(*arg) -> Tuple:
    my_list = []
    for n in arg:
        my_list.append(type(n))
    return tuple(my_list)


# print(type_func(32, 56, "dfd", [3, 4, "dff"], (34, "df"), {"fdf": 3}))


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
def grouping(**arg):
    my_full_type_list = []
    my_type_list = []
    my_list = []

    for key, value in arg.items():
        my_list.append([key, value])
        type_ = str(type(value))

        if not type_ in my_full_type_list:
            my_full_type_list.append(type_)
            my_type_list.append(type_[8:-2])

    my_dict = {}

    for i in range(len(my_full_type_list)):
        temporary_list = []

        for element in my_list:

            if my_full_type_list[i] == str(type(element[1])):
                temporary_list.append(element)

        my_dict[my_type_list[i]] = temporary_list

    return my_dict


# for key, value in grouping(a=34, b='some text', c=2, d=1.3, e={1: 2}, f=-3.0,
#                            g=[3, 4], h={1, 2, 3}, i="Text", j={5, 6}).items():
#     print(key, value)


# Реализовать функцию, которая принимает строку и произвольный набор неименованных и именованных параметров.
# Строка может содержать произвольный набор подстрок вида **, *index* или *name*.
# Вместо ** в строку должен быть подставлен символ *.
# Вместо *index* должен быть подставлен неименованный параметр с индексом index. Должна поддерживаться
# отрицательная индексация.
# Вместо *name* должен быть подставлен именованный параметр с именем name.

def function(text: str, *arg, **kwargs):


    return ...
