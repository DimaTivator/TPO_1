import pytest
from task2 import bubble_sort


@pytest.mark.parametrize(
    "test_input, expected, test_case_name", [
        ([], [], "empty list"),
        ([1], [1], "single element"),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], "already sorted"),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], "reverse sorted"),
        ([4, 2, 2, 8, 3, 3, 1], [1, 2, 2, 3, 3, 4, 8], "duplicates"),
        ([-1, 3, 0, -2, 5, 4], [-2, -1, 0, 3, 4, 5], "negative numbers"),
    ]
)
def test_bubble_sort(test_input, expected, test_case_name):
    assert bubble_sort(test_input) == expected
    
    
@pytest.mark.parametrize(
    "test_input", [
        "not a list",
        52,
        None,
        {5, 2}
    ]
)
def test_bubble_sort_invalid_input(test_input):
    with pytest.raises(TypeError):
        bubble_sort(test_input)
    