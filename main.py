from stats import count_total_book_letters, build_counts_list, total_count
import sys

def sort_on(items):
    return items["num"]

def get_book_text(title):
    with open(str(title)) as f:
        content = f.read()
    counts = count_total_book_letters(content)      
    counts_list = build_counts_list(counts)         
    counts_list.sort(reverse=True, key=sort_on)

    
    total = total_count(content)

    print(f'Found {total} total words')
    for item in counts_list:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")

    return counts_list, total


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    get_book_text(sys.argv[1])

main()

