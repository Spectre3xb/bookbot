from stats import num_words
from stats import num_letters
from stats import sort_letters

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    print(f"{num_words(get_book_text("books/frankenstein.txt"))} words found in the document")

    letter_dict = num_letters(get_book_text("books/frankenstein.txt"))
    print(letter_dict)
    #for letter in letter_dict:
    #    print(f"{letter}: {letter_dict[letter]}")

    sorted_list = sort_letters(letter_dict)
    print(sorted_list)

main()


