# Реализовать функцию, которая принимает форму и возвращает ее в обратном порядке.
def rev (value):
    value.reverse()
    return value
a = [1,2,3,4,5,6]
print(rev(a))

# Реализовать функцию, которая принимает два параметра: число и степень - и возвращает это число,
# сложное в степени.
# В случае, если степень не задана пользователем, используется значение 2.0.
def square (number, degree=2):
    return number ** degree

# Реализовать функцию, которая принимает стандартный набор значений и возвращает кортеж,
# Типы передаваемых параметров.

def tpl(value: tuple):
    return value

# Реализовать функцию, которая принимает произвольный набор именных параметров и возвращает их
# группировка параметров в видео словаря.
# Например, если заданы входные параметры как `a=34, b='some text', c=2, d=1.3, e={1: 2}, f=-3.0`,
# то необходимо вернуть словарь такого вида:
# {
# int: [['a', 34], ['c', 2]],
# str: [['b', 'какой-то текст']],
# float: [['d', 1.3], ['f', -3.0]],
# дикт: [['е', {1: 2}]]
# }
def sort_type(**dict_):
    answer =dict.fromkeys(['int', 'str', 'float', 'dict'])
    i_n=[]
    s=[]
    f=[]
    d=[]
    for i in dict_:
        if type(dict_[i]) == int:
            i_n += ([i,dict_[i]],)
            answer['int'] = i_n
        elif type(dict_[i]) == str:
            s += ([i,dict_[i]],)
            answer['str'] = s
        elif type(dict_[i]) == float:
            f += ([i,dict_[i]],)
            answer['float'] = f
        elif type(dict_[i]) == dict:
            d += ([i,dict_[i]],)
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

    l = 0
    for j in one_word:
        if type(j) == str:
            if j[0] == j[-1] and len(j) != 1:
                index = int(j[1])
                one_word[l] = args[index]
        l += 1

    ansver = [str(n) for n in one_word]
    return " ".join(ansver)

print(replacement('Some *first* string ** to be formatted *2* *first* *second* *0* *2*',111, 'string', '!!!', first=5, second=7,))