#Задача для закрепления на занятии 2

#1. Запросить у пользователя три числа. Сложите первое и второе число.
#Вычтите от второго третье.

# Запросить у пользователя три числа
#num1 = float(input("Введите первое число: "))
#num2 = float(input("Введите второе число: "))
#num3 = float(input("Введите третье число: "))

# Выполнить математические операции
#result = (num1 + num2) * (num2 - num3)

# Вывести результат
#print("Результат операции равен:", result)

# 2. Задача для закрепления на занятии

# 1. Проверьте делимость числа на 17.
# 2.  число нечетное, выведите “ого”, если четное “ага”.
# 3. Если число нечетное, выведите “ого”
# если число четное, и отрицательное, выведите “маловато”,
# если число четное и положительное, выведите “нормально”,
# если число равно нулю, выведите “на нет спроса нет”.
# 4. Переписать оператор or через вложенные условные операторы.

# 2-1 вариант решения задачи:
#number = int(input("Введите число: "))

#if number % 17 == 0:
#    if number % 2 == 0:
#        if number < 0:
#            print("маловато")
#        elif number == 0:
#            print("на нет спроса нет")
#        else:
#            print("нормально")
#   else:
#        print("ого")
#else:
#    if number % 2 == 0:
#        print("ага")

# 2-2 вариант решения задачи для закрепления на занятии:

# 1. Проверьте делимость числа на 17.
# 2.  число нечетное, выведите “ого”, если четное “ага”.
# 3. Если число нечетное, выведите “ого”
# если число четное, и отрицательное, выведите “маловато”,
# если число четное и положительное, выведите “нормально”,
# если число равно нулю, выведите “на нет спроса нет”.
# 4. Переписать оператор or через вложенные условные операторы.
#number = int(input("Введите число: "))
#if number % 17 == 0:
#    if number % 2 == 0:
#       if number < 0:
#            print("маловато")
#        elif number == 0:
#            print("на нет спроса нет")
#        else:
#            print("нормально")
#    else:
#        print("ого")
#else:
#    if (number % 2 == 0) and (number < 0):
#        print("маловато")
#    elif (number % 2 == 0) and (number > 0):
#        print("нормально")
#    elif number == 0:
#        print("на нет спроса нет")
#    else:
#        print("ого")

# 3. Задача для домашнего задания:
# Даны: три стороны треугольника. Требуется: проверить, действительно ли это стороны треугольника.
# Если стороны определяют треугольник, найти его площадь. Если нет, вывести сообщение о неверных данных.

#from math import sqrt
#a = float(input("Введите длину первой стороны треугольника: "))
#b = float(input("Введите длину второй стороны треугольника: "))
#c = float(input("Введите длину третьей стороны треугольника: "))
#if a <= 0 or b <= 0 or c <= 0:
#    print("Ошибка: длина стороны не может быть меньше или равна нулю")
#elif a + b <= c or a + c <= b or b + c <= a:
#    print("Ошибка: заданные стороны не могут образовать треугольник")
#else:
#    p = (a + b + c) / 2
#    S = sqrt(p * (p - a) * (p - b) * (p - c))
#    print("Площадь треугольника равна:", S)

# Задание 2. Коллекции.
# Примечание: входные параметры ни в однй из задач не должны быть модифицированы.
# '''
#Задание 2-1
# Сконструировать и вернуть список из переданных аргументов.
#def build_list_from_args(*args) -> List:
#    ...
#В строке from typing import Any, Dict, Iterable, List, Tuple мы импортируем необходимые типы из модуля typing.

#Строка from typing import Any, Dict, Iterable, List, Tuple задает импорт модуля typing, который используется для определения типов аргументов и
# возвращаемых значений функции.
# Функция build_list_from_args определена с помощью ключевого слова def, внутри скобок указаны параметры функции.
# Аргументы функции *args означают, что в эту переменную будут переданы все позиционные аргументы функции.
# В теле функции выполняется конвертация переданных аргументов в список с помощью функции list() и возвращается этот список.
# Далее, вызывается функция build_list_from_args с произвольными аргументами, которые передаются в качестве позиционных аргументов.
# Результат сохраняется в переменную result.
# В конце кода, функция print() выводит результат работы функции, т.е. список, созданный из переданных ей аргументов.
from typing import Any, Dict, Iterable, List, Tuple

def build_list_from_args(*args) -> List:
    return list(args)

result = build_list_from_args(1, 'two', 3.0, [4, 5, 6], {'seven': 7, 'eight': 8})
print(result)

#Задание 2-2
# Сконструировать и вернуть список из переданных аргументов, имеющих тип int.
# def build_int_list_from_args(*args) -> List[int]:
# ...
from typing import Any, Dict, Iterable, List, Tuple

# Сконструировать и вернуть список из переданных аргументов, имеющих тип int.
#Данная функция build_int_list_from_args должна принимать произвольное количество аргументов и возвращать список,
# состоящий только из целочисленных значений, переданных в качестве аргументов.
# Если какой-либо из аргументов не является целым числом, то он не должен попасть в итоговый список.
def build_int_list_from_args(*args) -> List[int]:
    return [arg for arg in args if isinstance(arg, int)]
#arg - это переменная, которая ссылается на текущий элемент, который проходится в цикле.

#for arg in args - это цикл, который проходит по каждому элементу, переданному в функцию и присваивает каждый элемент переменной arg.

#arg for arg in args - начало конструкции генератора списка, которая создает список из элементов, удовлетворяющих определенному условию.
# В данном случае, она проходит по каждому элементу, переданному в функцию, и выбирает те элементы, которые имеют тип int.

#if isinstance(arg, int) - это условие, которое проверяет, является ли текущий элемент int.
# Функция isinstance() возвращает True, если первый аргумент имеет тип, указанный во втором аргументе.
# В данном случае, она проверяет, имеет ли текущий элемент тип int
result = build_int_list_from_args(1, 'two', 3.0, [4, 5, 6], {'seven': 7, 'eight': 8})
print(result) # вывод [1]

#Задание 2-3
# Сконструировать и вернуть список из переданных аргументов, имеющих заданный тип.
# def build_list_from_args_using_type(argument_type: type, *args) -> List:
# ...

from typing import Any, Dict, Iterable, List, Tuple

# Сконструировать и вернуть список из переданных аргументов, имеющих заданный тип.
def build_list_from_args_using_type(argument_type: type, *args) -> List:
    return [arg for arg in args if isinstance(arg, argument_type)]
#где def - ключевое слово, которое начинает объявление функции
#build_list_from_args_using_type - имя функции, которую мы объявляем
#argument_type: type - определение типа переменной argument_type как type, то есть типа данных
#*args - необязательный список аргументов, который может содержать любое количество переменных
#-> List - тип возвращаемого значения функции, в данном случае это список
#return - ключевое слово, которое сообщает интерпретатору Python, что функция должна вернуть значение
#[arg for arg in args if isinstance(arg, argument_type)] - выражение-генератор списка, которое отбирает только те элементы из переданных аргументов,
# которые являются экземплярами заданного типа argument_type.

