def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowercase_text = convert_lowercase(text)
    char_counts = get_char_count(lowercase_text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document \n")
    sorted_dict = generate_report(char_counts)
    for a in sorted_dict:
        if not a["char"].isalpha():
            continue
        print(f"The {a['char']} character was found {a['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def convert_lowercase(text):
    lowercase_text = text.lower()
    return lowercase_text

def get_char_count(text):
    char_count = {}
    for t in text:
        if t in char_count:
            char_count[t] += 1
        else:
            char_count[t] = 1
    
    return char_count

def sort_on(new_dict):
    return new_dict["num"]

def generate_report(sorted_dict):
    new_list = []
    for i in sorted_dict:
        new_list.append({"char": i, "num": sorted_dict[i]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list





main()