#main.py
import sys
from stats import get_number_of_words, char_counter, sorting_dict, sort_on



def main():
    
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        count = get_number_of_words(text)
        counted_chars = char_counter(text)
        sorted_dict = sorting_dict(counted_chars)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {count} total words")
        print("--------- Character Count -------")
        for item in sorted_dict:
            print(f"{item["char"]}: {item["num"]}")
        print("============= END ===============")




def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents




main()
