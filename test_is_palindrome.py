import pytest
from is_palindrome import is_palindrome


def test_simple_word():
    assert is_palindrome("abba") is True

def test_not_palindrome():
    assert is_palindrome("python") is False

def test_number_palindrome():
    assert is_palindrome(12321) is True

def test_number_not_palindrome():
    assert is_palindrome(12345) is False

def test_phrase_with_spaces():
    assert is_palindrome("aaa bbb aaa") is True

def test_uppercase():
    assert is_palindrome("AbcacbA") is True

def test_empty_string():
    assert is_palindrome("") is True  
def test_single_char():
    assert is_palindrome("a") is True