result = build_list_from_args_using_type(str, 1, 'two', 3.0, [4, 5, 6], {'seven': 7, 'eight': 8})
#При вызове функции с аргументом str список фильтруется, и в результате возвращается 'two'
print(result) # вывод 'two'

#Задание 2-4
# Сконструировать и вернуть список из переданных аргументов, тип которых входит заданное множество.
# Для более эффективной работы преобразовать `argument_types` в `set`.
#def build_list_from_args_using_type_set(argument_types: Iterable, *args) -> List:
#    ...
#from typing import Any, Dict, Iterable, List, Tuple: это строка импортирует модуль typing и определяет набор типов, которые будут использоваться в коде.
# def build_list_from_args_using_type_set(argument_types: Iterable, *args) -> List: - это объявление функции с именем build_list_from_args_using_type_set.
# Функция принимает argument_types, которая является объектом Iterable и *args (аргументы переменной длины), и возвращает список.
# Функция использует аннотацию типа, чтобы указать, что она возвращает список типа List.
# allowed_types = set(argument_types): создает переменную allowed_types и присваивает ей новое множество, полученное из итерабельного объекта argument_types.
# return [arg for arg in args if type(arg) in allowed_types]: это возвращает список аргументов, тип которых есть в allowed_types. В этой строке используется
# генератор списка. Аргумент arg перебирается из *args, и если его тип содержится в множестве allowed_types, то он добавляется в новый список.
from typing import Any, Dict, Iterable, List, Tuple
def build_list_from_args_using_type_set(argument_types: Iterable, *args) -> List:
    allowed_types = set(argument_types)
    return [arg for arg in args if type(arg) in allowed_types]

#result = build_list_from_args_using_type_set([int, str], 1, 'two', 3.0, [4, 5, 6], {'seven': 7, 'eight': 8}): создает переменную result
# и присваивает ей результат выполнения функции build_list_from_args_using_type_set с аргументами [int, str], 1, 'two', 3.0, [4, 5, 6], {'seven': 7, 'eight': 8}.
#print(result): выводит на экран содержимое переменной result. В данном случае это [1, 'two'].

result = build_list_from_args_using_type_set([int, str], 1, 'two', 3.0, [4, 5, 6], {'seven': 7, 'eight': 8})
print(result)  # [1, 'two']

#Задание 2-5
# Сконструировать и вернуть список из двух списков, переданных в качестве аргументов.
#def build_list_from_two_lists(first: List, second: List) -> List:
#...
#Конечная цель задачи заключается в создании списка из элементов двух переданных списков.
#Для решения этой задачи мы используем функцию build_list_from_two_lists,
#которая принимает два аргумента типа List и возвращает новый список, содержащий все элементы из обоих переданных списков.

from typing import List
def build_list_from_two_lists(first: List, second: List) -> List:
    return first + second
list_one = [1, 2, 3]
list_two = ['a', 'b', 'c']
result = build_list_from_two_lists(list_one, list_two)
print(result)  # [1, 2, 3, 'a', 'b', 'c']

#def: Ключевое слово для определения функции в Python.
#build_list_from_two_lists: Название функции.
#first: List: Определение первого параметра функции с именем first, который должен быть типа List.
#second: List: Определение второго параметра функции с именем second, который также должен быть типа List.
#-> List: Определение возвращаемого типа функции, который должен быть List.
#return: Ключевое слово для возвращения значения из функции.
#first + second: Сложение двух переданных списков.
#list_one = [1, 2, 3]: Создание списка с элементами 1, 2 и 3.
#list_two = ['a', 'b', 'c']: Создание списка с элементами a, b и c.
#result = build_list_from_two_lists(list_one, list_two): Вызов функции build_list_from_two_lists с двумя аргументами
# и сохранение возвращаемого значения в переменную result.
#print(result): Вывод значения переменной result в консоль.

#Задание 2-6
# Сконструировать и вернуть список из неограниченного числа списков, переданных в качестве аргументов.
# def build_list_from_list_args(*lists) -> List:
# ...

from typing import List
def build_list_from_list_args(*lists) -> List:
    result = []
    for lst in lists:
        result.extend(lst)
    return result

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
result = build_list_from_list_args(list1, list2, list3)
print(result)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

#from typing import List: This line imports the List type from the typing module,
# which will be used later in the function definition to specify the function's return type.
# def build_list_from_list_args(*lists) -> List: - This is the function definition.
# The function is named build_list_from_list_args, and it takes an arbitrary number of arguments, each of which should be a list.
# The -> List: specifies that the function should return a list.
# result = []: This line creates an empty list called result. This list will be used to store the elements of the input lists.
# for lst in lists: - This is a for loop that iterates over each argument passed to the function.
# For each argument, the loop assigns the argument to a variable called lst.
# result.extend(lst): This line extends the result list with the elements of the lst list.
# The extend method is used instead of append because lst is a list itself, and using append would add the entire lst list as a single element in result.
# return result: This line returns the result list, which contains all the elements from all the input lists combined.
# list1 = [1, 2, 3], list2 = [4, 5, 6], list3 = [7, 8, 9]: These lines create three lists containing the numbers 1 through 9.
# result = build_list_from_list_args(list1, list2, list3): This line calls the build_list_from_list_args function with the three lists
# created above as arguments, and assigns the resulting list to the variable result.
# print(result) # [1, 2, 3, 4, 5, 6, 7, 8, 9]: This line prints the value of result to the console.

#Задание 2-7
# Сконструировать список из заданного элемента и значения длины (использовать умножение).
# def build_list_from_value_and_length(value: Any, length: int) -> List:
# ...

from typing import List, Any
def build_list_from_value_and_length(value: Any, length: int) -> List:
    return [value] * length
result = build_list_from_value_and_length('hello', 3)
print(result)  # ['hello', 'hello', 'hello']

#from typing: Импортирует стандартный модуль typing для использования типов данных.
# import List, Any: Импортирует тип данных List (список) и Any (любой тип данных) из модуля typing.
# def build_list_from_value_and_length(value: Any, length: int) -> List:
# Определяет функцию build_list_from_value_and_length с двумя аргументами - value (значение) и length (длина) и возвращает список.
# return [value] * length: Возвращает список, состоящий из value (значения), повторенного length (длина) раз.
# result = build_list_from_value_and_length('hello', 3): Вызывает функцию build_list_from_value_and_length с аргументами 'hello'
# и 3 и сохраняет результат в переменную result.
# print(result) # ['hello', 'hello', 'hello']: Выводит на экран список ['hello', 'hello', 'hello'].

