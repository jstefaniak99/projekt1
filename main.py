from cryptography.fernet import Fernet
import os


def encrypt(key):

    file_path = input("Proszę wprowadzić lokalizacje pliku zaszyfrowania: ")
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    print(f"Plik {file_path} zostal zaszyfrowany.")

def decrypt(key):

    file_path = input("Proszę wprowadzić lokalizacje pliku zaszyfrowania: ")
    f = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)
    print(f"Plik {file_path} zostal rozszyfrowany.")


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
    
generate_key_decision = input("Czy chcesz wygenerować nowy klucz? (tak/nie): ")
if generate_key_decision.lower() == 'tak':
    generate_key()

key = load_key()