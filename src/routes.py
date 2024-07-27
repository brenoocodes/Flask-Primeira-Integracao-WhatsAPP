from flask import jsonify, request, send_from_directory, abort
from src.config import app, verify_token

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

respostas_api = []

@app.route('/whatsapp', methods=['POST'])
def receber_mensagem():
    try:
        resposta = request.get_json()   
        respostas_api.append(resposta)
        return jsonify({'EVENT_RECEIVED': 'success'}), 200

    except Exception as e:
        print(e)
        return jsonify({'EVENT_RECEIVED': 'error'}), 500


@app.route('/resposta', methods=['GET'])
def pegar_resposta():
    return jsonify(respostas_api)
