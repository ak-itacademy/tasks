'''
Задание 2.
Коллекции.
Примечание: входные параметры ни в одной из задач не должны быть модифицированы.
'''
import copy
from typing import Any, Dict, Iterable, List, Tuple


# Сконструировать и вернуть список из переданных аргументов.
def build_list_from_args(*args) -> List:
    return list(args)


# Сконструировать и вернуть список из переданных аргументов, имеющих тип int.
def build_int_list_from_args(*args) -> List[int]:
    return [arg for arg in args if type(arg) is int]


# Сконструировать и вернуть список из переданных аргументов, имеющих заданный тип.
def build_list_from_args_using_type(argument_type: type, *args) -> list:
    return [arg for arg in args if type(arg) is argument_type]


# Сконструировать и вернуть список из переданных аргументов, тип которых входит заданное множество.
# Для более эффективной работы преобразовать `argument_types` в `set`.
def build_list_from_args_using_type_set(argument_types: Iterable, *args) -> List:
    argument_types = set(argument_types)
    return [arg for arg in args if type(arg) in argument_types]


# Сконструировать и вернуть список из двух списков, переданных в качестве аргументов.
def build_list_from_two_lists(first: List, second: List) -> List:
    return [*first, *second]


# Сконструировать и вернуть список из неограниченного числа списков, переданных в качестве аргументов.
def build_list_from_list_args(*lists) -> List:
    return [item for lst in lists for item in lst]


# Сконструировать список из заданного элемента и значения длины (использовать умножение).
def build_list_from_value_and_length(value: Any, length: int) -> List:
    return [value] * length


# Удалить из списка заданный элемент.
def remove_value_from_list(values: List, value_to_remove: Any) -> List:
    return [item for item in values if item != value_to_remove]


# Удалить из списка заданный элемент, используя comprehension expression [... for .. in ...].
def remove_value_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
    return [i for i in values if i != value_to_remove]


# Удалить из списка заданный элемент, используя `filter` и lambda-функцию.
def remove_value_from_list_using_filter(values: List, value_to_remove: Any) -> List:
    return list(filter(lambda x: x != value_to_remove, values))


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
def remove_values_from_list(values: List, values_to_remove: Iterable) -> List:
    new_values = []
    for i in values:
        if i not in set(values_to_remove):
            new_values.append(i)
    return new_values


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
def remove_values_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
    return [i for i in values if i not in set(value_to_remove)]


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
# Использовать `filter` и lambda-функцию.
def remove_values_from_list_using_filter(values: List, value_to_remove: Any) -> List:
    return list(filter(lambda x: x not in set(value_to_remove), values))


# Удалить из списка дублирующиеся значения (использовать преобразование в `set` и обратно).
def remove_duplicates_from_list(values: List) -> List:
    return list(set(values))


# Создать и вернуть словарь из заданного набора именованных аргументов, значения которых имеют тип int.
def build_dict_from_named_arguments_of_type_int(**kwargs) -> Dict:
    return {k: v for k, v in kwargs.items() if type(v) is int}


# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - None (dict.fromkeys).
def build_dict_from_keys(values: Iterable) -> Dict:
    return dict.fromkeys(values)


# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - None (dict.fromkeys).
def build_dict_from_keys(values: Iterable) -> Dict:
    return dict.fromkeys(values)


# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - значение по-умолчанию.
def build_dict_from_keys_and_default(values: Iterable, default: Any) -> Dict:
    return {key: default.copy() for key in values}


# Создать и вернуть словарь, ключами которого являются индексы элементов,
# а значениями - значения элементов iterable параметров (использовать enumerate и dict comprehension).
def build_dict_from_indexed_values(values: Iterable) -> Dict:
    return {index: value for index, value in enumerate(values)}


# Создать и вернуть словарь, собранный на основе списка пар ключ-значение.
def build_dict_from_key_value_pairs(kws: List[Tuple]) -> Dict:
    return {key: value for key, value in kws}

    # Создать и вернуть словарь, собранный из двух списков, один из которых
    # содержит ключ, а второй - соответствующее значение (использовать zip).


def build_dict_from_two_lists(keys: List, values: List) -> Dict:
    return {key: value for key, value in zip(keys, values)}


# Сформировать из двух словарей и вернуть его. В случае, если ключи совпадают,
# использовать значение из второго словаря (dict.update).
def build_dict_using_update(first: Dict, second: Dict) -> Dict:
    return {**first, **{key: second[key] for key in second if key not in first}}


# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Заменить значение в случае совпадения ключей.
def update_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    updated_dict = dictionary.copy()
    updated_dict.update({k: v for k, v in kwargs.items() if k not in updated_dict})
    return updated_dict


# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Объединить значения в список в случае совпадения ключей.
def update_and_merge_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    result_dict = dictionary.copy()
    for key, value in kwargs.items():
        if key in result_dict:
            if type(result_dict[key]) == list:
                result_dict[key].append(value)
            else:
                result_dict[key] = [result_dict[key], value]
        else:
            result_dict[key] = value
    return result_dict


