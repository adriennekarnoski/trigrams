"""Test the trigrams file."""


import pytest


def test_list_returned_from_book():
    """Verify word_list is returned as a list of words."""
    from trigrams import book_into_list
    word_list = book_into_list('test_book.txt')
    assert type(word_list) == list


def test_length_returned_from_book():
    """Verify word_list is not zero."""
    from trigrams import book_into_list
    word_list = book_into_list('test_book.txt')
    assert len(word_list) != 0


def test_list_passed_to_function():
    """Verify list is passed to trigrams function."""
    from trigrams import book_into_list, generate_trigrams
    word_list = book_into_list('test_book.txt')
    trigram = generate_trigrams(word_list)
    assert trigram


def test_keys_available_in_dictionary():
    """Test that keys are created for dictionary."""
    from trigrams import book_into_list, generate_trigrams
    word_list = book_into_list('test_book.txt')
    trigram = generate_trigrams(word_list)
    assert len(trigram) != 0


def test_main_function_taking_dictionary():
    """Test to verify main function is accepting trigram dictionary."""
    from trigrams import main
    returned_trigram = main('test_book.txt', 500)
    assert returned_trigram


def test_main_returns_correct_word_amount():
    """Test that the functions return the amount of words requested."""
    from trigrams import main
    returned_trigram = main('test_book.txt', 500)
    assert len(returned_trigram.split()) == 500