#Задание 2-8
# Удалить из списка заданный элемент.
# def remove_value_from_list(values: List, value_to_remove: Any) -> List:
# ...

from typing import List, Any
def remove_value_from_list(values: List, value_to_remove: Any) -> List:
    return [value for value in values if value != value_to_remove]
my_list = [1, 2, 3, 2, 4, 5, 2]
result = remove_value_from_list(my_list, 2)
print(result)  # [1, 3, 4, 5]

#from typing import List, Any: импортируются типы List и Any из модуля typing для использования в аннотациях типов параметров функции.
# def remove_value_from_list(values: List, value_to_remove: Any) -> List: - объявляется функция remove_value_from_list,
# которая принимает список values и элемент value_to_remove для удаления из списка. Функция возвращает список без удаленного элемента.
# return [value for value in values if value != value_to_remove]: используется генератор списка для создания нового списка, который состоит из всех элементов values,
# кроме элемента value_to_remove. Таким образом, элементы, равные value_to_remove, удаляются из списка.
# my_list = [1, 2, 3, 2, 4, 5, 2]: создается список my_list с несколькими повторяющимися элементами.
# result = remove_value_from_list(my_list, 2): вызывается функция remove_value_from_list, которая удаляет все вхождения числа 2 из списка my_list.
# Результат сохраняется в переменной result.
# print(result): выводится результат выполнения функции, то есть список без удаленного элемента 2: [1, 3, 4, 5].

#Задание 2-9
# Удалить из списка заданный элемент, используя comprehension expression [... for .. in ...].
# def remove_value_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
# ...

from typing import List, Any
def remove_value_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
    return [value for value in values if value != value_to_remove]
my_list = [1, 2, 3, 2, 4, 5, 2]
result = remove_value_from_list_using_comprehension(my_list, 2)
print(result)  # [1, 3, 4, 5]

#from typing import List, Any: импортируются типы данных List и Any из модуля typing. List используется для указания типа списка,
# а Any - для указания типа любого значения.
# def remove_value_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:- определяется функция remove_value_from_list_using_comprehension,
# которая принимает два аргумента - values, список значений, из которого нужно удалить значение, и value_to_remove, значение, которое нужно удалить.
# Функция возвращает список.
# return [value for value in values if value != value_to_remove]: используется list comprehension для создания нового списка из значений исходного списка values,
# за исключением значения value_to_remove.
# my_list = [1, 2, 3, 2, 4, 5, 2] - создается список my_list, содержащий несколько значений.
# result = remove_value_from_list_using_comprehension(my_list, 2)- вызывается функция remove_value_from_list_using_comprehension
# с аргументами my_list и 2, результат сохраняется в переменной result.
# print(result): выводится список result.

#Задание 2-10
# Удалить из списка заданный элемент, используя `filter` и lambda-функцию.
# def remove_value_from_list_using_filter(values: List, value_to_remove: Any) -> List:
# ...
from typing import List, Any

def remove_value_from_list_using_filter(values: List, value_to_remove: Any) -> List:
    return list(filter(lambda x: x != value_to_remove, values))

my_list = [1, 2, 3, 2, 4, 5, 2]
result = remove_value_from_list_using_filter(my_list, 2)
print(result)  # [1, 3, 4, 5]

#определяется функция remove_value_from_list_using_filter, которая удаляет из списка values все элементы, равные value_to_remove, используя функцию filter и лямбда-функцию.
# Функция filter фильтрует итерируемый объект, возвращая только те элементы, для которых переданная ей функция вернет True.
# В данном случае используется лямбда-функция, которая принимает аргумент x и возвращает True, если x не равен value_to_remove.
# Таким образом, функция filter вернет итератор, который содержит все элементы списка values, за исключением тех, которые равны value_to_remove.
# Чтобы получить список из этого итератора, вызывается функция list.
# Наконец, функция remove_value_from_list_using_filter возвращает этот список.
# В конце кода создается список my_list и вызывается функция remove_value_from_list_using_filter для удаления всех элементов со значением 2.
# Результат сохраняется в переменной result и выводится на экран.

#Задание 2-11
# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
# def remove_values_from_list(values: List, values_to_remove: Iterable) -> List:
# ...

from typing import List, Iterable
def remove_values_from_list(values: List, values_to_remove: Iterable) -> List:
    values_to_remove = set(values_to_remove)  # преобразование в множество
    return [x for x in values if x not in values_to_remove]  # генератор списков для создания нового списка
my_list = [1, 2, 3, 2, 4, 5, 2]
values_to_remove = [2, 4]
result = remove_values_from_list(my_list, values_to_remove)
print(result)  # [1, 3, 5]

# 1. Преобразуем итерируемый объект values_to_remove в множество set, чтобы быстро проверять наличие элементов при фильтрации списка values.
# 2. Используем генератор списков, чтобы создать новый список, исключив из него заданные элементы.
# 3. Cоздаем список my_list.
# 4. Cоздаемсписок values_to_remove, содержащий элементы, которые нужно удалить.
# 5. Вызываем функцию remove_values_from_list с этими аргументами и сохраняем результат в переменной result.
# 6. Результат выводится на экран.

#Задание 2-12
# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
# def remove_values_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
# ...
from typing import List, Any
def remove_values_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
    values_to_remove = set(value_to_remove)  # преобразование в множество
    return [x for x in values if x not in values_to_remove]  # генератор списков для создания нового списка
my_list = [1, 2, 3, 2, 4, 5, 2]
values_to_remove = [2, 4]
result = remove_values_from_list_using_comprehension(my_list, values_to_remove)
print(result)  # [1, 3, 5]

# Задание 2-14
# Удалить из списка дублирующиеся значения (использовать преобразование в `set` и обратно).
# def remove_duplicates_from_list(values: List) -> List:
# ...
# def remove_duplicates_from_list(values: List) -> List:
#     set_values = set(values)  # преобразование списка в множество
#    new_values = list(set_values)  # преобразование множества в список
#     return new_values
# values = [1, 2, 3, 2, 4, 5, 2]
# result = remove_duplicates_from_list(values)
# print(result)  # [1, 2, 3, 4, 5]

# Задание 2-13
# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
# Использовать `filter` и lambda-функцию.
# def remove_values_from_list_using_filter(values: List, value_to_remove: Any) -> List:
# ...
from typing import List, Any
def remove_values_from_list_using_filter(values: List, values_to_remove: Any) -> List:
    # Преобразуем values_to_remove в множество для быстрого поиска
    values_to_remove = set(values_to_remove)
    # Используем filter и lambda-функцию для фильтрации значений
    filtered_values = filter(lambda x: x not in values_to_remove, values)
    # Преобразуем отфильтрованные значения из filter-объекта в список
    result = list(filtered_values)
    return result
