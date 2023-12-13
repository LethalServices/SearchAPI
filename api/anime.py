import requests
from bs4 import BeautifulSoup
from api.proxy import Random_Proxy

def getAnime(host, query, page, proxie):
    moviesDictionary = {'Results': []}
    proxy = Random_Proxy()
    try:
        base_url = f'https://{host}/filter?keyword={query}'

        if page != None:
            base_url = f'https://{host}/filter?keyword={query}&page={page}'

        if proxie == 'true':
            currentPage = page or '1'
            r = proxy.Proxy_Request(url=base_url, request_type='get')
            soup = BeautifulSoup(r.content, 'lxml')
        else:
            currentPage = page or '1'
            soup = BeautifulSoup(requests.get(base_url).content, 'lxml')
            
    except requests.exceptions.RequestException as e:
        moviesDictionary['Status'] = False,
        moviesDictionary['error'] = str(e),
        return moviesDictionary

    moviesDictionary['Current_Page'] = currentPage
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
        moviesDictionary['Last_Page'] = getPages(soup, query)
        moviesDictionary['Results'].append(moviesObject)
   
    return moviesDictionary

def getPages(soup, query):
    try:
        ul = soup.find('ul', class_='pagination')
        li = ul.find_all('li')
    except:
        pages = '1'
        return pages

    for l in li:
        a = l.find('a', text='»')
    if a != None:
        href = a['href']
        hrefSplit = href.split('page=')
        pages = hrefSplit[1]
        return pages