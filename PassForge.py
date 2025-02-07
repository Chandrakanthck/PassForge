import random
import string
from itertools import permutations

def generate_sliced_words(base_word, max_permutations=5):
    sliced_words = set()
    for perm in permutations(base_word):
        if len(sliced_words) >= max_permutations:
            break
        sliced_word = ''.join(perm)
        sliced_words.add(sliced_word)
    return list(sliced_words)

def generate_password(base_word, min_length, max_length, special_chars, allow_slice=True):
    if allow_slice:
        base_options = generate_sliced_words(base_word)
    else:
        base_options = [base_word]
    
    chosen_base = random.choice(base_options)
    
    remaining_length = random.randint(
        max(min_length - len(chosen_base), 1),
        max_length - len(chosen_base)
    )
    
    all_chars = string.digits + special_chars
    suffix = ''.join(random.choices(all_chars, k=remaining_length))
    
    password = chosen_base + suffix
    return password

def main():
    base_word = input("Enter base word: ").strip()
    min_length = int(input("Min password length (e.g., 8): "))
    max_length = int(input("Max password length (e.g., 12): "))
    special_chars = input("Enter special characters (e.g., @!#): ").strip()
    allow_slice = input("Allow slicing? (y/n): ").lower() == 'y'
    num_passwords = int(input("Number of passwords to generate: "))
    
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(
            base_word, min_length, max_length, special_chars, allow_slice
        )
        passwords.append(password)
    
    with open("passwords.txt", "w") as f:
        f.write('\n'.join(passwords))
    print(f"\n {num_passwords} passwords generated! Check passwords.txt")

if __name__ == "__main__":
    main()