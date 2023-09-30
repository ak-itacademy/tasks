'''
Задание 2.
Функции, методы, тайпинги.
'''

# 2-2-1
# Реализовать функцию, которая принимает строку и возвращает ее в обратном порядке.
def reverse_string(string):
    return string[::-1]

# 2-2-2
# Реализовать функцию, которая принимает два параметра:
# число и степень - и возвращает это число, возведенное в степень.
# В случае, если степень не задана пользователем, используется значение 2.0.
def power(base, exponent=None):
    if exponent is None:
        exponent = 2.0
    return base ** exponent

print(power(3, 4)) #  81
print(power(5)) # 25.0


# 2-2-3
# Реализовать функцию, которая принимает произвольный набор параметров
# и возвращает кортеж, содержащий типы переданных параметров.
def get_parameter_types(*args):
    return tuple(map(type, args))

print(get_parameter_types(10, "Hello", [1, 2, 3], {"a": 1, "b": 2}))
# (<class 'int'>, <class 'str'>, <class 'list'>, <class 'dict'>)


# 2-2-4
# Реализовать функцию, которая принимает произвольный набор именованных параметров
# и возвращает их группировку по типу в виде словаря.
# Например, если входные параметры заданы как
# `a=34, b='some text', c=2, d=1.3, e={1: 2}, f=-3.0`,
# то необходимо вернуть словарь следующего вида:
# {
#   int: [['a', 34], ['c', 2]],
#   str: [['b', 'some text']],
#   float: [['d', 1.3], ['f', -3.0]],
#   dict: [['e', {1: 2}]]
# }
def group_parameters(**kwargs):
    parameter_groups = {}
    for key, value in kwargs.items():
        parameter_type = type(value)
        parameter_groups.setdefault(parameter_type, []).append([key, value])
    return parameter_groups

parameters = {
    'a': 34,
    'b': 'some text',
    'c': 2,
    'd': 1.3,
    'e': {1: 2},
    'f': -3.0
}
print(group_parameters(**parameters))

# 2-2-5
# Реализовать функцию, которая принимает строку и произвольный набор неименованных и именованных параметров.
# Строка может содержать произвольный набор подстрок вида **, *index* или *name*.
# Вместо ** в строку должен быть подставлен символ *.
# Вместо *index* должен быть подставлен неименованный параметр с индексом index. Должна поддерживаться
# отрицательная индексация.
# Вместо *name* должен быть подставлен именованный параметр с именем name.
def process_string(string, *args, **kwargs):
    print(string)

    print("Формируем словарь с неименованными аргументами:")
    arguments_dict = {i: arg for i, arg in enumerate(args, 1)}
    print(arguments_dict)

    print("Формируем словарь со всеми аргументами:")
    all_arguments_dict = arguments_dict.copy()
    all_arguments_dict.update(kwargs)
    print(all_arguments_dict)

    for key, value in all_arguments_dict.items():
        string = string.replace(f"*{key}*", str(value))

    for key, value in arguments_dict.items():
        key = len(arguments_dict) + 1 - key
        string = string.replace(f"*-{str(key)}*", str(value))

    string = string.replace(f"**", "*")

    print("Результирующая строка с замененными значениями:")
    print(string)

process_string("My name is *name* *lastname*** and here is an example of a positive indexing *1*, *2*, *3* and a negative indexing *-1*, *-2*, *-3*", 10, 20, 30, name="Natalia", lastname="S")
# My name is *name* *lastname*** and here is an example of a positive indexing *1*, *2*, *3* and a negative indexing *-1*, *-2*, *-3*
# Формируем словарь с неименованными аргументами:
# {1: 10, 2: 20, 3: 30}
# Формируем словарь со всеми аргументами:
# {1: 10, 2: 20, 3: 30, 'name': 'Natalia', 'lastname': 'S'}
# Результирующая строка с замененными значениями:
# My name is Natalia S* and here is an example of a positive indexing 10, 20, 30 and a negative indexing 30, 20, 10