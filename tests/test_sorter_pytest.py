import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.sorter import sort_descending, is_sorted_descending

@pytest.mark.parametrize("input_list,expected", [
    ([3, 1, 4, 1, 5, 9, 2], [9, 5, 4, 3, 2, 1, 1]),
    ([5, 5, 5, 5], [5, 5, 5, 5]),
    ([1, 2, 3], [3, 2, 1]),
    ([], []),
    ([42], [42]),
])
def test_sort_descending_parametrized(input_list, expected):
    """Параметризованный тест сортировки"""
    result = sort_descending(input_list)
    assert result == expected
    assert is_sorted_descending(result)

@pytest.mark.parametrize("input_list,expected", [
    ([5, 4, 3, 2, 1], True),
    ([10, 7, 7, 5, 1], True),
    ([1], True),
    ([], True),
    ([1, 2, 3, 4, 5], False),
    ([5, 4, 6, 2, 1], False),
])
def test_is_sorted_descending(input_list, expected):
    assert is_sorted_descending(input_list) == expected

def test_original_list_unchanged():
    """Тест: исходный список не изменяется"""
    original = [5, 2, 8, 1, 9, 3]
    sort_descending(original)
    assert original == [5, 2, 8, 1, 9, 3]

def test_invalid_input():
    """Тест: недопустимые входные данные"""
    with pytest.raises(TypeError, match="Ошибка: входное значение должно быть списком"):
        sort_descending("not a list")
