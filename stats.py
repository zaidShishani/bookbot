def count_total_book_letters(book):
    book = book.lower()
    letters = {}
    for ch in book:
        letters[ch] = letters.get(ch, 0) + 1
    return letters 

def build_counts_list(counts):
    lst = []
    for ch, cnt in counts.items():
        lst.append({"char": ch, "num": cnt})
    return lst

def total_count(book):
    words = book.split()
    count = len(words) 
    return count

