import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# URL do site principal
url = "https://www.djnetodeananindeua.com.br/"

# Armazena os links de download de todos os subdomínios
download_links = []

# Função para obter todos os links de download de um URL
def get_download_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # Encontra todos os links <a> no HTML
    links = soup.find_all("a")
    for link in links:
        # Verifica se o link começa com "https://cloudup.com/files"
        href = link.get("href")
        if href and href.startswith("https://cloudup.com/files"):
            download_links.append(href)

# Função recursiva para buscar em todos os subdomínios
def search_subdomains(url):
    # Obtém o nome do domínio e o caminho da URL
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path
    # Faz a solicitação HTTP para a URL atual
    response = requests.get(url)
    # Verifica se a resposta foi bem sucedida
    if response.status_code == 200:
        # Analisa o HTML para encontrar links de download
        get_download_links(url)
        # Encontra todos os links <a> no HTML
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all("a")
        # Percorre todos os links <a> e verifica se é um subdomínio
        for link in links:
            href = link.get("href")
            if href and href.startswith("http") and domain in href and href != url:
                # Faz uma chamada recursiva para buscar em todos os subdomínios
                search_subdomains(href)

# Chama a função de busca em todos os subdomínios
search_subdomains(url)

# Baixa os arquivos de download encontrados
for i, link in enumerate(download_links):
    # Define o caminho do arquivo local onde o download será salvo
    file_name = os.path.basename(link)
    if not file_name.endswith('.mp3'):
        file_name += '.mp3'
    file_path = os.path.join("downloads", file_name)
    # Faz o download do arquivo e salva no arquivo local
    response = requests.get(link, stream=True)
    with open(file_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print(f"[{i+1}/{len(download_links)}] Download completo: {file_name}")