values = [1, 2, 3, 2, 4, 5, 2]
values_to_remove = [2, 3]
result = remove_values_from_list_using_filter(values, values_to_remove)
print(result)  # [1, 4, 5]
# 1.	Создаем функцию remove_values_from_list_using_filter с параметрами values и values_to_remove, которая будет возвращать список.
# 2.	Преобразуем список values_to_remove в множество, чтобы быстро находить элементы для удаления.
# 3.	Используем функцию filter, которая позволяет фильтровать значения из списка values по заданному условию, применяя функцию lambda для каждого элемента.
#       Функция lambda проверяет, не содержится ли текущий элемент в множестве values_to_remove. Если содержится, то элемент не попадает в результирующий список.
# 4.	Применяем фильтр к списку values и сохраняем результат в переменной filtered_values.
# 5.	Преобразуем filtered_values из типа filter в список, вызвав функцию list.
# 6.	Возвращаем список result.
# 7.	Создаем список values с некоторыми повторяющимися элементами.
# 8.	Создаем список values_to_remove с элементами, которые нужно удалить из values.
# 9.	Вызываем функцию remove_values_from_list_using_filter с параметрами values и values_to_remove.
# 10.	Выводим результат работы функции на экран.

# Задание 2-14
# Удалить из списка дублирующиеся значения (использовать преобразование в `set` и обратно).
# def remove_duplicates_from_list(values: List) -> List:
# ...
from typing import List
def remove_duplicates_from_list(values: List) -> List:
    # Преобразуем список во множество, чтобы удалить дубликаты
    unique_values = set(values)
    # Преобразуем множество обратно в список
    result = list(unique_values)
    return result
values = [1, 2, 3, 2, 4, 5, 2]
result = remove_duplicates_from_list(values)
print(result)  # [1, 2, 3, 4, 5]
# 1.	Импортируем тип List из модуля typing.
# 2.	Создаем функцию remove_duplicates_from_list, которая принимает на вход список values и возвращает список без дублирующихся элементов.
# 3.	Преобразуем список values во множество unique_values, чтобы удалить дублирующиеся элементы.
# 4.	Преобразуем множество unique_values обратно в список result.
# 5.	Возвращаем result.
# 6.	Создаем список values, содержащий дубликаты элементов.
# 7.	Вызываем функцию remove_duplicates_from_list и передаем в нее список values.
# 8.	Выводим результат выполнения функции на экран.

# Задание 2-15
# Создать и вернуть словарь из заданного набора именованных аргументов, значения которых имеют тип int.
# def build_dict_from_named_arguments_of_type_int(*kwargs) -> Dict:
# ...
from typing import Dict
def build_dict_from_named_arguments_of_type_int(**kwargs) -> Dict:
    result_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, int):
            result_dict[key] = value
    return result_dict
result = build_dict_from_named_arguments_of_type_int(a=1, b='two', c=3.0, d=4, e=5.0)
print(result)  # {'a': 1, 'd': 4}
# 1.	Определение функции build_dict_from_named_arguments_of_type_int принимает неопределенное количество именованных аргументов **kwargs и возвращает словарь типа Dict.
# 2.	Создается пустой словарь result_dict.
# 3.	В цикле for проходим по каждой паре ключ-значение в словаре kwargs, используя метод items().
# 4.	Внутри цикла проверяем, является ли значение value целым числом, используя функцию isinstance().
# Если да, то добавляем в словарь result_dict пару ключ-значение key: value.
# 5.	Возвращаем результат в виде словаря result_dict.
# 6.	Вызываем функцию с именованными аргументами a=1, b='two', c=3.0, d=4, e=5.0.
# 7.	Функция возвращает словарь, содержащий только ключи с целочисленными значениями. Таким образом, в результате выполнения функции получаем словарь {'a': 1, 'd': 4}.

# Задание 2-16
# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - None (dict.fromkeys).
# def build_dict_from_keys(values: Iterable) -> Dict:
# ...
from typing import Dict, Iterable
def build_dict_from_keys(values: Iterable) -> Dict:
    return dict.fromkeys(values)
keys = ['a', 'b', 'c', 'd', 'e']
result = build_dict_from_keys(keys)
print(result)  # {'a': None, 'b': None, 'c': None, 'd': None, 'e': None}
# 1.	Импортировать необходимые модули: from typing import Dict, Iterable
# 2.	Объявить функцию с названием build_dict_from_keys, которая принимает один аргумент values типа Iterable и
# возвращает словарь типа Dict: def build_dict_from_keys(values: Iterable) -> Dict:
# 3.	В теле функции, вернуть словарь, используя метод dict.fromkeys(): return dict.fromkeys(values)
# 4.	Создать список keys с ключами: keys = ['a', 'b', 'c', 'd', 'e']
# 5.	Вызвать функцию build_dict_from_keys(), передав ей список keys в качестве аргумента: result = build_dict_from_keys(keys)
# 6.	Вывести результат на экран: print(result) # {'a': None, 'b': None, 'c': None, 'd': None, 'e': None}

# Задание 2-17
# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - значение по-умолчанию.
# def build_dict_from_keys_and_default(values: Iterable, default: Any) -> Dict:
# ...

# 1. Импортировать необходимые модули и функции:
from typing import Dict, Iterable, Any
# 2. Определить функцию с двумя аргументами - итерируемым значением (values) и значением по умолчанию (default):
def build_dict_from_keys_and_default(values: Iterable, default: Any) -> Dict:
# 3. Внутри функции использовать метод dict.fromkeys для создания словаря с заданными ключами и значением по умолчанию:
    return dict.fromkeys(values, default)
# 4. Создать список ключей и значение по умолчанию:
keys = ['a', 'b', 'c', 'd', 'e']
default_value = 0
# 5. Вызвать функцию с указанными аргументами:
result = build_dict_from_keys_and_default(keys, default_value)
# 6. Вывести результат на экран:
print(result)  # {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}

# Задание 2-18
# Создать и вернуть словарь, ключами которого являются индексы элементов,
# а значениями - значения элементов iterable параметров (использовать enumerate и dict comprehension).
# def build_dict_from_indexed_values(values: Iterable) -> Dict:
# ...
from typing import Dict, Iterable
def build_dict_from_indexed_values(values: Iterable) -> Dict:
    return {index: value for index, value in enumerate(values)}
