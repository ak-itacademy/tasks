'''
Задание 2.
Коллекции.
Примечание: входные параметры ни в однй из задач не должны быть модифицированы.
'''

from typing import Any, Dict, Iterable, List, Tuple


# Сконструировать и вернуть список из переданных аргументов.
def build_list_from_args(*args) -> List:
    return list(args)


# Сконструировать и вернуть список из переданных аргументов, имеющих тип int.
def build_int_list_from_args(*args) -> List[int]:
    result = []
    for arg in args:
        if isinstance(arg, int):
            result.append(arg)
    return result


# Сконструировать и вернуть список из переданных аргументов, имеющих заданный тип.
def build_list_from_args_using_type(argument_type: type, *args) -> List:
    result = []
    for arg in args:
        if isinstance(arg, argument_type):
            result.append(arg)
    return result


# Сконструировать и вернуть список из переданных аргументов, тип которых входит заданное множество.
# Для более эффективной работы преобразовать `argument_types` в `set`.
def build_list_from_args_using_type_set(argument_types: Iterable, *args) -> List:
    result = []
    argument_types = set(argument_types)
    for arg in args:
        if type(arg) in argument_types:
            result.append(arg)
    return result


# Сконструировать и вернуть список из двух списков, переданных в качестве аргументов.
def build_list_from_two_lists(first: List, second: List) -> List:
    result = []
    result.append(first)
    result.append(second)
    return result


# Сконструировать и вернуть список из неограниченного числа списков, переданных в качестве аргументов.
def build_list_from_list_args(*lists) -> List:
    result = []
    for lst in lists:
        result.append(lst)
        return result


# Сконструировать список из заданного элемента и значения длины (использовать умножение).
def build_list_from_value_and_length(value: Any, length: int) -> List:
    result = [value] * length
    return result


# Удалить из списка заданный элемент.
def remove_value_from_list(values: List, value_to_remove: Any) -> List:
    result = [value for value in values if value != value_to_remove]
    return result


# Удалить из списка заданный элемент, используя comprehension expression [... for .. in ...].
def remove_value_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
    result = [value for value in values if value != value_to_remove]
    return result


# Удалить из списка заданный элемент, используя `filter` и lambda-функцию.
def remove_value_from_list_using_filter(values: List, value_to_remove: Any) -> List:
    result = [value for value in values if value != value_to_remove]
    return result


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
def remove_values_from_list(values: List, values_to_remove: Iterable) -> List:
    values_to_remove = set(values_to_remove)
    result = [value for value in values if value not in values_to_remove]
    return result


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
def remove_values_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
    values_to_remove = set(value_to_remove)
    result = [value for value in values if value not in values_to_remove]
    return result


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
# Использовать `filter` и lambda-функцию.
def remove_values_from_list_using_filter(values: List, value_to_remove: Any) -> List:
    values_to_remove = set(value_to_remove)
    result = list(filter(lambda value: value not in values_to_remove, values))
    return result


# Удалить из списка дублирующиеся значения (использовать преобразование в `set` и обратно).
def remove_duplicates_from_list(values: List) -> List:
    return list(set(values))


# Создать и вернуть словарь из заданного набора именованных аргументов, значения которых имеют тип int.
def build_dict_from_named_arguments_of_type_int(**kwargs) -> Dict:
    result = {}
    for key, value in kwargs.items():
        if isinstance(value, int):
            result[key] = value
            return result


# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - None (dict.fromkeys).
def build_dict_from_keys(values: Iterable) -> Dict:
    return dict.fromkeys(values, None)


# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - значение по-умолчанию.
def build_dict_from_keys_and_default(values: Iterable, default: Any) -> Dict:
    return {key: default for key in values}


# Создать и вернуть словарь, ключами которого являются индексы элементов,
# а значениями - значения элементов iterable параметров (использовать enumerate и dict comprehension).
def build_dict_from_indexed_values(values: Iterable) -> Dict:
    return {index: values for index in enumerate(values)}


# Создать и вернуть словарь, собранный на основе списка пар ключ-значение.
def build_dict_from_key_value_pairs(kws: List[Tuple]) -> Dict:
    return {key: value for key, value in kws}

# Создать и вернуть словарь, собранный из двух списков, один из которых
# содержит ключ, а второй - соответствующее значение (использовать zip).


def build_dict_from_two_lists(keys: List, values: List) -> Dict:
    return dict(zip(keys, values))


# Сформировать из двух словарей и вернуть его. В случае, если ключи совпадают,
# использовать значение из второго словаря (dict.update).
def build_dict_using_update(first: Dict, second: Dict) -> Dict:
    result = first.copy()
    result.update(second)
    return result


# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Заменить значение в случае совпадения ключей.
def update_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    for key, value in kwargs.items():
        if key in dictionary:
            dictionary[key] = value
        else:
            dictionary.update({key: value})
            return dictionary


# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Объединить значения в список в случае совпадения ключей.
def update_and_merge_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    for key, value in kwargs.items():
        if key in dictionary:
            if isinstance(dictionary[key], list):
                dictionary[key].append(value)
            else:
                dictionary[key] = [dictionary[key], value]
        else:
            dictionary.update({key: value})
            return dictionary


# Объединить два словарь и вернуть результат.
# Объединить значения в список в случае совпадения ключей.
def merge_two_dicts(first: Dict, second: Dict) -> Dict:
    result = first.copy()
    for key, value in second.items():
        if key in result:
            if isinstance(result[key], list):
                result[key].append(value)
            else:
                result[key] = [result[key], value]
        else:
            result.update({key: value})
            return result