# Объединить два словарь и вернуть результат.
# Объединить значения в список в случае совпадения ключей.
def merge_two_dicts(first: Dict, second: Dict) -> Dict:
    result = {**first}
    for key, second_value in second.items():
        first_value = first.get(key)
        if first_value is not None:
            result[key] = [first_value, second_value]
        else:
            result[key] = second_value
    return result


# Объединить два словарь и вернуть результат.
# В случае совпадения ключей:
# - объединить значения рекурсивно, если оба значения - словари;
# - объединить значения в один список, если оба значения - списки;
# - объединить значения в одно множество, если оба значения - множества;
# - объединить значения в список в любом другом случае.
def deep_merge_two_dicts(first: Dict, second: Dict) -> Dict:
    for key, value in second.items():
        if key in first:
            if isinstance(first[key], dict) and isinstance(value, dict):
                first[key] = deep_merge_two_dicts(first[key], value)
            elif isinstance(first[key], list) and isinstance(value, list):
                first[key].extend(value)
            elif isinstance(first[key], set) and isinstance(value, set):
                first[key].update(value)
            else:
                first[key] = [first[key], value]
        else:
            first[key] = value
    return first


# Вернуть список, состоящий из ключей, принадлежащих словарю.
def get_keys(dictionary: Dict) -> List:
    return list(dictionary)


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
    return {k: v for k, v in dictionary.items() if v not in [None, '', [], {}]}


# Удалить из словаря дублирующиеся и пустые элементы.
def clear_dummy_and_duplicate_elements(dictionary: Dict) -> Dict:
    result = {}

    for k, v in clear_dummy_elements(dictionary).items():
        result.setdefault(v, k)

    return {v: k for k, v in result.items()}


# Обменять в словаре ключи и значения (в качестве значений могут выступать только неизменяемые значения).
def swap_dict_keys_and_values(dictionary: Dict) -> Dict:
    return {v: k for k, v in dictionary.items() if isinstance(v, (int, float, str, bool))}


# Вернуть словарь, отсортированный по ключу. Ключи могут иметь только тип int.
def sort_dict_with_int_keys(dictionary: Dict[int, Any]) -> Dict:
    return dict(sorted(((k, v) for k, v in dictionary.items() if isinstance(k, int)), key=lambda x: x[0]))


# Вернуть словарь, отсортированный по ключу в обратном порядке. Ключи могут иметь только тип int.
def sort_dict_backward_with_int_keys(dictionary: Dict) -> Dict:
    return dict(sorted(((k, v) for k, v in dictionary.items() if isinstance(k, int)), key=lambda x: x[0], reverse=True))


# Вернуть словарь, элементы которого сгруппированы по типу ключа.
# В качестве ключей могут выступать: целые числа, дробные числа и строки.
# Приоритет сортировки групп (от высшего к низшему): целые числа, дробные числа, строки.
def group_dict_elements_by_key_type(dictionary: Dict) -> Dict:
    grouped_items = [(type(key), key, value) for key, value in dictionary.items()]
    sorted_items = sorted(grouped_items, key=lambda x: (x[0] == int, x[0] == float, x[0] == str))
    return {key: value for _, key, value in sorted_items}


# Вернуть словарь, элементы которого сгруппированы по типу ключа.
# В качестве ключей могут выступать: целые числа, дробные числа и строки.
# Приоритет сортировки групп (от высшего к низшему): целые числа, дробные числа, строки.
# Внутри каждой из групп отсортировать элементы по значениям ключа в обратном порядке.
def group_dict_elements_by_key_type_and_sort(dictionary: Dict) -> Dict:
    str_keys, float_keys, int_keys = [], [], []

    for key, value in dictionary.items():
        if isinstance(key, str):
            str_keys.append((key, value))
        elif isinstance(key, float):
            float_keys.append((key, value))
        elif isinstance(key, int):
            int_keys.append((key, value))

    str_keys.sort()
    float_keys.sort()
    int_keys.sort()

    return {**dict(int_keys), **dict(float_keys), **dict(str_keys)}


# Подсчитать количество элементов словаря, имеющих числовой тип, значение которых находится
# в интервале [-10, 25].
def count_dict_elements(dictionary: Dict) -> Dict:
    return {'count': sum(isinstance(value, (int, float)) and -10 <= value <= 25 for value in dictionary.values())}


# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
def build_dict_from_two_unaligned_lists(keys: List, values: List) -> Dict:
    return {keys[i]: copy.deepcopy(values[i]) if i < len(values) else None for i in range(len(keys))}


# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение, заданное по-умолчанию.
def build_dict_from_two_unaligned_lists_and_default(keys: List, values: List, default: Any) -> Dict:
    return {keys[i]: values[i] if i < len(values) else copy.deepcopy(default) for i in range(len(keys))}


# Построить и возвратить словарь из двух iterable объектов. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
def build_dict_from_two_unaligned_iterables(keys: Iterable, values: Iterable) -> Dict:
    return {keys[i]: values[i] if i < min(len(keys), len(values)) else None for i in range(max(len(keys), len(values)))}
