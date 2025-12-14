from stats import get_num_words, count_characters, get_sorted_characters


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    char_counts = count_characters(text)
    sorted_chars = get_sorted_characters(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
