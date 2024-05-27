import random
import string

# Function to generate a random password


def generate_password(length, include_numbers, include_sc):
    chars = string.ascii_letters
    if include_numbers:
        chars += string.digits
    if include_sc:
        chars += string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# User input for password length


length = int(input("Enter Length: "))

# User input for including numbers and special characters
include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
include_sc = input("Include specialcharacters?(y/n):").strip().lower() == 'y'

# Generate and print the password
password = generate_password(length, include_numbers, include_sc)
print("Your random password is:", password)
