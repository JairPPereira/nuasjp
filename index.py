import requests
from bs4 import BeautifulSoup

# Fazer uma solicitação GET para o seu site
response = requests.get("https://jpp-ap.onrender.com/")
html_content = response.text

# Criar um objeto BeautifulSoup para analisar o HTML
soup = BeautifulSoup(html_content, "html.parser")

# Encontrar todos os elementos <img> dentro de um <div class="col-sm-2 col-xs-4">
div_elements = soup.find_all("div", class_="col-sm-2 col-xs-4")
for div in div_elements:
    img_elements = div.find_all("img")
    for img in img_elements:
        # Imprimir o atributo "src" da imagem, que contém o link para a imagem
        print(img["src"])

# Encontrar todos os elementos <a> dentro de um <div class="col-sm-2 col-xs-4">
div_elements = soup.find_all("div", class_="col-sm-2 col-xs-4")
for div in div_elements:
    a_elements = div.find_all("a")
