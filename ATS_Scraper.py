#abovetopsecret
#https://www.abovetopsecret.com
####
import pandas as pd
import numpy as np

import os
import sys

import requests
from bs4 import BeautifulSoup

import json


#path variable of python work directory
path = '/path/goes/here'

#url
url = 'https://www.abovetopsecret.com'


#running requests get method to retrieve url data
request = requests.get(url)

#request type
type(request)

#status code of request session
request.status_code
type(request.status_code)


#content of the html of the request 
request.content
type(request.content)

#printing request content from page variable 
with open(path + "/ATS_0417_1.txt", "w") as f:
    f.write(request.text)


#beatiful soup web scraping

#declaring soup variable to use html parser
soup = BeautifulSoup(request.content, "html.parser")
type(soup)

#find_all tag from html with div element and class content4x
content4x_banner = soup.find_all("div", class_="content4x")
len(content4x_banner)
type(content4x_banner)

content1x_banner = soup.find_all("div", class_="content1x")
len(content1x_banner)


#another find_all method
content4x_banner = soup.find_all("div", {"class": "content4x"})
len(content4x_banner)

content1x_banner= soup.find_all("div", {"class": "content1x"})
len(content1x_banner)

i=1

content4x_banner
type(content4x_banner)
len(content4x_banner)

content4x_banner[0]
content4x_banner[1]
content4x_banner[2]
content4x_banner[3]

ban = content4x_banner[i]


ban
forum_ban = ban.find_all('a', {'class': 'forumsm', 'href': True})
forum_ban
type(forum_ban)
len(forum_ban)

forum_ban[0]
type(forum_ban[0])

forum_ban[1]['class']
forum_ban[1]['href']
forum_ban[1].text




head = ban.find_all('a', {'class': 'H1 h1home', 'href': True})
len(head)
type(head)
href = head[0]['href']
title = head[0].text






#banner link
tags = ban.find_all('a', {'class': 'forumsm', 'href': True})
len(tags)
type(tags)
tags[0]['href']

ban
head = ban.find_all('a', {'class': 'H1 h1home', 'href': True})
len(head)
type(head)
href = head[0]['href']
title = head[0].text







for i in range(3,10,2):
    print(i)


a = content4x_banner
soup_find_a = soup.find_all('a')
type(soup_find_a)
len(soup_find_a)

i=120
soup_find_a[i]

link_list = []

aban = soup.find_all('a',{'class': 'H1 h1home', 'href': True})
type(aban)
len(aban)

aban[0]
aban[0]['href']
aban[0]['class']
aban[0].text

for a in aban:
    #print(a)
    print(type(a))


<a href=" " class="H1 h1home"


for link in soup.find_all('a'):
    print(link.get('href'))
    #add elements to a list
    link_list.append(link.get('href'))
    
    
thread_link = []
for link in link_list:
    try:
        if '/forum/thread' in link and '/pg' in link:
            thread_link.append(link)
    except TypeError:
        continue


type(link_list)

ft = '/forum/thread'

pt = '/pg'

t = '/forum/thread1309141/pg1'

ft in t
pt in t

thread_link = []
for link in link_list:
    if '/forum/thread' in link and '/pg' in link:
        thread_link.append(link)


#content banner
i=0
ban = content4x_banner[i]

ban
head = ban.find_all('a', {'class': 'H1 h1home', 'href': True})
len(head)
type(head)
href = head[0]['href']
title = head[0].text


content4x_banner
content1x_banner

len(content4x_banner)

href_list = []
title_list = []

for ban in content4x_banner:
    head = ban.find_all('a', {'class': 'H1 h1home', 'href': True})
    if len(head) == 0:
        continue
    href = head[0]['href']
    title = head[0].text
    
    href_list.append(href)
    title_list.append(title)
    
    print(href)
    print(title)


for i in range(8):
    print(i)
    #print("b {}".format(i%2))
    
    if(i%3==2):
        print('b')
        continue
    
    print('a')




#banner link
tags = ban.find_all('a', {'class': 'forumsm', 'href': True})
len(tags)
type(tags)
tags[0]['href']

ban
head = ban.find_all('a', {'class': 'H1 h1home', 'href': True})
len(head)
type(head)
href = head[0]['href']
title = head[0].text

print(head[0])

#banner
content4x_banner
type(content4x_banner)
len(content4x_banner)
content4x_banner[0]
content4x_banner[1]
content4x_banner[15]
content4x_banner[16]

type(content4x_banner[0])




i=1

ban = content4x_banner[i]
ban
type(ban)

ban_div = ban.find_all("div", {"class": "footline"})
len(ban_div)
type(ban_div)
a[0]


tags = ban.find_all('a', {'class': 'forumsm', 'href': True})
len(tags)
type(tags)
tags[0]['href']




a = ban.find_all('a', href=True)
len(a)
type(a)
a[0]
a[1]
a[2]

banner_test = content4x_banner[i]
type(content4x_banner)
type(banner_test)

a = content4x_banner[i].get('a')
a


banner_test['href']


banner_test['href']

a = banner_test.get('div')
print(a)

tag_test_1= soup.find_all("div", {"class": "homeRight"})

len(tag_test_1)
tag_test_1[0]


content4x_banner[0]
type(content4x_banner[0])

content4x_banner[0]

##########


soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


