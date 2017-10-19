import pytest


def test_book_argument_is_valid(book):
    from trigrams import main
    assert len(book) != 0 and type(book) == str