# Объединить два словарь и вернуть результат.
# В случае совпадения ключей:
# - объединить значения рекурсивно, если оба значения - словари;
# - объединить значения в один список, если оба значения - списки;
# - объединить значения в одно множество, если оба значения - множества;
# - объединить значения в список в любом другом случае.
def deep_merge_two_dicts(first: Dict, second: Dict) -> Dict:
    result = first.copy()
    for key, value in second.items():
        if key in result:
            if isinstance(result[key], dict) and isinstance(value, dict):
                result = deep_merge_two_dicts(result[key], value)
            elif isinstance(result[key], list) and isinstance(value, list):
                result[key] = result[key] + value
            elif isinstance(result[key], set) and isinstance(value, set):
                result[key] = result[key].union(value)
            else:
                result[key] = [result[key], value] if not isinstance(result[key], list) else result[key] + [value]
        else:
            result.update({key: value})
            return result


# Вернуть список, состоящий из ключей, принадлежащих словарю.
def get_keys(dictionary: Dict) -> List:
    return list(dictionary.keys())


# Вернуть список, состоящий из значений, принадлежащих словарю.
def get_values(dictionary: Dict) -> List:
    return list(dictionary.values())


# Вернуть список, состоящий из пар ключ-значение, принадлежащих словарю.
def get_key_value_pairs(dictionary: Dict) -> List[Tuple]:
    return list(dictionary.items())


# Реверсировать и вернуть словарь.
def reverse_dict(dictionary: Dict) -> Dict:
    return {value: key for key, value in dictionary.items()}


# Удалить из словаря элементы, имеющие пустые значения (None, '', [], {}).
def clear_dummy_elements(dictionary: Dict) -> Dict:
    return {key: value for key, value in dictionary.items() if value not in [None, '', [], {}]}


# Удалить из словаря дублирующиеся и пустые элементы.
def clear_dummy_and_duplicate_elements(dictionary: Dict) -> Dict:
    new_dict = {}
    for key, value in dictionary.items():
        if value in [None, '', [], {}]:
            continue
        if value in new_dict.values():
            continue
        new_dict[key] = value
        return new_dict


# Обменять в словаре клчи и значения (в качестве значений могут выступать только неизменяемые значения).
def swap_dict_keys_and_values(dictionary: Dict) -> Dict:
    for value in dictionary.values():
        if isinstance(value, (list, dict, set)):
            raise ValueError
    return {value: key for key, value in dictionary.items()}


# Вернуть словарь, отсортированный по ключу. Ключи могут иметь только тип int.
def sort_dict_with_int_keys(dictionary: Dict) -> Dict:
    for key in dictionary.keys():
        if not isinstance(key, int):
            raise ValueError
    return {key: dictionary[key] for key in sorted(dictionary.keys())}


# Вернуть словарь, отсортированный по ключу в обратном порядке. Ключи могут иметь только тип int.
def sort_dict_backward_with_int_keys(dictionary: Dict) -> Dict:
    for key in dictionary.keys():
        if not isinstance(key, int):
            raise ValueError
    return{key: dictionary[key] for key in sorted(dictionary.keys(), reverse=True)}


# Вернуть словарь, элементы которого сгруппированы по типу ключа.
# В качестве ключей могут выступать: целые числа, дробные числа и строки.
# Приоритет сортировки групп (от высшего к низшему): целые числа, дробные числа, строки.
def group_dict_elements_by_key_type(dictionary: Dict) -> Dict:
    int_keys = {}
    float_keys = {}
    str_keys = {}
    for key, value in dictionary.items():
        if isinstance(key, int):
            int_keys[key] = value
        elif isinstance(key, float):
            float_keys[key] = value
        elif isinstance(key, str):
            str_keys[key] = value
        else:
            raise ValueError
    return{
        **int_keys,
        **float_keys,
        **str_keys,
    }


# Вернуть словарь, элементы которого сгруппированы по типу ключа.
# В качестве ключей могут выступать: целые числа, дробные числа и строки.
# Приоритет сортировки групп (от высшего к низшему): целые числа, дробные числа, строки.
# Внутри каждой из групп отсортировать элементы по значениям ключа в обратном порядке.
def group_dict_elements_by_key_type_and_sort(dictionary: Dict) -> Dict:
    int_dict = {}
    float_dict = {}
    str_dict = {}
    for key, value in dictionary.items():
        if isinstance(key, int):
            int_dict[key] = value
        elif isinstance(key, float):
            float_dict[key] = value
        elif isinstance(key, str):
            str_dict[key] = value
    result_dict = {}
    if int_dict:
        result_dict['Integers'] = int_dict
    if float_dict:
        result_dict['Floats'] = float_dict
    if str_dict:
        str_dict['Strings'] = str_dict
    return result_dict


# Подсчитать количество элементов словаря, имеющих числовой тип, значение которых находится
# в интервале [-10, 25].
def count_dict_elements(dictionary: Dict) -> Dict:
    count = 0
    for key, value in dictionary.items():
        if isinstance(value, (int, float)) and -10 <= value <= 25:
            count += 1
        return count

# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
def build_dict_from_two_unaligned_lists(keys: List, values: List) -> Dict:
    b = {}
    for i, key in enumerate(keys):
        if i < len(values):
            b[key] = values[i]
        else:
            b[key] = None
        return b


# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение, заданное по-умолчанию.
def build_dict_from_two_unaligned_lists_and_default(keys: List, values: List, default: Any) -> Dict:
    a = {}
    for i, key in enumerate(keys):
        if i < len(values):
            a[key] = values[i]
        else:
            a[key] = default
    return a


# Построить и возвратить словарь из двух iterable объектов. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
def build_dict_from_two_unaligned_iterables(keys: Iterable, values: Iterable) -> Dict:
    a = {}
    for i, key in enumerate(keys):
        try:
            value = next(values)
        except StopIteration:
            value = None
        a[key] = value
    return a