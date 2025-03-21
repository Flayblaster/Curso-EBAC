from bs4 import BeautifulSoup
import requests
import pandas as pd

resposta = requests.get("https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/")

sopa = BeautifulSoup(resposta.text, features='html.parser')

print(sopa.prettify()[:500])

url_tabela = pd.read_html('https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico')
print(url_tabela[0].head(10))