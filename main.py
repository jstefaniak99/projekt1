import os
import management

def xor_encrypt_decrypt(data, key):
    encrypted_data = bytearray()
    for i in range(len(data)):
        data_byte = data[i]
        key_byte = key[i % len(key)]
        encrypted_data.append(data_byte ^ key_byte)
    return bytes(encrypted_data)

def encrypt_decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    processed_data = xor_encrypt_decrypt(data, key)

    with open(file_path, 'wb') as file:
        file.write(processed_data)

generate_key_decision = input("Czy chcesz wygenerować nowy klucz? (tak/nie): ")
if generate_key_decision.lower() == 'tak':
    key = management.generate_key()
else:
    key = management.load_key()

# Interfejs użytkownika
print("1: Szyfrowanie pliku")
print("2: Rozszyfrowanie pliku")
choice = input("Wybierz opcje (1/2): ")

if choice not in ['1', '2']:
    print("Nieprawidłowy wybór. Proszę wybrać 1 lub 2.")
else:
    file_path = input("Proszę wprowadzić lokalizację pliku: ")
    try:
        if os.path.exists(file_path):
            encrypt_decrypt_file(file_path, key)
        else:
            print("Plik nie istnieje.")
    except IOError as e:
        print(f"Wystąpił błąd podczas dostępu do pliku: {e}")
  