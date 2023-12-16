from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    key_path = input("Proszę wprowadzić lokalizacje zapisu klucza (wraz z nazwą klucza np. klucz_bezpieczenstwa.key)") 

    os.makedirs(os.path.dirname(key_path), exist_ok=True)

    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    key_path = input("Proszę wprowadzić lokalizacje wczytania klucza (wraz z nazwą klucza np. klucz_bezpieczenstwa.key)")
    with open(key_path, "rb") as key_file:
        return key_file.read()