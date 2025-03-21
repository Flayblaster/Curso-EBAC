import requests
from bs4 import BeautifulSoup

#https://www.casadocodigo.com.br/collections/livros-de-programacao

url = "https://www.casadocodigo.com.br/collections/livros-de-programacao"
requisicao = requests.get(url)
conteudo = BeautifulSoup(requisicao.text, features='html.parser')

for item in conteudo.find_all('a'):
    titulo = item.text.strip()
    print('Titulo: ', titulo)
