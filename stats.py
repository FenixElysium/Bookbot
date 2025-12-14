def get_num_words(text):
    return len(text.split())


def count_characters(text):
    counts = {}
    for ch in text:
        ch = ch.lower()
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts


def sort_on(item):
    return item["num"]


def get_sorted_characters(char_counts):
    char_list = []

    for ch, count in char_counts.items():
        if ch.isalpha():  # skip non-alphabetical characters
            char_list.append({"char": ch, "num": count})

    char_list.sort(reverse=True, key=sort_on)
    return char_list

