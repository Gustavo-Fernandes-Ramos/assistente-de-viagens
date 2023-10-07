import requests

# Defina a URL do servidor FastAPI
url = 'http://localhost:8000/auth/create-auth'  # Substitua pela URL real do servidor

# Dados a serem enviados no corpo da requisição (pode ser um dicionário ou outra estrutura de dados)
dados = {'id': '123', 'login': 'login123', 'pwd': 'senha123'}

# Envie a requisição POST
response = requests.post(url, json=dados)

# Verifique a resposta do servidor
if response.status_code == 200:
    print('Requisição POST bem-sucedida!')
    print('Resposta do servidor:', response.json())
else:
    print('Erro na requisição POST. Código de status:', response.status_code)
    print('Resposta do servidor:', response.text)

'''
url = 'http://localhost:8000/auth/authenticate'

response = requests.post(url, json=response.json())

if response.status_code == 200:
    print('Requisição POST bem-sucedida!')
    print('Resposta do servidor:', response.json())
else:
    print('Erro na requisição POST. Código de status:', response.status_code)
    print('Resposta do servidor:', response.text)
'''