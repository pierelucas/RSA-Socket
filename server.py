# Author: PiereLucas(Julian Huch)


import socket
from base64 import b64decode
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class Crypter():

    def __init__(self):
        self.key = ""
        self.data = ""
        self.dec_data = ""

        # Decode Key
        self.privatekey_dec()

    def privatekey_dec(self):

        key = b'LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlKS0FJQkFBS0NBZ0VBeGZNanRKTGF1dnR5SUxyM3BOaHdlT0lvN3dwYXBV' \
              b'SjFMU2lKOTkrVEk2WXNEQ1hKClFvQXNCUUlkbi9ib0lvazRNWVFtREpnU0FyT29TUkViUjRhRFkxRUxIRysyWlRMN0JRL1VFNlBVSlNW' \
              b'UERlSnEKMXUzSDRpREpJeHFPR0tjL200ejNOTUlPYTVlUjhHdHQxOWdEaGlhYVhsT3lVMFNwd3VHUUdPbk84cy8xK2wvMgovaU5qbklM' \
              b'M0dWcHgzSjJQQ1VFVWtxTDlTN25JQnFvYlpHS0hkSnIyRGxiN1QybzU4NHlvb3Q5dG5JYmwyQUpNCmtPdnVNQnZxeC85ZVBaQWlnbVZz' \
              b'KzBrcWN5MzI5dENFdkNhcU4rNElTUkVhbXI2cWwvM3lWRGFLNEowMlEzUGEKczF6TVhRbmtOR1BtcGlzQ2FTc2dKQXJHUXRlQk1ubmUr' \
              b'a3diVktQcUU4UTY1cDBkMU8yajB3SzZkRHVmeG1odQpuYXh1VGEzNTFJcVVKRVREcmZmVFZ4WWphM0h4a3dTOWlZTWczT2dmdzA2MTdM' \
              b'NEpzSDJWTVU3aDJWWnhoNGhsCkNXMUt0bnU2UVFUTlhyY1czeWgrSXZJZXJOWFJvN01ZbTB5ZlpRTm04L1ora1ZGTFhiSXFTRGFMOGxT' \
              b'VE5BQmkKeHlpaEZiSitGTHZPR256UlAzNkVSR00rNTJRU3VldGFXUTk5WW5BbDR2S0psZko2MWl3REVYKzBwUC9jUkxvVgpBaTBONWIr' \
              b'REV2THVyNVlNTU51MndwZkJROHRTTExXQnZ6V2xxTUdNcjdUcU1SVmFVTm1xcm1rY3pCWnExbWUzClB0a2pxNGp3SnByUmRrQ2I0LzA1' \
              b'bDc1MUxQWUJCNDFVYVdOWHlvS1NFeWw3RnhEKzRTNjNtZlU2c3dVQ0F3RUEKQVFLQ0FnQkxqK0dzVjNhcGM3eUFJLzdPYlZTWndITXh0' \
              b'SGtmcG52R1RqaEVaNUxxUTgrQ241WHhEYTVBQnl1NQoyVzJKYVdvSzlNLzFkTU5EUnNOUmlQY3AyWDRrRmxhd2R6QmY5eEw5UHFxTkNM' \
              b'ZTlxajFBSnBMMEVuWi9xbFk5ClVUQzIxbmtnYnJJYThJekNvMnd4STBFZDZMYUhxZ3E1UVNmTVEyU3VJSjU1OUI1c2I5Z015RDhuaWVq' \
              b'SFlQTGsKT2JOSExObmlCWGJOOXV2TDBWSTZ3UXFOeWxLOHZ6NTRBTm9UMlkvZm1XenlKMm5YRzJOM2pvRWR2UUlDV1ZYSgpISUVqN1Ba' \
              b'UFlsbzBuaHhYTlUrVnJjbE5iVkVDNHBsRkV3TmQyTFNVS25zcmpGcDlIV1lPWDVZM2E1QVRYK2c5CjIzaTdLNlhTOFlSbVhicUszMnJS' \
              b'RXRaOEl6czI2ZUNxelJKQmwzcG1na0I4SzQyN09RcmE5bHVqR1lVSDdHRFAKVlhnbFVtamFYUFdWdUhmUVRNaVdsdGE5SVlaQ0xJbjhR' \
              b'cHQyUDVCSUZtbzZvdWdmVDc3ZDFNdGx1U3IrMzc4Qgo1VWsvWXU5b2N6MERCTUw1NWNxYndZRWtRK1lzdWdNWW1JM2dmcHplVkQrVElu' \
              b'Y1JPWGdsNmZtSXQ5MUtab3RFCk5aRXJ0NGR0d2JZMjlZWXQyN29yczBUbGMyS3FJMlUzL1kyYmRPaVpDMGdmRGNHZzRlbnhuTmw2ejVV' \
              b'ZWZ3ci8KMXh4bW1hTjA5UkVpOWtOMHpLZ1JkaDFqenZ4NHhvbmNlemNJYnRQZEs0VjMyRXl5L3dpSXFSTHhPbythaXUwMApObStwVDdC' \
              b'ZXNVMy9TL3gxczJxajBDWlZJQ1hVUjJENnhjZFViQXF5Ym1aMTh2TXY3UUtDQVFFQXh1WDB0cTNFCnZOWjNJY2JBMXZEVmoxclIwcFRq' \
              b'djZOL3dWeU9Ic2M3T0VsZXRMbVNsNm5GYStyWEZuRkw4cXY4U21abXNyRTQKSm1JT0IvVnJOcDV6cDVOU3VWMTFyTTBDZFpxYnlKNHRj' \
              b'RGxzUngvbWdCMkVWRDU0SWoreTFoRjhrTXdBZ0tZVApyQ0x1NldycHJvZnR0L2R0ODAydzE3RWlEVEtYSzgzSkJwalp2Y2s2bVdFekVx' \
              b'YkNmOVFncGNrUk0vOTBUL3d2Cnl4aXMwUlNIQUFnZlBWNWlESmN4Ymd4SkUxNU5XYnR6dTdwWnhkNVhPclVNMjJwSWE1cEN6d05yMmQx' \
              b'SmZERjQKdDFmcHNUZ1NHc3R5Y2dPaXNIQkhEQ00yQ2xycFdaUHpaZ2t6ZzBZU0J6WTQwa3h3cTJhbVJvVWxtY1dzeU8vdwpFTDdZSTJi' \
              b'QWsrR25Ld0tDQVFFQS9zZDVMWkhrNW0zTlJMZEJiVVVTMGZ6UCtzWFpXVnByckRNNUNJNDBVOW40CmJTdFNEQk1WeXY0M1pmcm9tTDNI' \
              b'MnE1QUw2eDg1TWs3dG0wK0ZnWlMvUmtIdHhUNkplOGRsekxiUmRVbndocUoKTzZFSTUyQ29EWnZmZGlaOHN0S0xlb1JwWVJhVm14Mll0' \
              b'ODEzYXV2TXNXTlRBbzduaVc4UVdkN2I2YkNoYjZPVApUeFV2T1VMeU4vdHJTMkx0OGJYbDZRTmo2YjlyQlAxWW1qWVRwMGR2R1NXY0gz' \
              b'eVNDWk0vY3FEOThNQm16T3lPCncxaDhVTVlsK0RkbXVqYWhDcVZrWWswWnVwTFhVRGp4OGQ1TW9rT2FxbW9zT0JoRmdWOEFQOFBSazRQ' \
              b'bGh3WUQKQjVjSHFsV1ZCazFxNGZLZXVxMmQzZTJsUUZ3T3ptZGR4ZFdtWlNIMmp3S0NBUUFkNmo1Skw0K1VtMmtsb21BawpzK3BhK2x6' \
              b'dW9FZzA3YUZzY3NCSmJzdkFab0NoQy93NVpXWjFHY2dwN3ZadVZHSEl5dWdOWGt4RXNhRE1uNlAxCmZoV0ZFY3B5YU5VbkhWcU9WNmV3' \
              b'bitIVHJEOVYzejFxN1lXV3FpS2xmQkVvMDA1NTlNVHFsSkFHNXVZcUkxTnMKVmJOeVpQdWJpWWJjbWg2MS8zTHZPcTlPbDdUQUw4RHBp' \
              b'czRFc3lJejJiTGpYSCtDNDV3WjM2Tk1sN1IrYWVqNApIMENibVZPRDgwV1MrTFFRL3JFQm13a0lKam9VWWFHYkNkb2FNajBjT2dKc1lt' \
              b'WlpTVWdoTHN1cVA4VzlTdUttCk53MUtpck53ZUNLbmQ3Qk1GR3BlZDdzM0VKRTM0RlViMHBMdlJtSDMxYU9TbmJvUEM4VTJINmhxekZs' \
              b'ejBhT0wKV25nckFvSUJBUURJRE5KdVlLY044OXVBZ0RBRVgzODJtTDZwbHA1aUZhaUR6cmlTcWk0V1JRbFdsdlJXZk1uWQoyU0dnbHBI' \
              b'NkZOSVBPRkUzM2NVM1UzYnFkLzZQQnFvMUIybFNiVXM1YS9hZEdSYXBUNFJuV2JTMXVHMG9XSEc4Ck5jOFJrNGpJVkorbU5NQVZ0c2tE' \
              b'd2dwL0Qvc2JYa2tjWS9QekIwaHdWbC9OWVRybDFJWCtCYitPRWdGQmdmcDAKMEpwZjJDOGpZb05ESWlGYWthMnpma1lLMkRrNFdOTzRP' \
              b'QnJOY2wrczJ3eXZzZytTOFZBR3lod1M4TEMwTDlIeQpnM1hLODBnaDl0bktnZVdZNU9IaG9NVUErRjdON2kxTWNBK0dnREJiTThBYlVX' \
              b'T0c0OExlOFc2QmtDbzVxZmRZCnVvTVpKUXRUWXkyWTY1ZWM0R3ZUejhBR3JncDRVR0dyQW9JQkFDVm5peHBLOXNiNkUvT0ZZMVFJSmpX' \
              b'cGhJVlIKM2hMSHRWcXVYWkM4bGhudStQa2duUkNlMHVSWmdNVXFZZEhHd3hBVW41UGdheldZZ0JvbWdneFZINXl2enJhdwpERE85WVo0' \
              b'NXduWjYyWUJ4RjZSaGljL3orVU1ZZ3UxY3FTTTY0N0FmNkMzK3JiWFYyRnV1L21KMHVlYllsL29YCjZSNWxHeEx5aEoxTjFCSmZvSHlR' \
              b'WFhnOVFWWEcxekpoSWgyU3cwL0UvNVByN0tGYVFoR2dsME9NRmUyR1NwTWQKdm83Qk1IMFY4M3djQ0tickZSWmJUeU9MbUlsbklvY1Vs' \
              b'a2JlclVNcmYvU2VyQVpKdFlVSERIcU5GaHNqdlN0cgpYTkZ3T05hN0tCMFFVSHFGSm5mTXp2VGFmeWdhOUxSUUswWEVmejVxYitQbG1N' \
              b'WUtDYzdXZDU1RWNRND0KLS0tLS1FTkQgUlNBIFBSSVZBVEUgS0VZLS0tLS0='

        self.key = str(b64decode(key), encoding="UTF-8")

    def dec(self, data):

        key = RSA.importKey(self.key)
        pkcs1 = PKCS1_OAEP.new(key)
        dec_data = pkcs1.decrypt(data)
        return str(dec_data, encoding="UTF-8")


class Receiver(Crypter):

    def __init__(self, ip, port, buffer_size=1024):
        super(Receiver, self).__init__()
        self.bind_ip = ip
        self.bind_port = port
        self.buffer_size = buffer_size

    def start_receive(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.bind((self.bind_ip, self.bind_port))
            data, src_ip = sock.recvfrom(bufsize=self.buffer_size)
        dec_data = self.dec(data)
        return dec_data, src_ip[0]


