from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()

verify_token = os.getenv("verifytoken")
token = os.getenv("token")
base_url = os.getenv("base_url")
version_api = os.getenv("version_api")
phone_id = os.getenv("phone_id")

link_mensagens = f'{base_url}/{version_api}/{phone_id}/messages'

app = Flask(__name__)