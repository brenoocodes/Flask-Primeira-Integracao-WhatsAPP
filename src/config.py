from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()

verify_token = os.getenv("verifytoken")

app = Flask(__name__)