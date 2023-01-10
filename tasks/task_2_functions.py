'''
Задание 2.
Функции, методы, тайпинги.
'''


from typing import Tuple, Optional, Union


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
    return tuple(map(type, arg))


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
    my_dict = {}
    for key, value in arg.items():
        my_dict.setdefault(type(value), []).append([key, value])
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

def function(text: str, *arg, **kwargs) -> str:
    my_list = text.split("*")
    for i in range(len(my_list)):
        line = my_list[i]
        if i % 2:
            if not line:
                my_list[i] = "*"
            elif line in kwargs:
                my_list[i] = str(kwargs[line])
            else:
                try:
                    my_list[i] = str(arg[int(line)])
                except (ValueError, IndexError):
                    return "Wrong data!"

    result = "".join(my_list)
    return result


# print(function("This string contains elements ** kind of *2**-2**0*, *2*/*-2*/*0*, *2*, *1*, *0*, *param_2*, *param_3*, *param_1*, *param_0*",
#                10, "This", -29.5, param_0="Text", param_1=4, param_2=4.65, param_3=[1, 2, 3]))
