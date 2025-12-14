from stats import get_num_words, count_characters


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book_text = get_book_text("books/frankenstein.txt")

    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    char_counts = count_characters(book_text)
    print(char_counts)


main()

