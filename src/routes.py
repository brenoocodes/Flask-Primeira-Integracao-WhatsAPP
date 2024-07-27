from src.config import app, verify_token
from flask import jsonify, request

@app.route('/', methods=['GET'])
def home():
    return jsonify({'mensagem': 'API funcionando com sucesso'})

@app.route('/whatsapp', methods=['GET', 'POST'])
def get_whatsapp():
    try:
        if request.method == 'GET':
            print('Método GET')
            token = request.args.get('hub.verify_token')
            challenge = request.args.get('hub.challenge')

            if challenge and token and token == verify_token:
                return challenge
            else:
                return jsonify({'mensagem': 'erro interno'}), 500
        
        elif request.method == 'POST':
            received = request.get_json()
            print('Método POST')
            token = received['hub.verify_token']
            challenge = received['hub.challenge']

            if challenge and token and token == verify_token:
                return challenge
            else:
                return jsonify({'mensagem': 'erro interno'}), 500

    except Exception as e:
        print(e)
        return jsonify({'mensagem': 'erro interno'}), 500
