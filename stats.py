def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_dict = {chr(x):0 for x in range(ord('a'), ord('z')+1)}

    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
    return char_dict
