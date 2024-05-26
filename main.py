def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    result_get_each_char = get_each_char(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    
    for item in result_get_each_char:
        print(f"The {item["char"]} character was found {item["count"]} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def sort_on(item):
    return item["count"]
    

def get_each_char(text):
    each_char_dict = {}
    chars = text.lower()   
    for char in chars:
        if char.isalpha():
            if char in each_char_dict:
                each_char_dict[char] += 1
            else:
                each_char_dict[char] = 1
    
    result_get_each_char = [{"char": c, "count": k,} for c, k in each_char_dict.items()]
    result_get_each_char.sort(reverse=True, key=sort_on)

    return result_get_each_char



main()