from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
import base64
import json

# A function to pad the message to be encrypted
def pad(s):
    return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

# A function to encrypt a message using AES
def encrypt(message, password):
    salt = get_random_bytes(16)  # Generates a random salt
    key = scrypt(password, salt, key_len=32, N=2**20, r=8, p=1)  # Derives a key from the password
    iv = get_random_bytes(AES.block_size)  # Initialization vector for encryption
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(message)
    encrypted = cipher.encrypt(padded_message.encode())
    return base64.b64encode(iv + salt + encrypted).decode('utf-8')

# Function to store and return encrypted credentials
def store_credentials():
    username = input("Enter your username: ") #  hulk smash
    password = input("Enter your password: ") # Hulk123456
    encrypted_username = encrypt(username, password)
    encrypted_password = encrypt(password, password)  # Encrypt the password with itself
    return {'encrypted_username': encrypted_username, 'encrypted_password': encrypted_password}



