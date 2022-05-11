import requests
import pandas as pd
import datetime

import json

from bs4 import BeautifulSoup
from datetime import date

import nltk

import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer

def get_frontpage(boardLetter):
    
    url = "https://a.4cdn.org/" + boardLetter + "/catalog.json"
    
    kw_model = keybert.KeyBERT()
    
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
        
        
    kw_list = []
    for i in range(result_df.shape[0]):
        
        if result_df.iloc[i]['sub'] is np.nan:
            sub = ''
        else:
            sub = result_df.iloc[i]['sub']
            
        if result_df.iloc[i]['com'] is np.nan:
            com = ''
        else:
            com = result_df.iloc[i]['com'] 
            
        text = sub + "    " + com
        
        keywords = kw_model.extract_keywords(text)
        
        klist = []
        for k in keywords:
            klist.append(k[0])
        
        kw_list.append(klist)
    
    result_df['keywords'] = kw_list
        
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

def frontpage_replies_sentiment(frontpage_replies_df):
    
    
    df = frontpage_replies_df
    reply_text_clean = []
    n = int(df.shape[0])
    for i in range(n):
        print(i)
        try:
            if '>>' in df.iloc[i]['reply_text']:
                reply_text = df.iloc[i]['reply_text'][11:].replace(">","")
            else:
                reply_text = df.iloc[i]['reply_text']
        except:
            print('error')
            reply_text=''
        reply_text_clean.append(reply_text)
        
    df['reply_text_clean'] = reply_text_clean
    
    thread_ids = list(set(df['thread_id']))
    
    thread_clean_df = pd.DataFrame()
    
    thid_list = []
    conctext_list = []
    neg_list = []
    pos_list = []
    neu_list = []
    
    sia = nltk.sentiment.SentimentIntensityAnalyzer()
    
    for i in thread_ids:
        print(i)
    
        text = df[df['thread_id'] == i]['reply_text_clean']
    
        conctext = ''
        for t in text:
            conctext = t + """
            
            """ + conctext
    
        thid_list.append(i)
        conctext_list.append(conctext)
        
        neg = sia.polarity_scores(conctext)['neg']
        pos = sia.polarity_scores(conctext)['pos']
        neu = sia.polarity_scores(conctext)['neu']
        
        neg_list.append(neg)
        pos_list.append(pos)
        neu_list.append(neu)
        
    thread_clean_df = pd.DataFrame()
    thread_clean_df['thread_id'] = thid_list
    thread_clean_df['concat_replies_text'] = conctext_list
    thread_clean_df['neg'] = neg_list
    thread_clean_df['pos'] = pos_list
    thread_clean_df['neu'] = neu_list
    
    return thread_clean_df


def main():


    # path='/Users/mo/dev/projects/scrapper_csvs/4chan_data/'
    path='C:/Users/chowd/OneDrive/Desktop/PY/'

    # Get json and open
    boardLetter = 'pol'
    url = "https://a.4cdn.org/" + boardLetter + "/catalog.json"

    frontpage_df = get_frontpage(boardLetter)

    thread_ids = list(set(frontpage_df['no']))

    frontpage_replies_df = get_frontpage_replies(boardLetter)
    
    fpr_sent_df = frontpage_replies_sentiment(frontpage_replies_df)    

    ctime = str(datetime.datetime.now().strftime("%Y%d%m%H%M%S"))

    frontpage_df.to_csv(path+'frontpage'+ctime+'.csv')
    frontpage_replies_df.to_csv(path+'frontpagereplies'+ctime+'.csv')
    fpr_sent_df.to_csv(path+'frontpagerepliesSentiment'+ctime+'.csv')
    
    df = frontpage_replies_df
    
    reply_doc = list(df[df['thread_id'] == '376916482']['reply_text_clean'])
    type(reply_doc)
    
    vectorizer = sklearn.feature_extraction.text.TfidfVectorizer()
    vectors = vectorizer.fit_transform(reply_doc)
    feature_names = vectorizer.get_feature_names()
    dense = vectors.todense()
    denselist = dense.tolist()
    tf = pd.DataFrame(denselist, columns=feature_names)
    
if __name__ == "__main__":
        main()
