import random
import string
from operator import index
from struct import pack_into

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#Encryption
plain_text = input("Enter a message to encryption:")
cipher_text = ""

for letter in plain_text:
       index = chars.index(letter)
       cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")


#Decryption
cipher_text = input("Enter a message to Decryption:")
plain_text = ""

for letter in cipher_text:
       index = key.index(letter)
       plain_text += chars[index]

print(f"original message: {cipher_text}")
print(f"Decrypted message: {plain_text}")

