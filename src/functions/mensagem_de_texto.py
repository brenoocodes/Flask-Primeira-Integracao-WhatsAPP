import sys
from pathlib import Path
file = Path(__file__).resolve()
parent = file.parent.parent.parent
sys.path.append(str(parent))

from src.config import link_mensagens, token
import requests
import json

def mensagem_texto(numero, mensagem_texto):
    mensagem = {
            #formato exigido pela api oficial
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": numero,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": mensagem_texto
            }
        }
    enviar = requests.post(url=link_mensagens, data=json.dumps(mensagem), headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    })
    return enviar

enviando = mensagem_texto(numero='5535991319069', mensagem_texto='Enviando mensagem de texto usando a api oficial do whatsapp')
print(enviando.json())
