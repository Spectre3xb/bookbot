def num_words(text):
    return len(text.split())

def num_letters(text):
    letters_count = {}
    txt = text.lower() #making the whole text lower case
    letters = list(txt)
    for letter in letters: #iterates only over the keys
        if letter not in letters_count:
            letters_count[letter] = 1
        else:
            letters_count[letter] += 1
    return letters_count

def sort_on(items):
    return items["num"]

def sort_letters(letters_dict):
    chars = []
    for key in letters_dict:
        if key.isalpha():
            char_dict = {"char": key, "num": letters_dict[key]}
            chars.append(char_dict)
        sorted = chars.sort(key=sort_on, reverse=True)
    return sorted



