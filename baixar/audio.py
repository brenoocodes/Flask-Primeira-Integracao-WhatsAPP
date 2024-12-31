import requests
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("token")

url = 'https://lookaside.fbsbx.com/whatsapp_business/attachments/?mid=1437882233585973&ext=1722187591&hash=ATuKRtd1VgVGtMmPsVDBLKQ0WEhqmHAoqSrwoyybSz8tLA'
headers = {
    f'Authorization': 'Bearer EAAz0WkTZCT5ABOZBJQUrdkBPE2CSirCfqqfH777eyFIZBtTsGek5mDURa5kOESWnoOw3FBfnsSRaBszTJla6gLAhJjtUTyLjyDTLC8UyDnCgJri9yWacFG54II3RHXYbzq2VXoTnUKjZC9C2tKePYSyfZB7yRlJpHqRr3HyBIiSGgvDPjRLcCHkJtzaDEvKIi3CU1yVOZAXh8hhsAoZBbrCzLoAUUAqpdoNp09Dq1sKmWQtvtciL2H3'
}

response = requests.get(url, headers=headers)
print(response)
# Salvar a resposta em um arquivo
with open('media_file.pdf', 'wb') as file:
    file.write(response.content)
