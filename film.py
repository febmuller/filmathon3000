import requests
from bs4 import BeautifulSoup
import random

from flask import Flask
app = Flask(__name__)

def rando_calrissian(genre):
    page = requests.get('https://www.imdb.com/search/title/?genres={}'.format(genre.lower()))
    soup = BeautifulSoup(page.text, 'html.parser')

    film_list = (soup.find_all('div', class_='lister-item-content'))
    film_content = random.choice(film_list)
    film_header = film_content.find('h3', class_='lister-item-header')
    film_name = film_header.find('a').text
    film_url = film_header.find('a')['href']
    film_genres = film_content.find('span', class_="genre").text

    return """
    {} 
    <br />
    {}
    <br />
    <a href ='https://www.imdb.com/{}'>Link to IMDB</a>
    """.format(film_name, film_genres, film_url)  

    #print('\n\nYour search for {}:'.format(genre))
    #print(film_name)
    #print('https://www.imdb.com{}'.format(film_url))
    #print(film_genres)


@app.route('/')
def get_film():
    genre = 'comedy'
    return rando_calrissian(genre)


if __name__ == '__main__':
    print("This will print a random film based on your input.")
    genre = (input("Enter a genre of film: "))
    print(rando_calrissian(genre))
