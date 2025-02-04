def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words = file_contents.split()
    word_count = len(words)
    
    letters_counted = count_letters(file_contents)
    letter_list = []
    for letter in letters_counted:
        letter_dict = {"char": letter, "count": letters_counted[letter]}
        letter_list.append(letter_dict)

    letter_list.sort(reverse=True, key=sort_on)
    
    print_report(word_count,letter_list)

def count_letters(book):
    letter_count = {}
    book_lowered = book.lower()
    
    for k in book_lowered:
        if k in letter_count:
            letter_count[k] +=1
        else:
            letter_count[k] = 1
    
    return letter_count

def sort_on(dict):
    return dict["count"]

def print_report(word_count, letter_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    
    for letter in letter_list:
        if letter["char"].isalpha():
            print(f"The '{letter['char']}' character was found {letter['count']} times")
    
    print("--- End report ---")


main()
