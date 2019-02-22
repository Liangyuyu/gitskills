import time
from bs4 import BeautifulSoup
import requests
from urllib import request
import urllib
import sys
import os
import importlib


importlib.reload(sys)
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
}


def getfromBaidu(word):
    try:
        os.remove('url.txt')
    except:
        pass
    start = time.time()
    file_name_id = 1
    url = 'https://www.baidu.com.cn/s?wd=' + urllib.parse.quote(word) + '&pn='
    for k in range(1, 10):
        geturl(url, k)
    for url in open('url.txt'):
        print(url.strip())
        save_html(url.strip(), file_name_id)
        file_name_id += 1
    end = time.time()
    print(end - start)


def save_html(url, filename):
    r_page = requests.get(url)
    f = open(str(filename) + '.html', 'wb')
    f.write(r_page.content)
    f.close()
    return r_page


def geturl(url, k):
    path = url + str((k - 1) * 10)
    response = request.urlopen(path)
    page = response.read()
    soup = BeautifulSoup(page, 'lxml')
    tagh3 = soup.find_all('h3')
    for h3 in tagh3:
        href = h3.find('a').get('href')
        baidu_url = requests.get(url=href, headers=headers, allow_redirects=False)
        real_url = baidu_url.headers['Location']
        if real_url.startswith('http'):
            try:
                with open('url.txt', 'a') as f:
                    f.write(real_url + '\n')
                    f.close()
            except Exception as e:
                print(e)



if __name__ == '__main__':
    getfromBaidu('梁彧彧')
