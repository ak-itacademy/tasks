'''
Задание 2.
Функции, методы, тайпинги.
'''


# Реализовать функцию, которая принимает строку и возвращает ее в обратном порядке.
def reverse(string: str) -> str:
    rev = ''
    for i in range(len(string) - 1, -1, -1):
        rev += string[i]
    return rev


print(reverse('Hello World mtf'))


# Реализовать фунекцию, которая принимает два параметра: число и степень - и возвращает это число,
# возведенное в степень.
# В случае, если степень не задана пользователем, используется значение 2.0.

def sol(number: int, pow: int = 2) -> int:
    return number ** pow


print(sol(2))


# Реализовать функцию, которая принимает произвольный набор параметров и возвращает кортеж, содержащий
# типы переданных параметров.

def types(*args):
    for arg in range(len(args)):
        if arg < len(args):
            return type(arg)
        break
    return arg


print(types('1', "str", 1.3, 1))


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
def sort_type(**kwargs):
    answer = kwargs.fromkeys(['int', 'str', 'float', 'dict'])
    i_n = []
    s = []
    f = []
    d = []
    for i in kwargs:
        if type(kwargs[i]) == int:
            i_n += ([i, kwargs[i]],)
            answer['int'] = i_n
        if type(kwargs[i]) == str:
            s += ([i, kwargs[i]],)
            answer['str'] = s
        if type(kwargs[i]) == float:
            f += ([i, kwargs[i]],)
            answer['float'] = f
        if type(kwargs[i]) == dict:
            d += ([i, kwargs[i]],)
            answer['dict'] = d
    return answer


print(sort_type(a=34, b='some text', c=2, d=1.3, e={1: 2}, f=-3.0))


# Реализовать функцию, которая принимает строку и произвольный набор неименованных и именованных параметров.
# Строка может содержать произвольный набор подстрок вида **, *index* или *name*.
# Вместо ** в строку должен быть подставлен символ *.
# Вместо *index* должен быть подставлен неименованный параметр с индексом index. Должна поддерживаться
# отрицательная индексация.
# Вместо *name* должен быть подставлен именованный параметр с именем name.

def replacement(str_, *args, **kwargs):
    st = str_.replace('**', '*')
    one_word = st.split()
    k = 0
    for i in one_word:
        if i[0] == i[-1]:
            symbol = i[1:-1]
            if symbol == "first":
                one_word[k] = kwargs['first']
            elif symbol == "second":
                one_word[k] = kwargs['second']
        k += 1

    el = 0
    for j in one_word:
        if type(j) == str:
            if j[0] == j[-1] and len(j) != 1:
                index = int(j[1])
                one_word[el] = args[index]
        el += 1

    result = [str(n) for n in one_word]
    return " ".join(result)


print(replacement('Some *first* string ** need to be formatted *2* *first* *second* *0* *2*', 111, 'string', '!!!',
                  first=5,
                  second=7, ))
