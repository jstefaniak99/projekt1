import os
import io
from flask import Flask, render_template, request, send_file, jsonify

app = Flask(__name__)


#Funkcja do wykonania operacji XOR na danych przy użyciu klucza
def xor_operation(data, key):
    result_data = bytearray()
    for i in range(len(data)):
        data_byte = data[i]
        key_byte = key[i % len(key)]
        result_data.append(data_byte ^ key_byte)
    return bytes(result_data)

# Wszystko wykonywane w domyślej ścieżce
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        operation = request.form.get('operation')

        if operation == 'generate':
            key_string = request.form.get('key_string')
            if not key_string:
                return jsonify({"error": "Wymagany jest ciąg klucza"}), 400

            key_path = request.form.get('key_path', 'klucz.txt')
            if not key_path.endswith('.txt'):
                key_path += '.txt'

            # Zapisz plik jako
            with open(key_path, "w") as key_file:
                key_file.write(key_string)

            return jsonify({"message": "Klucz wygenerowany", "key_path": key_path})

        elif operation == 'load':
            return load_key_file()

        elif operation in ['encrypt', 'decrypt']:
            key_file = request.files.get('key_file')
            if not key_file:
                return jsonify({"error": "Wymagany jest klucz"}), 400

            key = key_file.read()
            file = request.files.get('file')
            if not file:
                return jsonify({"error": "Wymagany jest plik"}), 400

            file_data = file.read()
            processed_data = xor_operation(file_data, key)

            filename = 'Zaszyfrowany.txt' if operation == 'encrypt' else 'Odszyfrowany.txt'
            return send_file(io.BytesIO(processed_data), download_name=filename, as_attachment=True)

        else:
            return jsonify({"error": "Nieprawidłowa operacja!"}), 400

    return render_template('index.html')

def load_key_file():
    try:
        if 'key_file' not in request.files:
            return jsonify({"error": "Wymagany jest klucz"}), 400

        key_file = request.files['key_file']
        if key_file.filename == '':
            return jsonify({"error": "Wymagany jest plik"}), 400

        key = key_file.read()
        return jsonify({"message": "Wymagany jest klucz", "key": key.hex()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
