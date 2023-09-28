import requests
from bs4 import BeautifulSoup

# URL da página web que você deseja raspar
url = "https://embedder.net/lib/movies"

# Faz uma requisição GET para a página web
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parseia o conteúdo HTML da página usando o Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontra todos os elementos <div> com a classe "film-poster"
    film_posters = soup.find_all('div', class_='film-poster')
    
    # Loop pelos elementos e reformatá-los
    for film_poster in film_posters:
        img_tag = film_poster.find('img', class_='film-poster-img')
        title = film_poster.find('a', class_='bop-name').text.strip()
        img_url = img_tag['data-src']

        # Imprime o resultado formatado
        print(f'<div class="col mt-3">\n'
              '<!-- start media-box -->\n'
              f'<div class="media-box">\n'
              f'<a onclick="openMovie(\'{title}\', \'https://embedder.net/e/movie?imdb={title}\')" class="full-click"></a>\n'
              f'<div class="media-thumb" style="background-image: url({img_url});"></div>\n'
              f'<a onclick="openMovie(\'{title}\', \'https://embedder.net/e/movie?imdb={title}\')" class="media-play"><i class="icofont-ui-play"></i></a>\n'
              '<!-- Start rate-quality-info -->\n'
              f'<div class="media-info">\n'
              f'<h5 class="media-box-title">{title}</h5>\n'
              '</div>\n'
              '<!-- end media-box -->\n'
              '</div>\n'
              '</div>\n')
else:
    print("Erro ao acessar a página")

