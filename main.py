from stats import num_words
from stats import num_letters
from stats import sort_letters

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book = get_book_text("books/frankenstein.txt")
    letter_dict_list = sort_letters(num_letters(book))

    print("""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
""")
    print(f"{num_words(book)} words found in the document")
    print("--------- Character Count -------")
    for item in letter_dict_list:
        print(f"{item["num"]}: {item["char"]}")
    print("============= END ===============")



main()


