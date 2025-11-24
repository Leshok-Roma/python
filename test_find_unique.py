import pytest
from find_unique import find_unique

def test_simple_list():
    assert find_unique([1, 2, 2, 3, 4, 4]) == [1, 3]

def test_all_unique():
    assert find_unique([1, 2, 3]) == [1, 2, 3]

def test_no_unique():
    assert find_unique([1, 1, 2, 2, 3, 3]) == []

def test_strings():
    assert find_unique(["a", "b", "b", "c"]) == ["a", "c"]

def test_empty_list():
    assert find_unique([]) == []


