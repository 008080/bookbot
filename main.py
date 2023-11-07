with open("books/frankenstein.txt") as f:
    file_content = f.read()

def word_count(text):
    words = len(text.split())
    return words

def letter_count(text):
    letters = {}
    for i in text.lower():
        if i.isalpha():
            if i not in letters:
                letters[i] = 1
            else:
                letters[i]+= 1
    list = []
    for i in letters:
        list.append([letters[i], i])
    list.sort(reverse=True, )
    print_letter_count(list)

def print_letter_count(list):
    for i in list:
        print(f" The '{i[1]}' character was found {i[0]} times")

print("--- Begin report of books/frankenstein.txt ---")        
print(f"{word_count(file_content)} words found in the document")
print("\n\n")
letter_count(file_content)
print("--- End report ---")