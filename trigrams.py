"""Generate trigrams from a book."""


def main(path, n):
    """Make a docstring."""
    import string
    with open(path) as book_file:
        book = book_file.read()
        raw_word_list = book.split()
        word_list = []
        for word in raw_word_list:
            word_list.append(word.strip(string.punctuation))

        print(word_list)


main('test_book.txt', 1)
