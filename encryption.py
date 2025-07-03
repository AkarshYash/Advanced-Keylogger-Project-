from cryptography.fernet import Fernet
import base64
import os

class DataEncryptor:
    def __init__(self):
        # In production, this would be securely loaded from config
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        
    def encrypt(self, data):
        if isinstance(data, str):
            data = data.encode()
        return self.cipher.encrypt(data)
        
    def decrypt(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data)
