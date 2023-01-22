import random
import string
import argparse

def generate_password(length: int) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a random password')
    parser.add_argument('-l', '--length', type=int, default=16, help='Password length')
    args = parser.parse_args()

    password = generate_password(args.length)
    print(password)
