# Author: PiereLucas(Julian Huch)
# Client Module for comfortable sending of encrypted data over udp


import socket
from base64 import b64decode
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class Crypter():

    def __init__(self, data):
        self.data = data
        self.key = self.publickey_dec()
        self.enc_data = self.enc()

    def publickey_dec(self):

        rot_key = b'LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQ0lqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FnOEFNSUlDQ2dLQ0FnRUF4Zk1q' \
                  b'dEpMYXV2dHlJTHIzcE5odwplT0lvN3dwYXBVSjFMU2lKOTkrVEk2WXNEQ1hKUW9Bc0JRSWRuL2JvSW9rNE1ZUW1ESmdTQXJPb1NS' \
                  b'RWJSNGFEClkxRUxIRysyWlRMN0JRL1VFNlBVSlNWUERlSnExdTNINGlESkl4cU9HS2MvbTR6M05NSU9hNWVSOEd0dDE5Z0QKaGlh' \
                  b'YVhsT3lVMFNwd3VHUUdPbk84cy8xK2wvMi9pTmpuSUwzR1ZweDNKMlBDVUVVa3FMOVM3bklCcW9iWkdLSApkSnIyRGxiN1QybzU4' \
                  b'NHlvb3Q5dG5JYmwyQUpNa092dU1CdnF4LzllUFpBaWdtVnMrMGtxY3kzMjl0Q0V2Q2FxCk4rNElTUkVhbXI2cWwvM3lWRGFLNEow' \
                  b'MlEzUGFzMXpNWFFua05HUG1waXNDYVNzZ0pBckdRdGVCTW5uZStrd2IKVktQcUU4UTY1cDBkMU8yajB3SzZkRHVmeG1odW5heHVU' \
                  b'YTM1MUlxVUpFVERyZmZUVnhZamEzSHhrd1M5aVlNZwozT2dmdzA2MTdMNEpzSDJWTVU3aDJWWnhoNGhsQ1cxS3RudTZRUVROWHJj' \
                  b'VzN5aCtJdkllck5YUm83TVltMHlmClpRTm04L1ora1ZGTFhiSXFTRGFMOGxTVE5BQml4eWloRmJKK0ZMdk9HbnpSUDM2RVJHTSs1' \
                  b'MlFTdWV0YVdROTkKWW5BbDR2S0psZko2MWl3REVYKzBwUC9jUkxvVkFpME41YitERXZMdXI1WU1NTnUyd3BmQlE4dFNMTFdCdnpX' \
                  b'bApxTUdNcjdUcU1SVmFVTm1xcm1rY3pCWnExbWUzUHRranE0andKcHJSZGtDYjQvMDVsNzUxTFBZQkI0MVVhV05YCnlvS1NFeWw3' \
                  b'RnhEKzRTNjNtZlU2c3dVQ0F3RUFBUT09Ci0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQ=='

        return str(b64decode(rot_key), encoding="UTF-8")

    def enc(self):

        key = RSA.importKey(self.key)
        pkcs1 = PKCS1_OAEP.new(key)
        enc_data = pkcs1.encrypt(self.data.encode())
        return enc_data


class Send(Crypter):

    def __init__(self, ip, port, data):
        super(Send, self).__init__(data)
        self.ip = ip
        self.port = port

    def send_udp(self):
        try:

            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.settimeout(10)
                sock.sendto(self.enc_data, (self.ip, self.port))
            return True

        except Exception:
            return False
