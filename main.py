def word_count(book):
    words = book.split()
    return len(words)

def letter_count(book):
    letter_count = {}

    for letter in book:
        if letter.lower() in letter_count:
            letter_count[letter.lower()] += 1
        else:  
            letter_count[letter.lower()] = 1
    return format_report(letter_count)

def format_report(letter_count):   
    return dict(sorted(letter_count.items(), key=lambda item:item[1], reverse=True))

def print_report(letter_count):
    for letter in letter_count:
        if letter.isalpha():
            print(f"The '{letter}' character was found {letter_count[letter]} times")

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(file_contents)} \n")
    report = letter_count(file_contents)
    print_report(report)
    print("--- End report ---")
