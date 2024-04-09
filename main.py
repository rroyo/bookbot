def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_text(book_path)
    num_words = get_num_words(book_content)
    num_chars = get_num_chars(book_content)
    sorted_chars_list = dict_to_sorted_list(num_chars)
    print_data(num_words, sorted_chars_list, book_path)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_num_words(content):
    num_words = len(content.split())
    return num_words

def get_num_chars(content):
    lowercase_text = content.lower()
    chars_dict = {}
    for char in lowercase_text:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def alpha_sort(char_dict):
    return char_dict["count"]

def dict_to_sorted_list(dict):
    sorted_list = []
    for char, count in dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "count": count})
    sorted_list.sort(reverse=True, key=alpha_sort)
    return sorted_list

def print_data(num_words, chars, book_name):
    print(f"--- Begin report of {book_name} ---")
    print(f"{num_words} words found in document")
    print("")
    for char in chars:
        print(f"The '{char['char']}' character was found {char['count']} times")

main()
