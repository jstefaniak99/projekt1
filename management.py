import os

def generate_key(length=16):  # długość klucza
    key = os.urandom(length)
    key_path = input("Proszę wprowadzić lokalizację zapisu klucza (np. H:\klucze): ")
    os.makedirs(os.path.dirname(key_path), exist_ok=True)
    with open(key_path, "wb") as key_file:  # Zapisz klucz jako plik binarny
        key_file.write(key)
    return key

def load_key():
    key_path = input("Proszę wprowadzić lokalizację wczytania klucza (np. H:\klucze): ")
    with open(key_path, "rb") as key_file:
        return key_file.read()