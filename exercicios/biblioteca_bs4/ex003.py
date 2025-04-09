from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://news.ycombinator.com/"
header = {"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}

request = requests.get(url, headers=header)
site = BeautifulSoup(request.text, "html.parser")

link_ext = site.find_all('a')
for link_ext in link_ext:
    if 'ycombinator' not in link_ext['href'] and 'http' in link_ext['href']:
        print(f'link externo: {link_ext['href']}')
link_ext = site.find_all('a')
for link in link_ext:
    if 'ycombinator' in link['href']:
        print(f'link interno: {link['href']}')