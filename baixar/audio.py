import requests

# URL da imagem
url = "https://lookaside.fbsbx.com/whatsapp_business/attachments/?mid=335122459668803&ext=1722115948&hash=ATuRWe9vKC-eeFPwHIK1mXSBePtaS_lbg0sBlWbGmKjCIw"

# Nome do arquivo para salvar
filename = "imagem.jpg"

# Fazendo o download da imagem
response = requests.get(url)

# Verificando se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Salvando a imagem no disco
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Imagem salva como {filename}")
else:
    print("Falha ao baixar a imagem:", response.status_code)
