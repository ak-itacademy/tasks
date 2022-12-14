from tasks.task_2_collections import (
    build_list_from_args,
    build_int_list_from_args,
    build_list_from_args_using_type,
    build_list_from_args_using_type_set,
    build_list_from_two_lists,
    build_list_from_list_args,
    build_list_from_value_and_length,
    remove_value_from_list,
    remove_value_from_list_using_comprehension,
    remove_value_from_list_using_filter,
    remove_values_from_list,
    remove_values_from_list_using_comprehension,
    remove_values_from_list_using_filter,
    remove_duplicates_from_list,
    build_dict_from_named_arguments_of_type_int,
    build_dict_from_keys,
    build_dict_from_keys_and_default,
    build_dict_from_indexed_values,
    build_dict_from_key_value_pairs,
    build_dict_from_two_lists,
    build_dict_using_update,
    update_dict_using_kwargs,
    update_and_merge_dict_using_kwargs,
    merge_two_dicts,
    deep_merge_two_dicts,
    get_keys,
    get_values,
    get_key_value_pairs,
    reverse_dict,
    clear_dummy_elements,
    clear_dummy_and_duplicate_elements,
    swap_dict_keys_and_values,
    sort_dict_with_int_keys,
    sort_dict_backward_with_int_keys,
    group_dict_elements_by_key_type,
    group_dict_elements_by_key_type_and_sort,
    count_dict_elements,
    build_dict_from_two_unaligned_lists,
    build_dict_from_two_unaligned_lists_and_default,
    build_dict_from_two_unaligned_iterables
)


def test_build_list_from_args():
    assert [] == build_list_from_args()
    assert [1] == build_list_from_args(1)
    assert [1, None] == build_list_from_args(1, None)


def test_build_int_list_from_args():
    assert [] == build_int_list_from_args()
    assert [] == build_int_list_from_args('string', None, 1.2)
    assert [1] == build_int_list_from_args(None, 1)
    assert [1, 2, 3, 4] == build_int_list_from_args(1, 2, 3, 4)


def test_build_list_from_args_using_type():
    assert [] == build_list_from_args_using_type(int)
    assert [] == build_list_from_args_using_type(str, 1, 2)
    assert ['text'] == build_list_from_args_using_type(str, 1, 'text', {}, [1, 'text'])
    assert ['test1', 'text2'] == build_list_from_args_using_type(str, 'text1', 'text2')


def test_build_list_from_args_using_type_set():
    assert [] == build_list_from_args_using_type_set([])
    assert [] == build_list_from_args_using_type_set([], 1, 'text', {})
    assert [1, 2, {}, {}] == build_list_from_args_using_type_set([int, dict], 1, 'text', 2, [], {}, {})


def test_build_list_from_two_lists():
    assert [] == build_list_from_two_lists([], [])
    assert [1] == build_list_from_two_lists([1], [])
    assert [2] == build_list_from_two_lists([], [2])
    assert [1, 2, 3, 4] == build_list_from_two_lists([1, 2], [3, 4])


def test_build_list_from_list_args():
    assert [] == build_list_from_list_args([], [], [])
    assert [1, 2, 'text', {}, [], [], {}, 2, 3, None] == build_list_from_list_args([], [1], [2, 'text'], [], [{}, []],
                                                                                   [[], {}, 2], [], [3, None])


def test_build_list_from_value_and_length():
    ...


def test_remove_value_from_list():
    ...


def test_remove_value_from_list_using_comprehension():
    ...


def test_remove_value_from_list_using_filter():
    ...


def test_remove_values_from_list():
    ...


def test_remove_values_from_list_using_comprehension():
    ...


def test_remove_values_from_list_using_filter():
    ...


def test_remove_duplicates_from_list():
    ...


def test_build_dict_from_named_arguments_of_type_int():
    ...


def test_build_dict_from_keys():
    ...


def test_build_dict_from_keys_and_default():
    ...


def test_build_dict_from_indexed_values():
    ...


def test_build_dict_from_key_value_pairs():
    ...


def test_build_dict_from_two_lists():
    ...


def test_build_dict_using_update():
    ...


def test_update_dict_using_kwargs():
    ...


def test_update_and_merge_dict_using_kwargs():
    ...


def test_merge_two_dicts():
    ...


def test_deep_merge_two_dicts():
    ...


def test_get_keys():
    ...


def test_get_values():
    ...


def test_get_key_value_pairs():
    ...


def test_reverse_dict():
    ...


def test_clear_dummy_elements():
    ...


def test_clear_dummy_and_duplicate_elements():
    ...


def test_swap_dict_keys_and_values():
    ...


def test_sort_dict_with_int_keys():
    ...


def test_sort_dict_backward_with_int_keys():
    ...


def test_group_dict_elements_by_key_type():
    ...


def test_group_dict_elements_by_key_type_and_sort():
    ...


def test_count_dict_elements():
    ...


def test_build_dict_from_two_unaligned_lists():
    ...


def test_build_dict_from_two_unaligned_lists_and_default():
    ...


def test_build_dict_from_two_unaligned_iterables():
    ...
