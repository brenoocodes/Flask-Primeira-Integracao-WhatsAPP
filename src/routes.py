from src.config import app, verify_token
from flask import jsonify, request

@app.route('/', methods=['GET'])
def home():
    return jsonify({'mensagem': 'API funcionando com sucesso'})

@app.route('/whatsapp', methods=['POST'])
def get_whatsapp():
    try:
        received = request.get_json()
        token = received['hub.verify_token']
        challange = received['hub.challange']

        if challange and token and token == verify_token:
            return challange
        else:
            return jsonify({'mensagem': 'erro interno'}), 500

    except Exception as e:
        print(e)
        return jsonify({'mensagem': 'erro interno'}), 500
