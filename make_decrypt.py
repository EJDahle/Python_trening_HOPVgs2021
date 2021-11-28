from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = b'.\xa4+\xfc\xad\x0c>\xa5\x03"9\xc64@&\xf2'
aesCipher = Cipher(algorithms.AES(key), modes.ECB(), backend = default_backend())
aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

print(aesDecryptor.update(b"/\xd0\xbe9\xa8i\x9d\x08\xf0\x8f^\xa4\x14q\x13\x8d%\xc9O\x08\x17Y\xe0{\xd6\x9ex%\x1ct\xbfs\x1a\x8a\xbb\xd8.&j\x983\xad\xd3vsK\r\xd2N\xc3\x9a\xbe9t\x9c0\x1aEw\xf1\x0cw\x0c\x8e\xc2\x9e6Y\x95\xa2\n\x99\x8eA\x97\xab1Hp\x18R'\xae\x1d7wX\xcax\x8e\xd8^\x9f\x84\xbb\x80"))
