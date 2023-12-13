import requests
from bs4 import BeautifulSoup
from api.proxy import Random_Proxy

def getMovies(host, query, page, proxie):
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
            quality = item.find('div', class_="quality").text
            pclass = item.find('div', class_='poster')
            href = pclass.find('a').get('href')
            link = f'https://{host}{href}'       
            img = item.find('img')
            poster = img['data-src']
            meta = item.find('div', class_="meta")
            Title = meta.find('a').text
            Type = item.find('span', class_="type").text
        except Exception:
            link = str(e) 
       
        moviesObject = {'link': link, "Title": Title, 'Quality': quality, 'Cover': poster, "Content-Type": Type} 
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
