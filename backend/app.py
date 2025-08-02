from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import sqlite3
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/documents/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    filesize = os.path.getsize(filepath)

    conn = get_db_connection()
    conn.execute('INSERT INTO documents (filename, filepath, filesize) VALUES (?, ?, ?)', (filename, filepath, filesize))
    conn.commit()
    conn.close()

    return jsonify({'message': 'File uploaded successfully'}), 201

@app.route('/documents', methods=['GET'])
def list_documents():
    conn = get_db_connection()
    documents = conn.execute('SELECT * FROM documents').fetchall()
    conn.close()
    return jsonify([dict(doc) for doc in documents])

@app.route('/documents/<int:doc_id>', methods=['GET'])
def get_document(doc_id):
    conn = get_db_connection()
    doc = conn.execute('SELECT * FROM documents WHERE id = ?', (doc_id,)).fetchone()
    conn.close()
    
    if doc is None:
        return jsonify({'error': 'Document not found'}), 404

    return send_from_directory(app.config['UPLOAD_FOLDER'], doc['filename'])

@app.route('/documents/<int:doc_id>', methods=['DELETE'])
def delete_document(doc_id):
    conn = get_db_connection()
    doc = conn.execute('SELECT * FROM documents WHERE id = ?', (doc_id,)).fetchone()

    if doc is None:
        conn.close()
        return jsonify({'error': 'Document not found'}), 404

    os.remove(doc['filepath'])
    conn.execute('DELETE FROM documents WHERE id = ?', (doc_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Document deleted successfully'})

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return "Welcome to the Flask backend! Use the API endpoints for document operations."

if __name__ == '__main__':
    app.run(debug=True)