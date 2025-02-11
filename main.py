def main(): 
    #open_frankenstein()
    current_book = "books/frankenstein.txt"
    word_count = count_words(current_book)
    #print(book_to_strings(current_book))
    frankenstein = book_to_single_string(current_book)
    char_dic = (count_characters(frankenstein))
    char_dic_list = convert_dic_to_list(char_dic)
    sorted_list = sort_list(char_dic_list)
    print_report(current_book, sorted_list, word_count)
    
    return None

def open_frankenstein(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def count_words(book_file):
    with open(book_file) as f:
        file_contents = f.read()
        word_list = file_contents.split()
    return len(word_list)

def book_to_strings(book_file):
    with open(book_file) as f:
        file_contents = f.read()
        word_list = file_contents.split()
    return word_list

def book_to_single_string(book_file):
    with open(book_file) as f:
        file_contents = f.read()
    return file_contents

def count_characters(word_list):
    char_dic = {}
    for word in word_list:
        lowered_word = word.lower()
        for char in lowered_word:
            if char in char_dic:
                char_dic[char] += 1
            else:
                char_dic[char] = 1
    return char_dic
            
def convert_dic_to_list(char_dic):
    char_list = []
    for char in char_dic:
        if char.isalpha():
            char_list.append({"char": char, "num": char_dic[char]})
    return char_list

def sort_on(dict):
    return dict["num"]

def sort_list(char_dic_list):
    char_dic_list.sort(reverse=True, key=sort_on)
    return char_dic_list

def print_report(book, list, count):
    print(f"--- Begin report of {book} ---")
    print(f"{count} words found in the document\n")
    for item in list:
        print(f"The '{item["char"]}' character was found {item["num"]} times")


main()