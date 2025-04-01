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

print(f'{"VÍDEOS TV MS RECORD":^100}')
tag_a_vid = site.find_all('a', class_="tit webkit-box-3 flex-grow-1 ms-1")
tag_a_dat = site.find_all('a', class_="d-block video-tag bg-light has-img has-horario")

for titulo_vid, data_vid in zip(tag_a_vid, tag_a_dat):
    titulo = titulo_vid.text.strip()
    data = data_vid.text.strip()
    print(f"Titulo do vídeo: {titulo} /// HORÁRIOS: {data}")
    print("--"*50)
