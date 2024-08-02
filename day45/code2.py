import requests
from bs4 import BeautifulSoup

URL = 'https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

movies_list = soup.find_all(name='h3', class_="listicleItem_listicle-item__title__BfenH")

movies = [movie.getText() for movie in movies_list]
movies = movies[::-1]
movies_data = '\n'.join(movies)
print(movies_data)

# print(movies)

with open('movies.txt', mode='w') as file:
    file.write(movies_data)


