import requests
from bs4 import BeautifulSoup
from api.proxy import Random_Proxy

'''
Credits: Joshua .
URL: https://lethals.org.
Copyright\Trademark: © 2022 - 2023 Lethal Services ™ ​| All rights reserved.
'''

def getAnix(query, page, proxie):
    moviesDictionary = {'Status': True,'Query': query,'Results': []}
    proxy = Random_Proxy()
    try:
        if proxie == 'true':
            if page != None:
                base_url = f'https://anix.to/filter?keyword={query}&page={page}'
                currentPage = page
                r = proxy.Proxy_Request(url=base_url, request_type='get')
                soup = BeautifulSoup(r.content, 'lxml')
            else:
                base_url = f'https://anix.to/filter?keyword={query}'
                currentPage = '1'
                r = proxy.Proxy_Request(url=base_url, request_type='get')
                soup = BeautifulSoup(r.content, 'lxml')
        else:
            if page != None:
                base_url = f'https://anix.to/filter?keyword={query}&page={page}'
                currentPage = page
                soup = BeautifulSoup(requests.get(base_url).content, 'lxml')
            else:
                base_url = f'https://anix.to/filter?keyword={query}'
                currentPage = '1'
                soup = BeautifulSoup(requests.get(base_url).content, 'lxml')
    except requests.exceptions.RequestException as e:
        moviesDictionary['Status'] = False,
        moviesDictionary['error'] = str(e),
        return moviesDictionary

    moviesDictionary['Page'] = currentPage
    items = soup.find_all('div', class_='piece') #div class=""

    for item in items:
        try:
            #Link To Watch
            a = item.find('a')
            href = a.get('href')
            link = f'https://anix.to{href}'
            #Movie Cover
            conver = item.find('div', class_="inner")
            img = conver.find('img')
            poster = img['src']
            #Movie Title
            Title = item.find('div', class_="ani-name").text
            #Play Time
            Duration = item.find('span', class_="time dot").text
            #Content-Type
            Content = item.find('span', class_="type dot").text
   
        except Exception as e:
            link = str(e) 
            poster = str(e)
            Title = str(e)
            Duration = str(e)
            Content = str(e)
            
        moviesObject = {'link': link, 'Cover': poster, 'Title': Title, 'Duration': Duration, 'Content-Type': Content} #{'Title': Title, 'Cover': poster, , 'Date': Year}  
        moviesDictionary['Results'].append(moviesObject)
   
    return moviesDictionary