from cryptography.fernet import Fernet
import os
import managment


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
    
generate_key_decision = input("Czy chcesz wygenerować nowy klucz? (tak/nie): ")
if generate_key_decision.lower() == 'tak':
    key = managment.generate_key()
else:
    key = managment.load_key()

# Użytkownik
print("1: Szyfrowanie pliku")
print("2: Rozszyfrowanie pliku")
choice = input("Wybierz opcje: ")

if choice == '1':
    encrypt(key)
elif choice == '2':
    decrypt(key)
else:
    print("Nie ma takiej opcji")