#4chan /pol

import requests
import pandas as pd

import json

from bs4 import BeautifulSoup

def get_frontpage(boardLetter):
    
    url = "https://a.4cdn.org/" + boardLetter + "/catalog.json"
    
    response = requests.get(url)
    status_code = response.status_code
    print(status_code)
    
    print("get_frontpage \n url: {} \n response status code: {}".format(url, status_code))
    
    result_df = pd.DataFrame()
    cols = ['no', 'now', 'name', 'sub', 'com', 'filename', 'ext', 'w', 'h', 'tn_w', 'tn_h', 'tim', 'time', 'md5', 'fsize', 'resto', 'id', 'country', 'm_img', 'bumplimit', 'imagelimit', 'semantic_url', 'country_name', 'replies', 'images', 'omitted_posts', 'omitted_images', 'last_replies', 'last_modified' ]
    
    threadCatalog = json.loads(response.text)
    
    n = len(threadCatalog)

    for i in range(n):
        # print(i)
        
        df = pd.DataFrame(threadCatalog[i]['threads'], columns=cols)
        df['page_number'] = threadCatalog[i]['page']
        result_df = result_df.append(df,ignore_index=True)
        
    return result_df


def get_replies(boardLetter, thread_id):
    
    # boardLetter = 'pol'
    url = "https://boards.4chan.org/" + boardLetter + "/thread/" + str(thread_id)
    
    post_id = url.split("/")[-1]
    
    response = requests.get(url)
    print(response.status_code)
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    reply_divs = soup.find_all("div", {"class": "postContainer replyContainer"})
    
    #reply_count
    reply_count = len(reply_divs)
    
    result_df = pd.DataFrame()
    cols = ['thread_id','reply_id','reply_dt','reply_text']
    
    
    # i=2
    # reply = reply_divs[i]
    
    for reply in reply_divs:
        
        reply_id = reply["id"]
        
        reply_dt_tag = reply.find('span', {"class": "dateTime"})
        # len(reply_dt)
        reply_dt = reply_dt_tag.text
        
        reply_bq_tag = reply.find('blockquote')
        reply_text = reply_bq_tag.text
        
        # print("\npost_id: {}\nreply_id: {} \ndate: {} \ntext: \n\t{}".format(post_id,reply_id,reply_dt,reply_text))
        print("\npost_id: {}\nreply_id: {} \ndate: {}".format(post_id,reply_id,reply_dt))
        
        reply_list = [post_id,reply_id, reply_dt, reply_text]
        df = pd.DataFrame([reply_list],columns=cols)
        
        result_df = result_df.append(df, ignore_index=True)
        
    return result_df

def get_frontpage_replies(boardLetter):
    
    frontpage_df = get_frontpage(boardLetter)
    
    thread_ids = list(set(frontpage_df['no']))
    
    result_df = pd.DataFrame()

    for i in range(len(thread_ids)):
        print(i)
        thread_id=thread_ids[i]
        
        reply_df = get_replies(boardLetter, thread_id)
        result_df = result_df.append(reply_df,ignore_index=True)
        
    return result_df
    

def main():
    
    # Get json and open
    boardLetter = 'pol'
    url = "https://a.4cdn.org/" + boardLetter + "/catalog.json"
    
    frontpage_df = get_frontpage(url)

    thread_id = '375521299'    
    thread_url = url = 'https://boards.4chan.org/pol/thread/'+ thread_id + "/catalog.json"
    
    thread_id = '375506434'
    thread_df = get_replies(boardLetter, thread_id)
    
    thread_ids = list(set(frontpage_df['no']))
    
    frontpage_replies_df = get_frontpage_replies(boardLetter)
    
    
if __name__ == "__main__":
        main()   
    
    