values = ['apple', 'banana', 'cherry', 'date']
result = build_dict_from_indexed_values(values)
print(result) # {0: 'apple', 1: 'banana', 2: 'cherry', 3: 'date'}
# 1.	Импортируем типы данных Dict и Iterable из модуля typing.
# 2.	Определяем функцию build_dict_from_indexed_values, которая принимает на вход iterable значений.
# 3.	Создаем словарь, используя dict comprehension, где ключами будут индексы элементов, а значениями - сами элементы.
# a. Функция enumerate(values) возвращает итератор, который генерирует пары (индекс, значение) для каждого элемента в списке values.
# b. Используем генератор словарей для создания словаря, где для каждой пары (индекс, значение) создаем ключ словаря index и связываем его с соответствующим значением value.
# 4.	Создаем список values для использования в функции: ['apple', 'banana', 'cherry', 'date'].
# 5.	Вызываем функцию build_dict_from_indexed_values с аргументом values и сохраняем результат в переменную result.
# 6.	Выводим результат на экран.
# Результатом выполнения программы будет словарь, где ключи - целые числа от 0 до n-1 (где n - количество элементов в списке values),
# а значениями будут соответствующие элементы из списка values.

# Задание 2-19
# Создать и вернуть словарь, собранный на основе списка пар ключ-значение.
# def build_dict_from_key_value_pairs(kws: List[Tuple) -> Dict:
# ...
from typing import List, Tuple, Dict
def build_dict_from_key_value_pairs(kws: List[Tuple]) -> Dict:
    return dict(kws)
key_value_pairs = [('a', 1), ('b', 2), ('c', 3)]
result = build_dict_from_key_value_pairs(key_value_pairs)
print(result)  # {'a': 1, 'b': 2, 'c': 3}
# 1.	Импортируем необходимые типы данных из модуля typing: List, Tuple, Dict.
# 2.	Определяем функцию build_dict_from_key_value_pairs с аргументом kws типа List[Tuple] и возвращающую словарь типа Dict:
# a. Используем метод dict с аргументом kws для создания словаря из списка пар ключ-значение.
# b. Возвращаем полученный словарь.
# 3.	Присваиваем значение переменной key_value_pairs в виде списка кортежей, каждый из которых содержит два элемента - ключ и значение: [('a', 1), ('b', 2), ('c', 3)].
# 4.	Вызываем функцию build_dict_from_key_value_pairs с аргументом key_value_pairs.
# 5.	Распечатываем полученный результат с помощью функции print.

# Задание 2-20
# Создать и вернуть словарь, собранный из двух списков, один из которых
# содержит ключ, а второй - соответствующее значение (использовать zip).
# def build_dict_from_two_lists(keys: List, values: List) -> Dict:
# ...
from typing import List, Dict
def build_dict_from_two_lists(keys: List, values: List) -> Dict:
    pairs = zip(keys, values)
    result = dict(pairs)
    return result
keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = build_dict_from_two_lists(keys, values)
print(result)  # {'a': 1, 'b': 2, 'c': 3}
# 1.    Импортируем необходимые типы данных из модуля typing.
# 2.    Создаем функцию build_dict_from_two_lists, которая принимает два аргумента: список keys и список values, и возвращает словарь типа Dict.
# 3.	Создаем пары ключ-значение с помощью функции zip, передав ей список ключей и список значений.
# 4.	Применяем функцию dict к итератору, создавая словарь, где элементы из списка keys используются в качестве ключей, а элементы из списка values - в качестве значений.
# 5.	Возвращаем полученный словарь.
# 6.	Создаем два списка keys и values, содержащих ключи и значения, соответственно.
# 7.	Вызываем функцию build_dict_from_two_lists с аргументами keys и values, присваивая результат переменной result.
# 8.	Выводим на экран содержимое переменной result.

# Задание 2-21
# Сформировать из двух словарей и вернуть его. В случае, если ключи совпадают,
# использовать значение из второго словаря (dict.update).
# def build_dict_using_update(first: Dict, second: Dict) -> Dict:
# ...
from typing import Dict
def build_dict_using_update(first: Dict, second: Dict) -> Dict:
    # Создаем копию первого словаря
    result = first.copy()
    # Обновляем значения из второго словаря
    result.update(second)
    # Возвращаем объединенный словарь
    return result

# Запрашиваем значения для первого словаря
first = {}
n = int(input("Введите количество элементов для первого словаря: "))
for i in range(n):
    key = input("Введите ключ для первого словаря: ")
    value = input("Введите значение для первого словаря: ")
    first[key] = value

# Запрашиваем значения для второго словаря
second = {}
m = int(input("Введите количество элементов для второго словаря: "))
for i in range(m):
    key = input("Введите ключ для второго словаря: ")
    value = input("Введите значение для второго словаря: ")
    second[key] = value

# Вызываем функцию и передаем ей два словаря
result = build_dict_using_update(first, second)

# Выводим результат
print("Результат объединения двух словарей:")
print(result)


# Задание 2-22
# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Заменить значение в случае совпадения ключей.
# def update_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
# return ...
from typing import Dict
def update_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    """
    Обновляет словарь `dictionary` с помощью именованных аргументов `**kwargs`.
    Если ключ уже существует в словаре `dictionary`, значение будет заменено новым значением.
    Возвращает обновленный словарь.
    """
    # Обновляем словарь `dictionary` значениями из `**kwargs`
    dictionary.update(kwargs)
    # Возвращаем обновленный словарь
    return dictionary
# Создаем словарь
my_dict = {'a': 1, 'b': 2}
# Обновляем словарь с помощью именованных аргументов
my_dict = update_dict_using_kwargs(my_dict, b=3, c=4)
# Выводим обновленный словарь
print(my_dict)  # {'a': 1, 'b': 3, 'c': 4}

# Задание 2-23-1 вариант
# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Объединить значения в список в случае совпадения ключей.
# def update_and_merge_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
# return ...
from typing import Dict

def update_and_merge_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    """
    Обновляет словарь `dictionary` с помощью именованных аргументов `**kwargs`.
    Если ключ уже существует в словаре `dictionary`, значение будет добавлено в список значений этого ключа.
    Возвращает обновленный словарь.
    """
    for key, value in kwargs.items():
        if key in dictionary:
            if not isinstance(dictionary[key], list):# Проверяем, является ли значение, связанное с ключом key, не списком.
                dictionary[key] = [dictionary[key], value] #Если значение не является списком, то оно заменяется на список, содержащий старое и новое значения.
            dictionary[key].append(value) #Добавляем новое значение в список, который уже существует в словаре dictionary по заданному ключу key.
        else:
            dictionary[key] = value #Создаем новый элемент словаря, где ключу key присваивается значение value.
    return dictionary #Возвращаем обновленный словарь
# Создаем словарь
my_dict = {'a': 1, 'b': 2}

# Обновляем словарь с помощью именованных аргументов
my_dict = update_and_merge_dict_using_kwargs(my_dict, b=3, c=4, a=5)

# Выводим обновленный словарь
print(my_dict)  # {'a': [1, 5], 'b': [2, 3], 'c': 4}


# Задание 2-23-2 вариант решения с тернарным оператором

# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Объединить значения в список в случае совпадения ключей.
# def update_and_merge_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
# return ...
from typing import Dict
def update_and_merge_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    """
    # Если ключ уже существует в словаре dictionary и значение, связанное с ключом key, не является списком,
    то создается новый список из старого значения и нового значения и присваивается в словарь по ключу key.
    Если ключ не существует в словаре или значение, связанное с ключом key, уже является списком,
    то новое значение присоединяется к списку, связанному с ключом key.
    """
# Используя цикл for и метод items() для перебора всех элементов kwargs, обрабатывается каждый ключ-значение.
    for key, value in kwargs.items():

# dictionary[key] - обращение к значению в словаре с ключом key.
# = [dictionary[key], value] - присвоение значения, которое является списком из двух элементов: старое значение в словаре с ключом key и значение из kwargs.
# if key in dictionary and not isinstance(dictionary[key], list) - проверка, что ключ key уже существует в словаре dictionary, и что значение, связанное с ключом key,
# не является списком. Если это так, то выполнится первое выражение [dictionary[key], value].
# else - иначе, если ключ key не существует в словаре или значение, связанное с ключом key, уже является списком, то выполнится следующее выражение:
# dictionary.get(key, []) - обращение к значению словаря с ключом key, но в случае, если ключа key еще нет в словаре, вернется пустой список [].
# + [value] - объединение списка значений, связанных с ключом key и новым значением value.
# Если ключ key не существует в словаре, вернется пустой список, который будет объединен с новым значением value в список из одного элемента [value].
        dictionary[key] = [dictionary[key], value] if key in dictionary and not isinstance(dictionary[key], list) else dictionary.get(key, []) + [value]
    return dictionary

# Создаем словарь
my_dict = {'a': 1, 'b': 2}

# Обновляем словарь с помощью именованных аргументов
my_dict = update_and_merge_dict_using_kwargs(my_dict, b=3, c=4, a=5)

# Выводим обновленный словарь
print(my_dict)  # {'a': [1, 5], 'b': [2, 3], 'c': 4}


# Задание 2-24
# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Объединить значения в список в случае совпадения ключей.
# def update_and_merge_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
# return ...

from typing import Dict
def update_and_merge_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    for key, value in kwargs.items():
        if key in dictionary:
            if isinstance(dictionary[key], list):
                dictionary[key].append(value)
            else:
                dictionary[key] = [dictionary[key], value]
        else:
            dictionary[key] = value
    return dictionary
my_dict = {'a': 1, 'b': 2}
updated_dict = update_and_merge_dict_using_kwargs(my_dict, a=3, b=4, c=5)
print(updated_dict)
# {'a': [1, 3], 'b': [2, 4], 'c': 5}

# Задание 2-25
# Объединить два словарь и вернуть результат.
# Объединить значения в список в случае совпадения ключей.
# def merge_two_dicts(first: Dict, second: Dict) -> Dict:
# return ...

from typing import Dict

def merge_two_dicts(first: Dict, second: Dict) -> Dict:
    # Копируем содержимое первого словаря first в merged_dict
    merged_dict = first.copy()

    # Перебираем все ключи и значения второго словаря second
    for key, value in second.items():
        # Проверяем, существует ли ключ key в словаре merged_dict
        if key in merged_dict:
            # Проверяем, является ли значение с ключом key списком
            if isinstance(merged_dict[key], list):
                # Если значение является списком, добавляем value в конец списка
                merged_dict[key].append(value)
            else:
                # Если значение не является списком, создаем новый список с текущим значением и value
                merged_dict[key] = [merged_dict[key], value]
        else:
            # Если ключ key не существует в merged_dict, добавляем его со значением value
            merged_dict[key] = value

    # Возвращаем словарь merged_dict как результат объединения
    return merged_dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 3, 'c': 4}
merged_dict = merge_two_dicts(dict1, dict2)
print(merged_dict)
# {'a': [1, 3], 'b': 2, 'c': 4}


# Задание 2-26
# Объединить два словарь и вернуть результат.
# В случае совпадения ключей:
# - объединить значения рекурсивно, если оба значения - словари;
# - объединить значения в один список, если оба значения - списки;
# - объединить значения в одно множество, если оба значения - множества;
# - объединить значения в список в любом другом случае.
# def deep_merge_two_dicts(first: Dict, second: Dict) -> Dict:
# return ...

from typing import Dict, Any

def deep_merge_two_dicts(first: Dict, second: Dict) -> Dict:
# Создаем копии первого словаря для сохранения оригинала
    merged_dict = first.copy()

# Перебираем ключи и значения второго словаря
    for key, value in second.items():
        if key in merged_dict:
# Проверяем, является ли значение, связанное с ключом key в словаре merged_dict, словарем.
# И проверяем, является ли значение из второго словаря value словарем.
            if isinstance(merged_dict[key], dict) and isinstance(value, dict):
# Рекурсивное объединение словарей
                merged_dict[key] = deep_merge_two_dicts(merged_dict[key], value)
# Проверяем, являются ли значения списками
            elif isinstance(merged_dict[key], list) and isinstance(value, list):
# Расширяем список, находящийся в значении merged_dict[key],
# путем добавления элементов из списка value
                merged_dict[key].extend(value)
# Проверяем, являются ли значения множествами
            elif isinstance(merged_dict[key], set) and isinstance(value, set):
# Объединение множеств
                merged_dict[key].update(value)
            else:
# Обрабатываем случаи, когда значения не являются контейнерами (т.е. не являются словарями, списками или множествами).
# Значения объединяются в список.
                merged_dict[key] = [merged_dict[key], value]
        else:
# Добавляем новый ключ и значение в объединенный словарь
            merged_dict[key] = value
# Возвращаем объединенный словарь
    return merged_dict

dict1 = {'a': {'x': 1, 'y': 2}, 'b': [3, 4]}
dict2 = {'a': {'y': 3, 'z': 4}, 'b': [5, 6], 'c': {7, 8}}

# Вызываем функцию для объединения двух словарей
merged_dict = deep_merge_two_dicts(dict1, dict2)

# Вывододим результат объединения
print(merged_dict)
# {'a': {'x': 1, 'y': [2, 3], 'z': 4}, 'b': [3, 4, 5, 6], 'c': {8, 7}}


# Задание 2-27
# Вернуть список, состоящий из ключей, принадлежащих словарю.
# def get_keys(dictionary: Dict) -> List:
# ...

from typing import Dict, List

def get_keys(dictionary: Dict) -> List:
    # Инициализируем пустой список, в который будем добавлять ключи
    keys = []

    # Перебираем все ключи в словаре
    for key in dictionary.keys():
        # Добавляем текущий ключ в список keys
        keys.append(key)

    # Возвращаем список ключей
    return keys

# Создаем словарь
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Вызываем функцию get_keys и сохраняем результат
result = get_keys(my_dict)

