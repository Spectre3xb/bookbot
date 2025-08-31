from stats import num_words
from stats import num_letters
from stats import sort_letters
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    letter_dict_list = sort_letters(num_letters(book))

    print(f"""
============ BOOKBOT ============
Analyzing book found at {sys.argv [1]}...
----------- Word Count ----------""")
    print(f"Found {num_words(book)} total words")
    print("--------- Character Count -------")
    for item in letter_dict_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")



main()


