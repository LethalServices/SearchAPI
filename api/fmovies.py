import requests
from bs4 import BeautifulSoup
from api.proxy import Random_Proxy

def getMovies(host, query, page, proxie):
    moviesDictionary = {'Status': True,'Query': query,'Results': []}
    proxy = Random_Proxy()
    try:
        if proxie == 'true':
            if page != None:
                base_url = f'https://{host}/filter?keyword={query}&page={page}'
                currentPage = page
                r = proxy.Proxy_Request(url=base_url, request_type='get')
                soup = BeautifulSoup(r.content, 'lxml')
            else:
                base_url = f'https://{host}/filter?keyword={query}'
                currentPage = '1'
                r = proxy.Proxy_Request(url=base_url, request_type='get')
                soup = BeautifulSoup(r.content, 'lxml')
        else:
            if page != None:
                base_url = f'https://{host}/filter?keyword={query}&page={page}'
                currentPage = page
                soup = BeautifulSoup(requests.get(base_url).content, 'lxml')
            else:
                base_url = f'https://{host}/filter?keyword={query}'
                currentPage = '1'
                soup = BeautifulSoup(requests.get(base_url).content, 'lxml')
    except requests.exceptions.RequestException as e:
        moviesDictionary['Status'] = False,
        moviesDictionary['error'] = str(e),
        return moviesDictionary

    moviesDictionary['Page'] = currentPage
    items = soup.find_all('div', class_='item')

    for item in items:
        try:
            a = item.find('a')
            href = a.get('href')
            link = f'https://{host}{href}'
            quality = item.find('div', class_="quality").text
            img = item.find('img')
            poster = img['data-src']
            Info = item.find('div', class_="meta").text
            movieinfo = Info.split(' ')
            year =  movieinfo[2]
            ctype = movieinfo[3].replace('SS', 'TV SHOW')
            duration =  f'{movieinfo[4]} {movieinfo[5]}'
            title =  ' '.join(movieinfo[7:])
        except Exception as e:
            link = str(e) 
            quality = str(e)
            poster = str(e)
            Info = str(e)
            
        moviesObject = {'Title': title,'link': link,'Quality': quality, 'Duration': duration,'Cover': poster,'Year': year, 'Content-Type': ctype}
        moviesDictionary['Results'].append(moviesObject)
   
    return moviesDictionary
