def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    letters = get_num_letters(text)
    print(f'These letters are used:')
    print(letters)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_letters(text):
    letter_dict = {}
    for letter in text:
        if letter.isalpha() == False:
            continue
        if letter.lower() not in letter_dict:
            letter_dict[letter.lower()] = 1
        else:
            letter_dict[letter.lower()] += 1

    return letter_dict

def convert_dict(dict):
    list = []
    for key in dict.keys():
        new_dict = {}
        new_dict["char"] = key
        new_dict["count"] = dict[key]
        list.append(new_dict)
        
    return new_dict




def sort_occurences(dict):
    return dict["count"]


if __name__== '__main__':
    main()