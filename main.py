def main(): 
    #open_frankenstein()
    current_book = "books/frankenstein.txt"
    #print(count_words(current_book))
    #print(book_to_strings(current_book))
    frankenstein = book_to_single_string(current_book)
    print (count_characters(frankenstein))
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
            


main()