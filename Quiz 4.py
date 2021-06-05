import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

p = {'page': 1}
file = open('movies.csv', 'w', newline='\n')
file_csv = csv.writer(file)
file_csv.writerow(['Title', 'Imdb', 'Release_year'])
url = 'https://movie.ge/filter-movies?search=&type=movie&genres%5B%5D=16'

while p['page'] < 6:
    r = requests.get(url, params=p)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    info = soup.find("div", {'class': 'mlist section'})
    all_movies = info.find_all('div', {'class': 'col-md-3'})
    for each in all_movies:
        t_card = each.find('div', {'class': 'popular-card__title'})
        i_card = each.find('div', {'class': 'imdb'})
        y_card = each.find('div', {'class': 'year'})
        title = t_card.h2.a.span.text
        imdb = i_card.span.text
        rel_year = y_card.text
        rel_year = rel_year.replace('წ', '')
        file_csv.writerow([title, imdb, rel_year])

    p['page'] += 1
    sleep(randint(15, 20))


file.close()