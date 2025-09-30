from stats import get_word_count, get_char_count, get_chat_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_word_count(text)
    char_count_dict = get_char_count(text)
    sorted_list = get_chat_list(char_count_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")

    print("============= END ===============")

main()
