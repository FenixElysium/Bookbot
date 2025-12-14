def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    counts = {}

    for ch in text:
        ch = ch.lower()
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1

    return counts

