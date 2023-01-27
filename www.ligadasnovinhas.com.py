from bs4 import BeautifulSoup
import requests

# Fazer uma solicitação à página da web
url = 'https://www.ligadasnovinhas.com/fotos-de-buceta-rosinha-da-gordinha-gostosa/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Encontre a div com a classe "post-texto"
div = soup.find('div', class_='post-texto')

# Imprima todo o conteúdo dentro da div
print(div.prettify())
