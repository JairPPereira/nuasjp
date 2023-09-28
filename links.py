import requests
from bs4 import BeautifulSoup

url = "https://embedder.net/lib/movies?&sort_by=imdb_rate"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movies = soup.find_all("div", class_="d-block")

for movie in movies:
    link_element = movie.find("a", class_="bop-name")
    if link_element is not None:
        link = link_element.get("href")
        name = link_element.text.strip()
        print(f'<button onclick="openMovie(\'{name}\', \'{link}\')">{name}</button>')
