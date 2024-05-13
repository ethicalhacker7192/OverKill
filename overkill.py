import random
import string
import base64
import urllib.parse
import os
import argparse
from tqdm import tqdm

d = '''
   ___                 _  ___ _ _ 
  / _ \__   _____ _ __| |/ (_) | |
 | | | \ \ / / _ \ '__| ' /| | | |
 | |_| |\ V /  __/ |  | . \| | | |
  \___/  \_/ \___|_|  |_|\_\_|_|_|
                                                                                    
The password generator that makes you scream "What the heck!?"

'''

def random_transformation(text, probability, iterations):
    print(d)
    bytes_list = []  # Initialize an empty list to store bytes
    for _ in tqdm(range(iterations), desc="Generating password..."):
        if random.random() < probability:  # Controlled chance to perform an operation.
            operation = random.choice(['insert', 'replace', 'delete', 'b64', 'hex', 'rot13', 'url', 'ascii'])
            position = random.randint(0, len(text) - 1) if len(text) > 0 else 0

            if operation == 'insert':
                char = random.choice(string.ascii_letters + string.punctuation + string.digits)
                text = text[:position] + char + text[position:]
            elif operation == 'replace' and len(text) > 0:
                char = random.choice(string.ascii_letters + string.punctuation + string.digits)
                text = text[:position] + char + text[position + 1:]
            elif operation == 'delete' and len(text) > 0:
                text = text[:position] + text[position + 1:]
            elif operation == 'b64':
                text_b64 = base64.b64encode(text.encode())
                bytes_list.append(text_b64)
            elif operation == 'hex':
                text_hex = text.encode().hex()
                bytes_list.append(bytes.fromhex(text_hex))
            elif operation == 'rot13':
                text_rot13 = text.translate(str.maketrans(
                    string.ascii_lowercase + string.ascii_uppercase,
                    string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
                    string.ascii_uppercase[13:] + string.ascii_uppercase[:13]
                )).encode()
                bytes_list.append(text_rot13)
            elif operation == 'url':
                text_url = urllib.parse.quote(text)
                bytes_list.append(text_url.encode())
            elif operation == 'ascii':
                text_ascii = text.encode('ascii', 'ignore')
                bytes_list.append(text_ascii)

    return b''.join(bytes_list)  # Concatenate all bytes in the list and return the password.

def main():
    parser = argparse.ArgumentParser(description=d, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-o', '--output', default='password.txt', help='Output file to write the transformed text to.')
    parser.add_argument('-r', '--random', type=int, default=500, help='Units of urandom to use.')
    parser.add_argument('-p', '--probability', type=float, default=0.5, help='Probability of an operation. (0.01 to 1)')
    parser.add_argument('-i', '--iterations', type=int, default=1000000, help='Iterations taken to create a password, higher is more secure, while lower is faster.')
    args = parser.parse_args()

    initial_text = str(os.urandom(args.random))  # Initial random data
    final_text = random_transformation(initial_text, args.probability, args.iterations)

    with open(args.output, 'wb') as f:
        f.write(final_text)
    print(f"Generated password written to {args.output}")

if __name__ == '__main__':
    main()
