import os
import io
from flask import Flask, render_template, request, send_file, jsonify

app = Flask(__name__)

def xor_encrypt_decrypt(data, key):
    key_bytes = key.encode()
    encrypted_data = bytearray()
    for i in range(len(data)):
        data_byte = data[i]
        key_byte = key_bytes[i % len(key_bytes)]
        encrypted_data.append(data_byte ^ key_byte)
    return bytes(encrypted_data)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("Form data:", request.form)    # Debugowanie
        print("Files data:", request.files)  
        
        key_path = request.form.get('key_path')
        file = request.files.get('file')
        file = request.files['file'].filename
        print(key_path, file)

        if not key_path or not file:
            return "Klucz jest wymagany", 400
        
        try:
            with open(key_path, 'rb') as key_file:
                key_data = key_file.read()
        except IOError:
            return "Nie można odczytać klucza", 400
        
        operation = request.form.get('operation')

        if 'file' not in request.files or request.files['file'].filename == '':
            return "Plik jest wymagany", 400

        uploaded_file = request.files['file']

        try:
            if operation == 'encrypt':
                processed_data = xor_encrypt_decrypt(uploaded_file.read(), file)
                filename = 'encrypted_file'
            elif operation == 'decrypt':
                processed_data = xor_encrypt_decrypt(uploaded_file.read(), file)
                filename = 'decrypted_file'
            else:
                return "Niepoprawna operacja", 400

            return send_file(
                io.BytesIO(processed_data),
                download_name=file,
                as_attachment=True
            )
        except Exception as e:
            print("Błąd:", str(e))  # Debugowanie
            return jsonify({"error": str(e)}), 500

    return render_template('index.html')

if __name__ == '__main__':
     app.run(debug=True)
