"""Test the trigrams file."""


import pytest


def test_book_argument_is_valid():
    """Make sure the string passed into main is valid."""
    from trigrams import main
    test_book = main('test_book.txt', 1)
    assert len(test_book) != 0 and type(test_book) == str
