import itertools
import random

def generate_all_passwords(base_word, min_length, max_length, special_chars, allow_slice):
    """Generates all possible passwords based on given rules."""
    passwords = set()
    word_variations = [base_word[:i] for i in range(1, len(base_word) + 1)] if allow_slice else [base_word]

    for word in word_variations:
        for length in range(min_length, max_length + 1):
            if len(word) >= length:
                passwords.add(word[:length])  # Direct slice
            else:
                extras = itertools.product(special_chars or "0123456789", repeat=length - len(word))
                for extra in extras:
                    passwords.add(word + ''.join(extra))

    return sorted(passwords)

def generate_random_passwords(base_word, min_length, max_length, special_chars, allow_slice, num_passwords):
    """Generates a fixed number of passwords randomly."""
    passwords = set()
    
    while len(passwords) < num_passwords:
        word = base_word[:random.randint(1, len(base_word))] if allow_slice else base_word
        while len(word) < min_length:
            word += random.choice(special_chars or "0123456789")
        passwords.add(word[:max_length])

    return sorted(passwords)

def main():
    base_word = input("Enter base word: ").strip()

    while True:
        try:
            min_length = int(input("Min password length: "))
            max_length = int(input("Max password length: "))
            if min_length > max_length or min_length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input! Min length should be ≤ Max length and both positive numbers.")

    special_chars = input("Enter allowed special characters (e.g., @!#): ").strip()
    allow_slice = input("Allow slicing? (y/n): ").strip().lower() == 'y'
    
    gen_type = input("Generate (1) Fixed number or (2) All possible? Enter 1 or 2: ").strip()
    
    if gen_type == "1":
        while True:
            try:
                num_passwords = int(input("Number of passwords to generate: "))
                if num_passwords <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input! Enter a positive number.")

        passwords = generate_random_passwords(base_word, min_length, max_length, special_chars, allow_slice, num_passwords)
    
    elif gen_type == "2":
        passwords = generate_all_passwords(base_word, min_length, max_length, special_chars, allow_slice)
    
    else:
        print("Invalid option! Exiting...")
        return
    
    with open("passwords.txt", "w") as f:
        f.write('\n'.join(passwords))

    print(f"Generated {len(passwords)} passwords. Check passwords.txt!")

if __name__ == "__main__":
    main()
