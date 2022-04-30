#abovetopsecret
#https://www.abovetopsecret.com

import pandas as pd
import numpy as np

import os
import sys

import requests
from bs4 import BeautifulSoup

import json
import psycopg2

!pip install psycopg2-binary
from sqlalchemy import create_engine


main_url = 'https://www.abovetopsecret.com'
url = 'https://www.abovetopsecret.com'
path = '/Users/mo/development/'


def mainPageThreadLinks(url):
    
    #Request
    request = requests.get(url)
    
    if request.status_code < 200 or request.status_code > 299:
        print("Request has failed with code {}".format(request.status_code))
        return request
    else:
        print("Request has passed with code {}".format(request.status_code))
    
    
    #Declare the soup
    soup = BeautifulSoup(request.content, "html.parser")
    #type(soup)

    #declare list to obtain all href links in a-tag html
    link_list = []

    for link in soup.find_all('a'):
        #print(link.get('href'))
        #add elements to a list
        link_list.append(link.get('href'))
        
    #create new list to retrieve thread links    
    thread_link = []
    for link in link_list:
        try:
            if '/forum/thread' in link and '/pg' in link:
                thread_link.append(link)
        except TypeError:
            continue

    #create new list of clean links
    thread_link_clean = []    

    for link in thread_link:
        if 'https://www.abovetopsecret.com/' not in link:
            thread_link_clean.append('https://www.abovetopsecret.com' + link)
        else:
            thread_link_clean.append(link)
            
    return thread_link_clean


def threadPostDF(url):
    
    request = requests.get(url)      
    print(request.status_code)
    
    if request.status_code < 200 or request.status_code > 299:
        return(request)

    soup = BeautifulSoup(request.content, "html.parser")
    
    #title
    title = soup.title.text

    thread_replies = soup.find_all('div', {'class': 'threadpostC post'})

    #initializing dataframe
    thread_df = pd.DataFrame()
    postid_list = []
    text_list = []
    
    for t in thread_replies:
        postid = t['id']
        #print(postid)
        
        postid_list.append(postid)
        text_list.append(t.text)
        
    thread_df['postid'] = postid_list
    thread_df['text'] = text_list
    thread_df['title'] = title
    thread_df['link'] = url
    
    return thread_df


def aboveTopFullDF(url):
    
    links = mainPageThreadLinks(url)
    
    result_df = pd.DataFrame()
    
    for link in links:
        print(link)
        tdf = threadPostDF(link)
        
        result_df = result_df.append(tdf)

    return result_df

result_df.to_csv(path+'/test1.csv')


links = mainPageThreadLinks(main_url)

tdf = threadPostDF(links[0])
tdf.to_csv(path+'/thread_df_0417_3.csv')

path
thread_df.to_csv(path+'/thread_df_0417_2.csv')
    
    


            

links = mainPageThreadLinks(url)
links
len(links)            
            
i=0           

l = links[i]            


l            

request = requests.get(l)      
request.status_code            

with open(path + "/link1_above_1.txt", "w") as f:
    f.write(request.text)            
            


soup = BeautifulSoup(request.content, "html.parser")  

#title of the link
soup.title.text

#date posted
date_threads = soup.find_all('div',{'class': 'posttopL'})
type(date_threads)
len(date_threads)

date_threads[0]
type(date_threads[0])
len(date_threads[0])


#Date posted
date_threads[0].text

#pid
pid_find = date_threads[0].find_all('a')
pid_find[0]['name']





thread_replies = soup.find_all('div', {'class': 'threadpostC post'})       
type(thread_replies)
len(thread_replies)        

#postid
thread_replies[0]['id']    

#thread
thread_replies[0].text


thread_replies[1].text
thread_replies[2] 
thread_replies[3] 
thread_replies[17].text 

type(thread_replies[0])

pid_thread = thread_replies[0].find_all('div')
pid_thread[0]
pid_thread[1]
pid_thread[2]
len(pid_thread)     

#DataFrame
result_df = pd.DataFrame()


links = mainPageThreadLinks(url)
         
i=0
l = links[i]  
print(l)     

request = requests.get(l)      
request.status_code          
           
soup = BeautifulSoup(request.content, "html.parser")  

#link
l

#title of the link
title = soup.title.text 


#date posted dataframe
date_df = pd.DataFrame()

#Date Posted
date_threads = soup.find_all('div',{'class': 'posttopL'})
len(date_threads)

dp_list = []
pid_list = []

for t in date_threads:
    print(t.text)
    dp_list.append(t.text)
    
    pid_find = t.find_all('a')
    pid = pid_find[0]['name']  

    print(pid)
    pid_list.append(pid)
    
date_df['dateposted'] = dp_list
date_df['pid'] = pid_list

date_df

type(date_df)



i=0

#Date posted
date_threads[i].text

#pid
pid_find = date_threads[i].find_all('a')
pid_find[i]['name']        
len(pid_find)
            





thread_replies = soup.find_all('div', {'class': 'threadpostC post'})

#title
title = soup.title.text

thread_df = pd.DataFrame()
postid_list = []
text_list = []

for t in thread_replies:
    postid = t['id']
    print(postid)
    
    postid_list.append(postid)
    text_list.append(t.text)
    
thread_df['postid'] = postid_list
thread_df['text'] = text_list
thread_df['title'] = title
thread_df['link'] = l


path
thread_df.to_csv(path+'Output/thread_df_0417_2.csv')






l = ['a','d','c']
result_df['test'] = l
result_df

result_df.to_sql('data1', engine, index=False)

thread_df.to_sql('tablee', engine, index=False)
thread_df


#postid
thread_replies[0]['id']    

#thread
thread_replies[0].text


#creating basic dataframe
df = pd.DataFrame()

engine = create_engine("postgresql+psycopg2://user1:Namaste1@localhost/postgres")

connection = engine.connect()
connection.close()








