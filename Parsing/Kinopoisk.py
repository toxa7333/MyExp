import requests
from bs4 import BeautifulSoup


user_id = 1464337
page = 1
result = []

with open('test.html', 'w') as output_file:
    while page < 7:
        url = 'http://www.kinopoisk.ru/user/1464337/votes/list/ord/date/page/%d/#list' % (user_id, page)
        r = requests.get(url)

        soup = BeautifulSoup(r.text)

        film_list = soup.find('div', {'class': 'profileFilmsList'})
        items = film_list.find_all('div', {'class': ['item', 'item even']})

        for item in items:
            movie_link = item.find('div', {'class': 'nameRus'}).find('a').get('href')
            movie_name = item.find('div', {'class': 'nameRus'}).find('a').text

            result.append([
                movie_link, movie_name
            ])

        page += 1


#with open('test.html') as input_file:
#    text = input_file.read()




for item in result:
    print ("%s - %s" % (item[0], item[1]))

