from src.config import app
from flask import jsonify

@app.route('/', methods=['GET'])
def home():
    return jsonify({'mensagem': 'API funcionando com sucesso'})

@app.route('/whatsapp', methods=['GET'])
def get_whatsapp():
    return jsonify({'mensagem': 'usando o get do /whatsapp'})

@app.route('/whatsapp', methods=['POST'])
def post_whatsapp():
    return jsonify({'mensagem': 'usando o post do /whatsapp'})