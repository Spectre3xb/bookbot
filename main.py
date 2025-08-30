def get_book_text(path):
    with open(path) as f:
        return f.read()

def num_words(text):
    return len(text.split())

def main():
    print(f"{num_words(get_book_text("books/frankenstein.txt"))} words found in the document")

main()


