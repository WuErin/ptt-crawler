# __author__ = 'Erin'

import sys
import requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")

# open first page
ptt_url = 'https://www.ptt.cc'
first_link = '/bbs/elderly/index1.html'
index = requests.get(ptt_url+first_link)
soup = BeautifulSoup(index.text)

url=[]
page_url = []
page_url.append(first_link)

# get all page links of elderly section
next_page = soup.select('.btn-group')[1]
next_page = next_page.findAll('a',{'class':'btn'})[2]
page_link = next_page['href']
while page_link!=None:
    page_url.append(page_link)
    index1 = requests.get(ptt_url+page_link)
    soup1 = BeautifulSoup(index1.text)
    next_page1 = soup1.select('.btn-group')[1]
    next_page2 = next_page1.findAll('a',{'class':'btn wide'})[2]
    if next_page1.findAll('a',{'class':'btn wide disabled'}):
        break
    else:
        page_link = next_page2['href']
print page_url

# get all url in elderly section
for i in xrange(len(page_url)):
    page_soup = BeautifulSoup(requests.get(ptt_url+page_url[i]).text)
    for item in page_soup.select('#main-container'):
        res = item.findAll('div',{'class':'title'})
        for href in res:
            for a in href.a['href'].split():
                if a!=None:
                    url.append(a)
    i = i+1
print(url)

outfile=open("ptt_elderly.txt","w+")
for j in xrange(len(url)):
    web = requests.get(ptt_url+url[j])
    content_soup = BeautifulSoup(web.text)
    content=""
    for item in content_soup.select('#main-content'):
        a = str(item).find('<span class=\"f2\">')
        content=content+BeautifulSoup(str(item)[:a]).text
    # if content_soup.findAll('div',{'class':'article-metaline'}):
    #     for k in xrange(len(content_soup.select('.article-meta-value'))):
    #         content = content+content_soup.select('.article-meta-value')[k].text+" --- "
    # else:
    #     continue
    outfile.write(content+'\n')
outfile.close()