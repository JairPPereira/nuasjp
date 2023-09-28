import requests
from bs4 import BeautifulSoup

url = "https://embedder.net/lib/movies?page=7"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

for film_poster in soup.find_all("div", class_="film-poster"):
    img = film_poster.find("img")
    title = img["alt"]
    image_url = img["data-src"]
    link = film_poster.find("a", class_="film-poster-ahref")["href"]

    print('<div class="col-sm-2 col-xs-4"><div class="media-box">')
    print(f'   <img src="{image_url}" style="max-height: 250px; min-height: 190px;" class="m-t-10 b-radius-5 img-responsive center-block" alt="{title}" /><center>')
    print(f'   <button class="btn btn-primary" onclick="openMovie(\'{title}\', \'{link}\')">Assistir</button></center>')
    print('</div></div>')



