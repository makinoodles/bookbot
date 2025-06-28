def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    text = text.lower()
    count = {}

    for char in text:
        if char.isalpha():
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

    return count

def sort_char_count(text):
    count = get_char_count(text)
    sorted_count = sorted(count.items(), key=lambda item: item[1], reverse=True)
    return sorted_count

