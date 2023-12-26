from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def key_operations():
    print(request.form)
    print("Files data:", request.files)
    try:
        operation = request.form.get('operation')
        # Tworzenie pliku
        if operation == 'generate':
            length = request.form.get('length', default=16, type=int)
            key_path = request.form.get('key_path')

            # plik teksowy
            if not key_path.endswith('.txt'):
                key_path += '.txt'

            os.makedirs(os.path.dirname(key_path), exist_ok=True)

            key = os.urandom(length)
            with open(key_path, "wb") as key_file:
                key_file.write(key)

            return jsonify({"message": "Klucz został wygenerowany.", "key_path": key_path})
        # Wczytanie pliku
        elif operation == 'load':
            if 'file' not in request.files:
                return jsonify({"error": "Brak wymaganego pliku w zapytaniu"})

            key_file = request.files['file']
            if key_file.filename == '':
                return jsonify({"error": "Nie wybrano pliku"})

            key = key_file.read()  # Read key directly from the uploaded file
            return jsonify({"message": "Klucz został wczytany.", "key": key.hex()})

        else:
            return jsonify({"error": "Niepoprawna operacja."})

    except FileNotFoundError:
        return jsonify({"error": "Plik klucza nie istnieje."})
    except Exception as e:
        print("Error:", str(e))
    return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
