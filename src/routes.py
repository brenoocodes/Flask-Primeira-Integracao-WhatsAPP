import os
import json
from flask import jsonify, request, send_from_directory
from src.config import app, verify_token

# Define the directory to save the JSON files
SAVE_DIR = 'receber'
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'mensagem': 'API funcionando com sucesso'})

@app.route('/whatsapp', methods=['GET'])
def verify_token_whatsapp():
    try:
        if request.method == 'GET':
            token = request.args.get('hub.verify_token')
            challenge = request.args.get('hub.challenge')

            if challenge and token and token == verify_token:
                return challenge
            else:
                return jsonify({'EVENT_RECEIVED'}), 500
    except Exception as e:
        print(e)
        return jsonify({'EVENT_RECEIVED'}), 500

@app.route('/whatsapp', methods=['POST'])
def receber_mensagem():
    try:
        resposta = request.get_json()

        # Generate a file name
        file_list = os.listdir(SAVE_DIR)
        file_count = len(file_list)
        file_name = f"message_{file_count + 1}.json"

        # Save the JSON to a file
        file_path = os.path.join(SAVE_DIR, file_name)
        with open(file_path, 'w') as json_file:
            json.dump(resposta, json_file)

        return jsonify({'EVENT_RECEIVED': 'success'}), 200

    except Exception as e:
        print(e)
        return jsonify({'EVENT_RECEIVED': 'error'}), 500

@app.route('/json_files', methods=['GET'])
def list_json_files():
    try:
        file_list = os.listdir(SAVE_DIR)
        file_urls = [request.url_root + 'json_files/' + file_name for file_name in file_list]
        return jsonify({'files': file_urls}), 200
    except Exception as e:
        print(e)
        return jsonify({'EVENT_RECEIVED': 'error'}), 500

@app.route('/json_files/<filename>', methods=['GET'])
def get_json_file(filename):
    try:
        return send_from_directory(SAVE_DIR, filename)
    except Exception as e:
        print(e)
        return jsonify({'EVENT_RECEIVED': 'error'}), 500