# Выводим результат
print(result) #['a', 'b', 'c']


# Задание 2-28
# Вернуть список, состоящий из значений, принадлежащих словарю.
# def get_values(dictionary: Dict) -> List:
# ...

from typing import Dict, List

def get_values(dictionary: Dict) -> List:
# Инициализируем пустой список, в который будем добавлять значения
    values = []

# Перебираем все значения в словаре с помощью цикла for и переменной value
    for value in dictionary.values():
# Добавляем текущее значение в список values на каждой итерации цикла
        values.append(value)

# После перебора всех значений в словаре возвращаем список значений из функции
    return values

# Создаем словарь
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Вызываем функцию get_values с аргументом my_dict и
# сохраняем результат в переменную result
result = get_values(my_dict)

# Выводим результат
print(result) # список [1, 2, 3], который содержит значения из словаря my_dict


# Задание 2-29
# Вернуть список, состоящий из пар ключ-значение, принадлежащих словарю.
# def get_key_value_pairs(dictionary: Dict) -> List[Tuple]:
# ...
from typing import Dict, List, Tuple

def get_key_value_pairs(dictionary: Dict) -> List[Tuple]:
    # Инициализируем пустой список, в который будем добавлять пары ключ-значение
    key_value_pairs = []

    # Перебираем все элементы (ключи и значения) в словаре с помощью метода items()
    for key, value in dictionary.items():
        # На каждой итерации цикла создаем кортеж pair из текущей пары ключ-значение
        pair = (key, value)

        # Добавляем текущую пару ключ-значение в список key_value_pairs
        key_value_pairs.append(pair)

    # Возвращаем список пар ключ-значение
    return key_value_pairs


# Создаем словарь
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Вызываем функцию get_key_value_pairs и сохраняем результат
result = get_key_value_pairs(my_dict)

# Выводим результат
print(result) # [('a', 1), ('b', 2), ('c', 3)]


# Задание 2-30
# Реверсировать и вернуть словарь. def reverse_dict(dictionary: Dict) -> Dict:    ...
from typing import Dict

def reverse_dict(dictionary: Dict) -> Dict:
# Инициализируем пустой словарь, в который будем добавлять реверсированные пары ключ-значение
    reversed_dict = {}

# Перебираем все элементы (ключи и значения) в исходном словаре с помощью метода items(),
# который возвращает пары (ключ, значение).
    for key, value in dictionary.items():
# На каждой итерации цикла меняем местами ключ и значение и добавляем их в реверсированный словарь reversed_dict.
# То есть, ранее значение становится ключом, а ранее ключ становится значением.
        reversed_dict[value] = key

    # Возвращаем реверсированный словарь
    return reversed_dict

# Создаем исходный словарь
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Вызываем функцию reverse_dict и сохраняем результат
result = reverse_dict(my_dict)

# Выводим результат
print(result) # {1: 'a', 2: 'b', 3: 'c'}


# Задание 2-31
# Удалить из словаря элементы, имеющие пустые значения (None, '', [], {}).
# def clear_dummy_elements(dictionary: Dict) -> Dict:
# ...

from typing import Dict
def clear_dummy_elements(dictionary: Dict) -> Dict:
    # Создаем новый словарь, куда будем добавлять только непустые элементы
    cleaned_dict = {}

    # Перебираем все элементы входного словаря
    for key, value in dictionary.items():
        # Проверяем, является ли значение пустым (None, '', [], {})
        if value is not None and value != '' and value != [] and value != {}:
            # Добавляем непустой элемент в новый словарь
            cleaned_dict[key] = value

    # Возвращаем очищенный словарь без пустых элементов
    return cleaned_dict

# Исходный словарь
my_dict = {'a': 1, 'b': None, 'c': '', 'd': [1, 2, 3], 'e': {}}

# Вызываем функцию clear_dummy_elements и сохраняем результат
result = clear_dummy_elements(my_dict)

# Выводим результат
print(result) # {'a': 1, 'd': [1, 2, 3]}


# Задание 2-32
# Удалить из словаря дублирующиеся и пустые элементы.
# def clear_dummy_and_duplicate_elements(dictionary: Dict) -> Dict:    ...

from typing import Dict

def clear_dummy_and_duplicate_elements(dictionary: Dict) -> Dict:
    # Создаем новый словарь, куда будем добавлять только уникальные и непустые элементы
    cleaned_dict = {}

    # Создаем множество для отслеживания уникальных значений
    unique_values = set()

    # Перебираем все элементы входного словаря
    for key, value in dictionary.items():
        # Проверяем, является ли ключ или значение пустым
        if key not in cleaned_dict and value is not None and value != '' and value != [] and value != {}:
            # Проверяем, присутствует ли уже значение в множестве уникальных значений
            if value not in unique_values:
                # Добавляем элемент в новый словарь и в множество уникальных значений
                cleaned_dict[key] = value
                unique_values.add(value)

    # Возвращаем очищенный словарь без дублирующихся ключей и значений
    return cleaned_dict

# Исходный словарь
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': '', 'f': [], 'g': 1}

# Вызываем функцию clear_dummy_and_duplicate_elements и сохраняем результат
result = clear_dummy_and_duplicate_elements(my_dict)

# Выводим результат
print(result)  # {'a': 1, 'b': 2, 'c': 3}


# Задание 2-33
# Обменять в словаре ключи и значения
# (в качестве значений могут выступать только неизменяемые значения).
# def swap_dict_keys_and_values(dictionary: Dict) -> Dict:    ...

from typing import Dict

def swap_dict_keys_and_values(dictionary: Dict) -> Dict:
    # Проверяем, что все значения в словаре являются неизменяемыми типами данных
    for value in dictionary.values():
        if not isinstance(value, (int, float, str, tuple)):
            return None

    # Возвращаем словарь с обмененными ключами и значениями
    return {value: key for key, value in dictionary.items()}


# Исходный словарь
my_dict = {'a': 1, 'b': 2.5, 'c': 'hello', 'd': (1, 2, 3), 'e': [4, 5, 6], 'f': {'x': 7, 'y': 8}}

# Вызываем функцию swap_dict_keys_and_values и сохраняем результат
result = swap_dict_keys_and_values(my_dict)

# Проверяем результат
if result is None:
    # Выводим сообщение об ошибке, если значения в словаре не являются неизменяемыми типами данных
    print("Values must be immutable types")
else:
    # Выводим результат, если значения в словаре являются неизменяемыми типами данных
    print(result) # Values must be immutable types

# Задание 2-34
# Вернуть словарь, отсортированный по ключу. Ключи могут иметь только тип int.
def sort_dict_with_int_keys(dictionary):
    sorted_dict = {}
    keys = sorted(dictionary.keys())
    for key in keys:
        sorted_dict[key] = dictionary[key]
    return sorted_dict


