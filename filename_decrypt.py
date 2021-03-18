from Crypto.Cipher import AES
import base64

def unpad(ct):  return ct[:-ct[-1]]

enc_name = '7z2rdffDKyELLqEp9fiVDQ'
enc = base64.b64decode(enc_name + '==')

key = b'202cb962ac59123\x00'
iv = key
cipher = AES.new(key, AES.MODE_CBC, iv)
dec = cipher.decrypt(enc)
dec_name = unpad(dec).decode()
print(dec_name)
