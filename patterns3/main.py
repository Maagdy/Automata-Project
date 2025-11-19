# main.py
from extractor import find_emails as extract_emails, find_phones as extract_phones, find_addresses as extract_addresses

def read_file(path):
    with open(path, "r") as f:
        return f.read()

def main():
    data = read_file("../data/random_data.txt")

    emails = extract_emails(data)
    
    phones = extract_phones(data)
    addresses = extract_addresses(data)

    print("=== EMAILS ===")
    print(emails[:20])
    print(f"Total: {len(emails)}\n")

    print("=== PHONES ===")
    print(phones[:20])
    print(f"Total: {len(phones)}\n")

    print("=== ADDRESSES ===")
    print(addresses[:20])
    print(f"Total: {len(addresses)}\n")

if __name__ == "__main__":
    main()
