import sys
from stats import get_num_words, count_characters, get_sorted_characters


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    # Check for command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    # Read the book
    text = get_book_text(book_path)

    # Word count
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Character count
    char_counts = count_characters(text)
    sorted_chars = get_sorted_characters(char_counts)
    print("--------- Character Count -------")

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()

