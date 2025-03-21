import requests

respostas = requests.get("https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/historico/")

print(respostas.text[:600])