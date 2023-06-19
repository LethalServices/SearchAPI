import requests
from bs4 import BeautifulSoup
from api.proxy import Random_Proxy

'''
Credits: Joshua .
URL: https://lethals.org.
Copyright\Trademark: © 2022 - 2023 Lethal Services ™ ​| All rights reserved.
'''

def getAnihdPlay(host, query, page, proxie):
    moviesDictionary = {'Status': True,'Query': query,'Results': []}
    proxy = Random_Proxy()
    try:
        if proxie == 'true':
            if page != None:
                base_url = f'https://{host}/search.html?keyword={query}&page={page}'
                currentPage = page
                r = proxy.Proxy_Request(url=base_url, request_type='get')
                soup = BeautifulSoup(r.content, 'lxml')
            else:
                base_url = f'https://{host}/search.html?keyword={query}'
                currentPage = '1'
                r = proxy.Proxy_Request(url=base_url, request_type='get')
                soup = BeautifulSoup(r.content, 'lxml')
        else:
            if page != None:
                base_url = f'https://{host}/search.html?keyword={query}&page={page}'
                currentPage = page
                soup = BeautifulSoup(requests.get(base_url).content, 'lxml')
            else:
                base_url = f'https://{host}/search.html?keyword={query}'
                currentPage = '1'
                soup = BeautifulSoup(requests.get(base_url).content, 'lxml')
    except requests.exceptions.RequestException as e:
        moviesDictionary['Status'] = False,
        moviesDictionary['error'] = str(e),
        return moviesDictionary

    moviesDictionary['Page'] = currentPage
    items = soup.find_all('li', class_="video-block")

    for item in items:
        try:
            #link
            a = item.find('a')
            href = a.get('href')
            link = f'https://{host}{href}'
            #Movie Cover
            conver = item.find('div', class_="picture")
            img = conver.find('img')
            poster = img['src']
            #Movie Title
            Name = item.find('div', class_="name").text
            nl0 = Name.replace('\n                        ', "")
            Title = nl0.replace('    \n                ', "")
            
            Year = item.find('span', class_="date").text
   
        except Exception as e:
            link = str(e) 
            poster = str(e)
            Title = str(e)
            Year = str(e)
            
        moviesObject = {'Title': Title, 'Cover': poster, 'link': link, 'Date': Year}  
        moviesDictionary['Results'].append(moviesObject)
   
    return moviesDictionary