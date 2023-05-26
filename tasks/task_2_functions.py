# Задание 2.
# Функции, методы, тайпинги.


# Реализовать функцию, которая принимает строку и возвращает ее в обратном порядке.
def reverse_string(s):
    return s[::-1]


# Реализовать фунекцию, которая принимает два параметра: число и степень - и возвращает это число,
# возведенное в степень.
# В случае, если степень не задана пользователем, используется значение 2.0.
def exp(number, exponent=2.0):
    return number ** exponent


# Реализовать функцию, которая принимает произвольный набор параметров и возвращает кортеж, содержащий
# типы переданных параметров.
def get_param_and_types(*args):
    return tuple(type(arg) for arg in args)

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


def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        param_type = type(value)
        if param_type not in result:
            result[param_type] = []
        result[param_type].append([key, value])
    return result

# Реализовать функцию, которая принимает строку и произвольный набор неименованных и именованных параметров.
# Строка может содержать произвольный набор подстрок вида **, *index* или *name*.
# Вместо ** в строку должен быть подставлен символ *.
# Вместо *index* должен быть подставлен неименованный параметр с индексом index. Должна поддерживаться
# отрицательная индексация.
# Вместо *name* должен быть подставлен именованный параметр с именем name.


def rep_params(string, *args, **kwargs):
    result = ''
    for i in range(len(string)):
        if string[i:i + 2] == '**':
            result += '*'
        elif string[i:i + 1] == '*':
            if string[i + 1:i + 2].isdigit():
                index = int(string[i + 1:i + 2])
                if index < 0:
                    index = len(args) + index
                result += str(args[index])
            else:
                name = string[i + 1:string.find('*', i + 1)]
                result += str(kwargs[name])
            i = string.find('*', i + 1)
        else:
            result += string[i]
    return result
