import requests, random
from bs4 import BeautifulSoup

#This was Found On Github Not Made By Lethals.

class Random_Proxy(object):
    def __init__(self):
        self.__url = 'https://www.sslproxies.org/'
        self.__headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive',
            }
        self.random_ip = []
        self.random_port = []

    def __random_proxy(self):
        """
        This is Private Function Client Should not have accesss
        :return: Dictionary object of Random proxy and port number
        """
        r = requests.get(url=self.__url, headers=self.__headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        for x in soup.findAll('td')[::8]:
            self.random_ip.append(x.get_text())

        for y in soup.findAll('td')[1::8]:
            self.random_port.append(y.get_text())

        z = list(zip(self.random_ip, self.random_port))
        number = random.randint(0, len(z)-50)
        ip_random = z[number]
        ip_random_string = "{}:{}".format(ip_random[0],ip_random[1])
        proxy = {'https':ip_random_string}
        return proxy

    def Proxy_Request(self,request_type='get',url='',**kwargs):
        """
        :param request_type: GET, POST, PUT
        :param url: URL from which you want to do webscrapping
        :param kwargs: any other parameter you pass
        :return: Return Response
        """
        while True:
            try:
                proxy = self.__random_proxy()
                r = requests.request(request_type,url,proxies=proxy,headers=self.__headers ,timeout=5, **kwargs)
                return r
            except:
                pass