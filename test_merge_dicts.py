import pytest
from merge_dicts import merge_dicts


def test_simple_merge():
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    result = merge_dicts(d1, d2)
    assert result == {"a": 1, "b": 2, "c": 3, "d": 4}

def test_overlap_replace():
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 10}
    result = merge_dicts(d1, d2)
    assert result == {"a": 1, "b": 10}


def test_nested_merge():
    d1 = {"a": {"x": 1, "y": 2}}
    d2 = {"a": {"z": 3}}
    result = merge_dicts(d1, d2)
    assert result == {"a": {"x": 1, "y": 2, "z": 3}}


def test_list_merge():
    d1 = {"a": [1, 2]}
    d2 = {"a": [3, 4]}
    result = merge_dicts(d1, d2)
    assert result == {"a": [1, 2, 3, 4]}


def test_set_merge():
    d1 = {"a": {1, 2}}
    d2 = {"a": {2, 3}}
    result = merge_dicts(d1, d2)
    assert result == {"a": {1, 2, 3}}


def test_tuple_merge():
    d1 = {"a": (1, 2)}
    d2 = {"a": (3, 4)}
    result = merge_dicts(d1, d2)
    assert result == {"a": (1, 2, 3, 4)}


def test_type_mismatch_replace():
    d1 = {"a": [1, 2]}
    d2 = {"a": "new"}
    result = merge_dicts(d1, d2)
    assert result == {"a": "new"}


