from bs4 import BeautifulSoup
import requests
#BeautifulSoup é uma classe e bs4 é o mudulo ou biblioteca

resposta = requests.get("https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/")

sopa = BeautifulSoup(resposta.text, features='html.parser') #classes tem propriedades, a propriedade PARSE, indica que o conteúdo do site será analizado na indentação do HTML.

print(sopa.prettify()[:500])