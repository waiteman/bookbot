def main(): 
    #open_frankenstein()
    current_book = "books/frankenstein.txt"
    print(count_words(current_book))
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




main()