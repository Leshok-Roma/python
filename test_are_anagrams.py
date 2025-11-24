import pytest
from are_anagrams import are_anagrams

def test_simple_anagrams():
    assert are_anagrams("listen", "silent") is True

def test_not_anagrams():
    assert are_anagrams("hello", "world") is False

def test_with_spaces():
    assert are_anagrams("a gentleman", "elegant man") is True

def test_upper_lower_cases():
    assert are_anagrams("Debit Card", "Bad Credit") is True

def test_empty_strings():
    assert are_anagrams("", "") is True

def test_single_char():
    assert are_anagrams("a", "a") is True
