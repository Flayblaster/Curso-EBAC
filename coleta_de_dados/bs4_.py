from bs4 import BeautifulSoup
import requests

resposta = requests.get("https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/")

sopa = BeautifulSoup(resposta.text, features='html.parser')

print(sopa.prettify()[:500])