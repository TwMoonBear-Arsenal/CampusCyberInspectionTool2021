import base64
from Crypto.Cipher import AES
from Crypto import Random
import os
import base64
import json

def add_to_16(text):
    while len(text) % 16 != 0:
        text += '\0'
    return (text)

key = 'Fcniggersm'
key = add_to_16(key) 

def decode_base64(data):
    missing_padding = 4-len(data)%4
    if missing_padding:
        data += b'='*missing_padding
    return (data)

message = 'gYknrv3zMWYXEpRLDL0n8q+6s68DKapAfRpBDhN1XGM='
encrypt_data = message 
encrypt_data = decode_base64(encrypt_data)

cipher = AES.new(key)
result2 = base64.b64decode(encrypt_data)
a = cipher.decrypt(result2)

a = a.decode('utf-8','ignore')
a = a.rstrip('\n')
a = a.rstrip('\t')
a = a.rstrip('\r')
a = a.replace('\x06','')
print('\n','data:',a)


def encrypt(data, password):
    bs = AES.block_size
    pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    cipher = AES.new(password)
    data = cipher.encrypt(pad(data))
    return (data)
    
if __name__ == '__main__':
    data = 'ni hao'
    password = 'aesrsasec' #16,24,32位长的密码
    password = add_to_16(password)        
    encrypt_data = encrypt(data, password)
    encrypt_data = base64.b64encode(encrypt_data)
    print ('encrypt_data:', encrypt_data)
 
def decrypt(data, password):
    bs = AES.block_size
    if len(data) <= bs:
        return (data)
    unpad = lambda s : s[0:-ord(s[-1])]
    iv = data[:bs]
    cipher = AES.new(password, AES.MODE_CBC, iv)
    data  = unpad(cipher.decrypt(data[bs:]))
    return (data)
 
if __name__ == '__main__':
    data = 'd437814d9185a290af20514d9341b710'
    password = '78f40f2c57eee727a4be179049cecf89' #16,24,32位长的密码
    encrypt_data = encrypt(data, password)
    encrypt_data = base64.b64encode(encrypt_data)
    print ('encrypt_data:', encrypt_data)
 
 
    encrypt_data = base64.b64decode(encrypt_data)
    decrypt_data = decrypt(encrypt_data, password)
    print ('decrypt_data:', decrypt_data)