# Задание 2-35

# Вернуть словарь, отсортированный по ключу в обратном порядке.
# Ключи могут иметь только тип int.
from typing import Dict

def sort_dict_backward_with_int_keys(dictionary: Dict) -> Dict:
    # Сортировка словаря по ключу в обратном порядке
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[0], reverse=True))
    return sorted_dict

my_dict = {3: 'значение3', 1: 'значение1', 5: 'значение5', 2: 'значение2', 4: 'значение4'}

# Вызываем функцию sort_dict_backward_with_int_keys() с нашим словарем
sorted_dict = sort_dict_backward_with_int_keys(my_dict)

# Выводим отсортированный словарь
print(sorted_dict) # {5: 'значение5', 4: 'значение4', 3: 'значение3', 2: 'значение2', 1: 'значение1'}


# Задание 2-36

# Вернуть словарь, элементы которого сгруппированы по типу ключа.
# В качестве ключей могут выступать: целые числа, дробные числа и строки.
# Приоритет сортировки групп (от высшего к низшему): целые числа, дробные числа, строки.
# Внутри каждой из групп отсортировать элементы по значениям ключа в обратном порядке.
# def group_dict_elements_by_key_type_and_sort(dictionary: Dict) -> Dict:
# ...
from typing import Dict
from collections import defaultdict

def group_dict_elements_by_key_type(dictionary: Dict) -> Dict:
    # Создаем словарь с группированными элементами, чтобы создавать новые пустые списки
    # для каждой группы, если они не существуют.
    grouped_dict = defaultdict(list)

    # Проходим по ключам и значениям и добавляем их в соответствующую группу
    for key, value in dictionary.items():
        if isinstance(key, int):
            grouped_dict["int"].append((key, value))
        elif isinstance(key, float):
            grouped_dict["float"].append((key, value))
        elif isinstance(key, str):
            grouped_dict["str"].append((key, value))
        else:
            # Если тип ключа не подходит ни под одну группу, игнорируем его
            pass

    # Преобразуем словарь с группами в обычный словарь с помощью генератора словаря
    result_dict = {group: dict(items) for group, items in grouped_dict.items()}

    return result_dict

# Определяем входной словарь
input_dict = {
    10: 'value1',
    3.14: 'value2',
    'key3': 'value3',
    20: 'value4',
    'key5': 'value5',
    2.718: 'value6'
}

# Вызываем функцию и выводим результат
result = group_dict_elements_by_key_type(input_dict)
print(result)


# Задание 2-37
# Подсчитать количество элементов словаря, имеющих числовой тип, значение которых находится
# в интервале [-10, 25].
# def count_dict_elements(dictionary: Dict) -> Dict:
# ...

from typing import Dict
def count_dict_elements(dictionary: Dict) -> Dict:
    # Инициализация счетчиков
    int_count = 0
    non_int_count = 0

    # Перебираем ключи и значения словаря
    for key, value in dictionary.items():
        # Проверяем, является ли значение числовым и находится ли в интервале [-10, 25]
        if isinstance(value, (int, float)) and -10 <= value <= 25:
            int_count += 1
        elif isinstance(value, (int, float)):
            non_int_count += 1

    # Возвращаем словарь с результатами
    return {"int": int_count, "non_int": non_int_count}

# Определяем входной словарь
input_dict = {
    'key1': 15,
    'key2': -5,
    'key3': 30,
    'key4': 20.5,
    'key5': 'value'
}

# Вызываем функцию подсчета и выводим результат
result = count_dict_elements(input_dict)
print(result) # {"int": 2, "non_int": 2}


# Задание 2-38
# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
# def build_dict_from_two_unaligned_lists(keys: List, values: List) -> Dict:
# ...
from typing import List, Dict
# Определение функции, принимающей два списка: keys (список ключей)
# и values (список значений) и возвращающей словарь.
def build_dict_from_two_unaligned_lists(keys: List, values: List) -> Dict:

    # Инициализация словаря
    result_dict = {}

    # Перебор элементов ключевого списка
    for index, key in enumerate(keys):
        # Проверка наличия соответствующего значения, т.е. находится ли текущий индекс
        # в пределах длины списка values, чтобы убедиться,
        # что у нас есть соответствующее значение для текущего ключа
        if index < len(values): #  Если текущий индекс index находится в пределах длины
            # списка values, то мы присваиваем переменной value соответствующее значение из списка values по этому индексу
            value = values[index]
        else:
            value = None

        # Добавление пары ключ-значение в словарь
        result_dict[key] = value

    # Возврат полученного словаря
    return result_dict

# Определение ключей и значений списка
keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3]

# Вызов функции построения словаря
result = build_dict_from_two_unaligned_lists(keys, values)
print(result) # {'a': 1, 'b': 2, 'c': 3, 'd': None, 'e': None}


# Задание 2-39
# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение, заданное по-умолчанию.
# def build_dict_from_two_unaligned_lists_and_default(keys: List, values: List, default: Any) -> Dict:
# ...

from typing import List, Dict, Any

def build_dict_from_two_unaligned_lists_and_default(keys: List, values: List, default: Any) -> Dict:
    # Инициализируем словарь
    result_dict = {}

    # Перебор элементов ключевого списка
    for index, key in enumerate(keys):
        # Проверка наличия соответствующего значения для текущего ключа
        if index < len(values):
            value = values[index]
        else:
            value = default

        # Добавление пары ключ-значение в словарь
        result_dict[key] = value

    # Возвращаем построенный словарь
    return result_dict

# Определяем списки ключей и значений
keys = ['key1', 'key2', 'key3', 'key4']
values = ['value1', 'value2', 'value3']

# Задаем значение по умолчанию
default_value = None

# Вызываем функцию для построения словаря
result = build_dict_from_two_unaligned_lists_and_default(keys, values, default_value)

# Выводим результат
print(result) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': None}


# Задание 2-40
# Построить и возвратить словарь из двух iterable объектов. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
# def build_dict_from_two_unaligned_iterables(keys: Iterable, values: Iterable) -> Dict:
# ...

from typing import Iterable, Dict

def build_dict_from_two_unaligned_iterables(keys: Iterable, values: Iterable) -> Dict:
    # Инициализация словаря
    result_dict = {}

    # Итерирование по ключам
    for key in keys:
        # Проверка наличия соответствующего значения
        if values:
            value = next(values, None)
        else:
            value = None

        # Добавление пары ключ-значение в словарь
        result_dict[key] = value

    # Возвращение словаря
    return result_dict

# Определение ключевого и значения iterable объектов
keys = ['key1', 'key2', 'key3', 'key4']
values = iter(['value1', 'value2', 'value3'])

# Вызов функции для построения словаря
result = build_dict_from_two_unaligned_iterables(keys, values)

# Вывод результата
print(result) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': None}


