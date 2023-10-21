import requests
from bs4 import BeautifulSoup
from api.proxy import Random_Proxy
from colorama import Fore

def getMovies(host, query, page, proxie):
    moviesDictionary = {'Results': []}
    proxy = Random_Proxy()
    try:
        if proxie == 'true':
            if page != None:
                base_url = f'https://{host}/search/{query}?page={page}'
                currentPage = page
                r = proxy.Proxy_Request(url=base_url, request_type='get')
                soup = BeautifulSoup(r.content, 'lxml')
            else:
                base_url = f'https://{host}/search/{query}'
                currentPage = '1'
                r = proxy.Proxy_Request(url=base_url, request_type='get')
                soup = BeautifulSoup(r.content, 'lxml')
        else:
            if page != None:
                base_url = f'https://{host}/search/{query}?	={page}'
                currentPage = page
                soup = BeautifulSoup(requests.get(base_url).content, 'lxml')
            else:
                base_url = f'https://{host}/search/{query}'
                currentPage = '1'
                soup = BeautifulSoup(requests.get(base_url).content, 'lxml')
            
    except requests.exceptions.RequestException as e:
        moviesDictionary['Status'] = False,
        moviesDictionary['error'] = str(e),
        return moviesDictionary

    moviesDictionary['Current_Page'] = currentPage 
    items = soup.find_all('div', class_='flw-item')

    for item in items:
        try:
            info = item.find('div', 'film-poster')
            a = info.find('a')
            href = a.get('href')
            link = f'https://{host}{href}'
            quality = item.find('div', class_="pick film-poster-quality").text
            
            img = info.find('img')
            poster = img['data-src']
            TitleBR = item.find('h2', class_="film-name").text
            Title = TitleBR.replace('\n', '')
       
            year =  item.find('span', class_="fdi-item").text
            duration = item.find('span', class_="fdi-item fdi-duration").text
            ctype = item.find('span', class_="float-right fdi-type").text
            
        except Exception:
            pass 
       
        moviesObject = {'Quality': quality, 'link': link, 'Cover': poster, 'Title': Title, 'Year': year, 'Duration': duration, 'Type': ctype}#,'Quality': quality, 'Duration': duration,'Cover': poster,'Year': year, 'Content-Type': ctype} #, 'Last_Page':last_page[1]}
        moviesDictionary['Last_Page'] = getPages(soup, query)
        moviesDictionary['Results'].append(moviesObject)
   
    return moviesDictionary

def getPages(soup, query):
    try:
        ul = soup.find('ul', class_='pagination pagination-lg justify-content-center')
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
