# Author: PiereLucas(Julian Huch)
# MIT LICENSE


"""
B64 Encoder
"""


import os
from base64 import b64encode


def read(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'rt') as f:
            data = f.read()
            data = bytes(data, encoding="UTF-8")
            key_dec = b64encode(data)
            print("B64 Encoded:")
            print(key_dec)

if __name__ == "__main__":
    file = input("Filepath: ")
    read(file)
