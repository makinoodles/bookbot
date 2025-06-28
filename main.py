import sys 

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
 
else :
    filepath = sys.argv[1]

def main():
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    sort_char = sort_char_count(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sort_char:
        print(f"{char}: {count}")
    print("============= END ===============")
   
  
from stats import get_num_words

from stats import get_char_count

from stats import sort_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
   

main()