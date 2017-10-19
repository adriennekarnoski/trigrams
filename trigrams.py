"""Generate trigrams from a book."""


def main(path, n):
    """Make a docstring."""
    with open(path) as book_file:
        book = book_file.read()
        print(book)


main('/test_book.txt')
