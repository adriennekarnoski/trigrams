"""Generate trigrams from a book."""


def main(path, n):
    """Make a docstring."""
    trigrams = generate_trigrams(book_into_list(path))


def book_into_list(path_to_book):
    """Break the book.txt file into a list of words without punctuation."""
    import string

    with open(path_to_book) as book_file:
        book = book_file.read()
        raw_word_list = book.split()
        word_list = []
        for word in raw_word_list:
            word_list.append(word.strip(string.punctuation))

    return word_list


def generate_trigrams(words):
    """Take in a list of words and return a dictionary of trigrams."""
    generated_trigrams = {}
    for idx, word in enumerate(words):
        pair = word[idx] + word[idx + 1]
        if pair in generated_trigrams:
            generated_trigrams[pair].append(word[idx + 2])
        else:
            generated_trigrams[pair] = [word[idx + 2]]

    return generated_trigrams

main('test_book.txt', 1)
