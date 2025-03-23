import requests
import json

def enviar_arquivo():
    #Caminho do aqruivo para upload
    caminho = "C:/Users/david/Downloads/produtos_informatica.xlsx"

    #Enviar arquivo
    requisicao = requests.post('https://www.file.io', files={'file': open(caminho, 'rb')}) #post envia, rb é a criptografia do arq, no caso esta em binário
    conteudo = requisicao.text
    saida_de_requisicao = requisicao.json()

    print(saida_de_requisicao)
    url = saida_de_requisicao['link']
    print('Arquivo enviado. link para acesso:', url)
    
enviar_arquivo()