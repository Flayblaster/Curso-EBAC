from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes"
header = {"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}

request = requests.get(url, headers=header)
site = BeautifulSoup(request, "html.parser")

tabela = site.find_all('tr', class_="fundoPadraoBClaro2")
print(tabela.text.strip())