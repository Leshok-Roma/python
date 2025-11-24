import pytest 
from count_words  import count_words


def test_empty_string():
    assert count_words("") == 0

def test_single_word():
    assert count_words("Hello") == 1
def test_multiple_words():
    assert count_words("Hello world this is a test") == 6
def test_leading_trailing_spaces():
    assert count_words("   Hello world   ") == 2    
def test_only_spaces():
    assert count_words("     ") == 0    
