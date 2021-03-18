import hashlib
from Crypto.Cipher import AES
from Crypto.Util import Counter
import Crypto
import base64

f = open('7z2rdffDKyELLqEp9fiVDQ.6zu', 'rb+')
enc_img = f.read()
f.close()

key = hashlib.sha1('1234'.encode()).digest()[:16]
iv = key
print(int.from_bytes(iv, 'big'))

counter = Counter.new(128, initial_value=int.from_bytes(iv, 'big'))
cipher = AES.new(key, AES.MODE_CTR, counter=counter)
dec_img = cipher.decrypt(enc_img)

f = open('downloadfile.jpeg', 'wb+')
f.write(dec_img)
f.close()
