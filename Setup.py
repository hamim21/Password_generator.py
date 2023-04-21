import string

import random

import argparse

def generate_password(length, uppercase=False, lowercase=False, numbers=False, special=False):

    chars = ''

    if uppercase:

        chars += string.ascii_uppercase

    if lowercase:

        chars += string.ascii_lowercase

    if numbers:

        chars += string.digits

    if special:

        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))

    return password

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Generate a random password')

    parser.add_argument('-l', '--length', type=int, default=8, help='Length of the password (default: 8)')

    parser.add_argument('-u', '--uppercase', action='store_true', help='Include uppercase letters')

    parser.add_argument('-c', '--lowercase', action='store_true', help='Include lowercase letters')

    parser.add_argument('-n', '--numbers', action='store_true', help='Include numbers')

    parser.add_argument('-s', '--special', action='store_true', help='Include special characters')

    args = parser.parse_args()

    password = generate_password(args.length, args.uppercase, args.lowercase, args.numbers, args.special)

    print(password)

