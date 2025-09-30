def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_dict = {}

    for char in text.lower():
        if char not in char_dict:
            char_dict.update({char: 1})
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def get_chat_list(char_dict):
    char_list = []
    for key in char_dict:
        char_list.append({"char": key, "num": char_dict[key]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


