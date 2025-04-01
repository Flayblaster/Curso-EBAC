from bs4 import BeautifulSoup
import requests

url = "https://www.diariodigital.com.br/ultimas-noticias"
header = {"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}

request = requests.get(url, headers=header)
site = BeautifulSoup(request.text, "html.parser")

print(f'{"NOTÍCIAS DA CAPA":^100}')
tag_a_tit = site.find_all('a', class_='titulo')
tag_p_dat = site.find_all('p', class_='dataPub')

for titulo, data in zip(tag_a_tit, tag_p_dat):
    titulo = titulo.text.strip()
    data = data.text.strip()
    print(f"Título: {titulo} /// DATA: {data}")
    print('--'*50)
