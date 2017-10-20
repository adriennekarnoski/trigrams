"""Return a string of n related words using trigrams from a .txt file."""


import random
import string


def main(path, n):
    """Return a string of n related words using trigrams from a .txt file."""

    trigrams = generate_trigrams(book_into_list(path))

    output = random.choice(list(trigrams)).split()

    while len(output) < n:
        for word in range(n - 2):
            pair_to_check = output[-2] + ' ' + output[-1]
            word_to_add = trigrams.get(pair_to_check)[0]
            output.append(word_to_add)

    print(' '.join(output))
    return ' '.join(output)


def book_into_list(path_to_book):
    """Make .txt file into a list of lower-case words without punctuation."""  

    with open(path_to_book) as book_file:
        book = book_file.read().lower()

    raw_word_list = book.split()
    word_list = []

    for word in raw_word_list:
        word_list.append(word.strip(string.punctuation).strip())

    return word_list


def generate_trigrams(words):
    """Take in a list of words and return a dictionary of trigrams."""
    generated_trigrams = {}
    for idx, word in enumerate(words):
        if idx == len(words) - 2:
            break

        pair = (words[idx] + ' ' + words[idx + 1])

        if pair in generated_trigrams:
            generated_trigrams[pair].append(words[idx + 2])

        else:
            generated_trigrams[pair] = [words[idx + 2]]

    return generated_trigrams


# main('test_book.txt', 100)


if __name__ == '__main__':
    import sys

    main(sys.argv[1], int(sys.argv[2]))
