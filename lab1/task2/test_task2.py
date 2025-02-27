import pytest
from task2 import bubble_sort


def test_empty_list():
    assert bubble_sort([]) == []

def test_single_element():
    assert bubble_sort([1]) == [1]

def test_already_sorted():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_duplicates():
    assert bubble_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]

def test_negative_numbers():
    assert bubble_sort([-1, 3, 0, -2, 5, 4]) == [-2, -1, 0, 3, 4, 5]
    