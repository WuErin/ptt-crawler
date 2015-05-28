# __author__ = 'Erin'

import requests
from bs4 import BeautifulSoup

index = requests.get('https://www.ptt.cc/bbs/elderly/M.1394156981.A.18E.html')
soup = BeautifulSoup(index.text)

for item in soup.select('#main-content'):
    a = str(item).find('<span class=\"f2\">')
    print BeautifulSoup(str(item)[:a]).text


