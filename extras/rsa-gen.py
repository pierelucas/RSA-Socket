# Author: PiereLucas(Julian Huch )
# MIT LICENSE


"""
Generate new RSA Keys
"""


import os
import shutil
import string
import random
from Crypto.PublicKey import RSA


def rnd_str():
    letters = string.ascii_lowercase + string.digits
    return "".join(random.choice(letters) for i in range(6))

def gen():

    key_ = RSA.generate(4096)
    publickey_ = key_.publickey()

    key = key_.exportKey()
    publickey = publickey_.exportKey()

    if os.path.isfile("cryptkey.txt"):
        new_name = "cryptkey_" + rnd_str() + ".txt"
        shutil.move("cryptkey.txt", new_name)
        print("Old Private-Key backup'd:", new_name)

    if os.path.isfile("cryptkey_public.txt"):
        new_name = "cryptkey_public_" + rnd_str() + ".txt"
        shutil.move("cryptkey_public.txt", new_name)
        print("Old Public-Key backup'd:", new_name)

    with open("cryptkey.txt", 'wb') as private, open("cryptkey_public.txt", 'wb') as public:
        private.write(key)
        public.write(publickey)
    print("Keys sucessfully generated")

if __name__ == "__main__":
    gen()
