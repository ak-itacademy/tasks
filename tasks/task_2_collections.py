'''
Задание 2.
Коллекции.
Примечание: входные параметры ни в однй из задач не должны быть модифицированы.
'''

from typing import Any, Dict, Iterable, List, Tuple


# Сконструировать и вернуть список из переданных аргументов.
def build_list_from_args(*args) -> List:
    return [x for x in args]


# a = build_list_from_args(2, 3, 4, 5, 3, "ddw", "fe")
# print(a, type(a))


# Сконструировать и вернуть список из переданных аргументов, имеющих тип int.
def build_int_list_from_args(*args) -> List[int]:
    return [x for x in args if isinstance(x, int)]


# a = build_int_list_from_args(2, 3, "wew", 4, 5, 3, "ddw", "fe")
# print(a, type(a))


# Сконструировать и вернуть список из переданных аргументов, имеющих заданный тип.
def build_list_from_args_using_type(argument_type: type, *args) -> List:
    return [x for x in args if isinstance(x, argument_type)]


# a = build_list_from_args_using_type(float, 2, 3, "wew", 4, 5.7, 3, "ddw", "fe")
# print(a, type(a))


# Сконструировать и вернуть список из переданных аргументов, тип которых входит в заданное множество.
# Для более эффективной работы преобразовать `argument_types` в `set`.
def build_list_from_args_using_type_set(argument_types: Iterable, *args) -> List:
    argument_types = set(argument_types)
    return [x for x in args for type_ in argument_types if type(x) == type_]


# a = build_list_from_args_using_type_set([float, str], 2, 3, "wew", 4, 5.7, 3, "ddw", "fe", 3.8, [3, 5])
# print(a, type(a))


# Сконструировать и вернуть список из двух списков, переданных в качестве аргументов.
def build_list_from_two_lists(first: List, second: List) -> List:
    return first + second


# a = build_list_from_two_lists([float, str, int], [1, 2, 3, 4, 5])
# print(a, type(a))


# Сконструировать и вернуть список из неограниченного числа списков, переданных в качестве аргументов.
def build_list_from_list_args(*lists) -> List:
    my_list = []
    [my_list.extend(list_) for list_ in lists]
    return my_list


# a = build_list_from_list_args([float, str, int], [1, 2, 3, 4, 5], [4, "erqw"], [])
# print(a, type(a))


# Сконструировать список из заданного элемента и значения длины (использовать умножение).
def build_list_from_value_and_length(value: Any, length: int) -> List:
    return [value] * length


# a = build_list_from_value_and_length("text", 3)
# print(a, type(a))


# Удалить из списка заданный элемент.
def remove_value_from_list(values: List, value_to_remove: Any) -> List:
    values.remove(value_to_remove)
    return values


# a = remove_value_from_list([3, 5, 7, 8, "ref", "del", [], {}], "del")
# print(a, type(a))


# Удалить из списка заданный элемент, используя comprehension expression [... for .. in ...].
def remove_value_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
    return [value for value in values if value != value_to_remove]


# a = remove_value_from_list_using_comprehension([3, 5, 7, 8, "ref", "del", [], {}], "del")
# print(a, type(a))


# Удалить из списка заданный элемент, используя `filter` и lambda-функцию.
def remove_value_from_list_using_filter(values: List, value_to_remove: Any) -> List:
    return list(filter(lambda x: x != value_to_remove, values))


# a = remove_value_from_list_using_filter([3, 5, 7, 8, "ref", "del", [], {}], "del")
# print(a, type(a))


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
def remove_values_from_list(values: List, values_to_remove: Iterable) -> List:
    values_to_remove = set(values_to_remove)
    list(map(lambda x: values.remove(x), values_to_remove))
    return values


# a = remove_values_from_list([3, 5, 7, 8, "ref", "del", [], {}], ["del", 5, 3])
# print(a, type(a))


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
def remove_values_from_list_using_comprehension(values: List, values_to_remove: Any) -> List:
    values_to_remove = set(values_to_remove)
    return [value for value in values if value not in values_to_remove]


# a = remove_values_from_list_using_comprehension([3, 5, 7, 8, "ref", "del"], ["del", 5, 3])
# print(a, type(a))


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
# Использовать `filter` и lambda-функцию.
def remove_values_from_list_using_filter(values: List, values_to_remove: Any) -> List:
    values_to_remove = set(values_to_remove)
    return list(filter(lambda value: value not in values_to_remove, values))


# a = remove_values_from_list_using_filter([3, 5, 7, 8, "ref", "del"], ["del", 5, 3])
# print(a, type(a))


# Удалить из списка дублирующиеся значения (использовать преобразование в `set` и обратно).
def remove_duplicates_from_list(values: List) -> List:
    values = set(values)
    return list(values)


# a = remove_duplicates_from_list([3, "ref", 5, 7, 3, 7, 8, "ref", "del"])
# print(a, type(a))


# Создать и вернуть словарь из заданного набора именованных аргументов, значения которых имеют тип int.
def build_dict_from_named_arguments_of_type_int(**kwargs) -> Dict:
    return {str(key): value for key, value in kwargs.items() if isinstance(value, int)}

# a = build_dict_from_named_arguments_of_type_int(a=3, b="ref", c=5, d=7.6, e=3, f=7, g=8.3, h="ref", i="del")
# print(a, type(a))


# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - None (dict.fromkeys).
def build_dict_from_keys(values: Iterable) -> Dict:
    return dict.fromkeys(values)


# a = build_dict_from_keys([8, 7, 9, 4])
# print(a, type(a))


# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - None (dict.fromkeys).
def build_dict_from_keys(values: Iterable) -> Dict:
    return dict.fromkeys(values)


# a = build_dict_from_keys([8, 7, 9, 4])
# print(a, type(a))


# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - значение по-умолчанию.
def build_dict_from_keys_and_default(values: Iterable, default: Any) -> Dict:
    return dict.fromkeys(values, default)


# a = build_dict_from_keys_and_default([8, 7, 9, 4], "nothing")
# print(a, type(a))


# Создать и вернуть словарь, ключами которого являются индексы элементов,
# а значениями - значения элементов iterable параметров (использовать enumerate и dict comprehension).
def build_dict_from_indexed_values(values: Iterable) -> Dict:
    return {key: value for key, value in enumerate(values)}


# a = build_dict_from_indexed_values([8, 7, 9, 4, "add"])
# print(a, type(a))


# Создать и вернуть словарь, собранный на основе списка пар ключ-значение.
def build_dict_from_key_value_pairs(kws: List[Tuple]) -> Dict:
    return dict(kws)


# a = build_dict_from_key_value_pairs([(8, 3), ("s", 7), (5, "sf"), (2, 9)])
# print(a, type(a))

# Создать и вернуть словарь, собранный из двух списков, один из которых
# содержит ключ, а второй - соответствующее значение (использовать zip).
def build_dict_from_two_lists(keys: List, values: List) -> Dict:
    return dict(zip(keys, values))


# a = build_dict_from_two_lists([8, 3, 7, 4], [9, 55, 33, 76])
# print(a, type(a))


# Сформировать из двух словарей и вернуть его. В случае, если ключи совпадают,
# использовать значение из второго словаря (dict.update).
def build_dict_using_update(first: Dict, second: Dict) -> Dict:
    first.update(second)
    return first


# a = build_dict_using_update({8: 3, 7: 4}, {8: 7, 1: 0})
# print(a, type(a))


# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Заменить значение в случае совпадения ключей.
def update_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    dictionary.update(dict(kwargs))
    return dictionary


# a = update_dict_using_kwargs({"a": 3, "b": 4, "c": 7, 1: 0}, a=9, d="df", c=6)
# print(a, type(a))


# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Объединить значения в список в случае совпадения ключей.
def update_and_merge_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    return ...


# Объединить два словарь и вернуть результат.
# Объединить значения в список в случае совпадения ключей.
def merge_two_dicts(first: Dict, second: Dict) -> Dict:
    return ...


# Объединить два словарь и вернуть результат.
# В случае совпадения ключей:
# - объединить значения рекурсивно, если оба значения - словари;
# - объединить значения в один список, если оба значения - списки;
# - объединить значения в одно множество, если оба значения - множества;
# - объединить значения в список в любом другом случае.
def deep_merge_two_dicts(first: Dict, second: Dict) -> Dict:
    return ...


# Вернуть список, состоящий из ключей, принадлежащих словарю.
def get_keys(dictionary: Dict) -> List:
    ...


# Вернуть список, состоящий из значений, принадлежащих словарю.
def get_values(dictionary: Dict) -> List:
    ...


# Вернуть список, состоящий из пар ключ-значение, принадлежащих словарю.
def get_key_value_pairs(dictionary: Dict) -> List[Tuple]:
    ...


# Реверсировать и вернуть словарь.
def reverse_dict(dictionary: Dict) -> Dict:
    ...


# Удалить из словаря элементы, имеющие пустые значения (None, '', [], {}).
def clear_dummy_elements(dictionary: Dict) -> Dict:
    ...


# Удалить из словаря дублирующиеся и пустые элементы.
def clear_dummy_and_duplicate_elements(dictionary: Dict) -> Dict:
    ...


# Обменять в словаре клчи и значения (в качестве значений могут выступать только неизменяемые значения).
def swap_dict_keys_and_values(dictionary: Dict) -> Dict:
    ...


# Вернуть словарь, отсортированный по ключу. Ключи могут иметь только тип int.
def sort_dict_with_int_keys(dictionary: Dict) -> Dict:
    ...


# Вернуть словарь, отсортированный по ключу в обратном порядке. Ключи могут иметь только тип int.
def sort_dict_backward_with_int_keys(dictionary: Dict) -> Dict:
    ...


# Вернуть словарь, элементы которого сгруппированы по типу ключа.
# В качестве ключей могут выступать: целые числа, дробные числа и строки.
# Приоритет сортировки групп (от высшего к низшему): целые числа, дробные числа, строки.
def group_dict_elements_by_key_type(dictionary: Dict) -> Dict:
    ...


# Вернуть словарь, элементы которого сгруппированы по типу ключа.
# В качестве ключей могут выступать: целые числа, дробные числа и строки.
# Приоритет сортировки групп (от высшего к низшему): целые числа, дробные числа, строки.
# Внутри каждой из групп отсортировать элементы по значениям ключа в обратном порядке.
def group_dict_elements_by_key_type_and_sort(dictionary: Dict) -> Dict:
    ...


# Подсчитать количество элементов словаря, имеющих числовой тип, значение которых находится
# в интервале [-10, 25].
def count_dict_elements(dictionary: Dict) -> Dict:
    ...


# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
def build_dict_from_two_unaligned_lists(keys: List, values: List) -> Dict:
    ...


# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение, заданное по-умолчанию.
def build_dict_from_two_unaligned_lists_and_default(keys: List, values: List, default: Any) -> Dict:
    ...


# Построить и возвратить словарь из двух iterable объектов. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
def build_dict_from_two_unaligned_iterables(keys: Iterable, values: Iterable) -> Dict:
    ...
