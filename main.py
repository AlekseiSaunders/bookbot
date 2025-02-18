#main.py

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = book_words(text)
    char_library = book_characters(text)
    alpha_library = alpha_report(char_library)
    report = generate_report(book_path, num_words, alpha_library)

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
def book_words(text):
    words = str(text).split()
    return len(words)
        
def book_characters(text):
    characters = {}
    for char in text:
        if not char.lower() in characters:
            characters[char.lower()] = 1
        else:
            characters[char.lower()] += 1
    return characters  

def alpha_report(characters):
    alpha_list = {}
    for char,value in characters.items():
        if char.isalpha():
            alpha_list[char] = value
    return alpha_list

def generate_report(book, word_count, alpha_library):
    report = []
    file_name = "".join(book.split("/")[-1::])
    title = "".join(file_name.split(".")[0:1]).capitalize()
    report.append(f"--- Begin report of {file_name} ---\n")
    report.append(f"{word_count} words found in the document\n\n")
    for key,value in alpha_library.items():
        report.append(f"The '{key}' character was found {value} times\n")
    report.append(f"--- End report ---")
    return " ".join(report)
        
main()
