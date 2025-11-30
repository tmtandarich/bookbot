def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    chars = {}
    for c in text:
        lowercase = c.lower()
        if lowercase in chars:
            chars[lowercase] += 1
        else:
            chars[lowercase] = 1
    return chars