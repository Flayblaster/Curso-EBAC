import requests
from bs4 import BeautifulSoup

"""
hearders é uma forma de indicar ao site quem está acessando ele, se voce deixar no padrão, 
o site mostrará sua versão de python mas já se você indicar um motor específico, ele mostra
outras versões que podem te trazer mais vantagens
"""
headers = {"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}

request = requests.get("https://g1.globo.com", headers=headers) 
soup = BeautifulSoup(request.text, 'html.parser') 
#html.parser signifaca 'leitor de html'. O bs4 é um organizador de html
#print(request) Se a requisicao deu certo o site retorna o código 200
#print(soup.prettify()) os parenteses significa que é uma função 

print(soup.title,'\n') #uma das várias funções do bs4

titulo = soup.find('title') #find mostra o primeiro que ele achar
print(f'titulo: {titulo}\n')

"""
As funções de procurar itens, podem ter um parâmetro que indica o nome daquela tag, podendo ser usado: class_, name e id
"""

h2 = soup.find('span', class_="bstn-hl-title gui-color-primary gui-color-hover gui-color-primary-bg-after") 
print(f'titulo h2: {h2}\n')
