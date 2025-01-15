import pytest
from arrays_and_hashing.contains_duplicates import has_duplicates_sort, has_duplicates_compare, has_duplicates_hashset, has_duplicates_short

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 3], True),
    ([1, 2, 3, 4], False),
    ([], False),
    ([1], False),
    ([1, 1], True),
    ([1, 2, 3, 4, 5, 1], True),
])

def test_has_duplicates(nums, expected):
    assert has_duplicates_sort(nums) == expected
    assert has_duplicates_compare(nums) == expected
    assert has_duplicates_hashset(nums) == expected
    assert has_duplicates_short(nums) == expected
