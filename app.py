from flask import Flask, request, jsonify, send_file
import pandas as pd
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploaded_files'
CONVERTED_FOLDER = 'converted_files'

# Ensure directories exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(CONVERTED_FOLDER):
    os.makedirs(CONVERTED_FOLDER)

@app.route('/convert', methods=['POST'])
def convert_xls_to_xlsx():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not file.filename.endswith('.xls'):
        return jsonify({"error": "File must be .xls format"}), 400

    try:
        # Save the uploaded file
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Convert the file to .xlsx
        df = pd.read_excel(file_path)
        output_file = os.path.join(CONVERTED_FOLDER, f"{os.path.splitext(file.filename)[0]}.xlsx")
        df.to_excel(output_file, index=False)

        # Send the converted file as response
        return send_file(output_file, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5950)
