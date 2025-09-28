from stats import get_word_count, get_char_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_word_count(text)
    char_count_dict = get_char_count(text)
    print(f"Found {num_words} total words")
    print(char_count_dict)

main()
