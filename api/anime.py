import requests
from bs4 import BeautifulSoup
from api.proxy import Random_Proxy

def getAnime(host, query, page, proxie):
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
            Title = item.find('a', class_="name d-title").text
            img = item.find('img')
            poster = img['src']
            Type = item.find('div', class_="right").text
        except Exception as e:
            link = str(e) 
            poster = str(e)
            Title = str(e)
            Type = str(e)
            
        moviesObject = {'link': link, 'Cover': poster, 'Title': Title, 'Content-Type': Type} 
        moviesDictionary['Results'].append(moviesObject)
   
    return moviesDictionary

 #'Quality': quality, 'Duration': duration,'Cover': poster,'Year': year, 'Content-Type': ctype}