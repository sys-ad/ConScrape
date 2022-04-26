import urllib, json, os, datetime
from unidecode import unidecode
import unicodecsv as csv
import requests

import pandas as pd

# Get json and open
boardLetter = 'pol'
url = "https://a.4cdn.org/" + boardLetter + "/catalog.json"



response = requests.get(url)
threadCatalog = json.loads(response.text)

# First page of catalog

frontPage = threadCatalog[0]['threads']
print(frontPage)
type(frontPage)

for l in frontPage:
    print(l)
    
frontPage[2]['no']


type(frontPage)
type(frontPage[2])
type(frontPage[2]['threads'])


len(frontPage)
frontPage[1].keys()

fp_dict = {}


result_df = pd.DataFrame()

cols = ['no', 'sticky', 'closed', 'now', 'name', 'com', 'filename', 'ext', 'w', 'h', 'tn_w', 'tn_h', 'tim', 'time', 'md5', 'fsize', 'resto', 'id', 'capcode', 'semantic_url', 'replies', 'images', 'last_modified']

cols=[]
for i in frontPage[0].keys():
    cols.append(i)


fp_dict = {}
for i in range(len(frontPage)):
    print(i)
    
    cols=[]
    for co in frontPage[0].keys():
        cols.append(co)
    
    for c in cols:
        data.append(frontPage[i][c])
        
        df = pd.DataFrame([data], columns=cols)
        
    fp_dict[i] = df
        
    fp_df = fp_df.append(df)
    fp_df['index_0'] = i
    
    result_df = result_df.append(fp_df)
    

cols = ['no', 'sticky', 'closed', 'now', 'name', 'com', 'filename', 'ext', 'w', 'h', 'tn_w', 'tn_h', 'tim', 'time', 'md5', 'fsize', 'resto', 'id', 'capcode', 'semantic_url', 'replies', 'images', 'last_modified']


frontPage[1]['no']

data = []

for c in cols:
    data.append(frontPage[1][c])


df = pd.DataFrame([data], columns=cols)



#############3
strikes = [individualThread[int(x)] for x in individualThread.split()]

individualThread = json.loads(response.content)
j = 0
len(individualThread)
for post in individualThread:
    print(post)
    print(individualThread['now'])
		timeStamp = individualThread['posts'][j]['now']
		name = individualThread['posts'][j]['name']
		try:
			posterID = individualThread['posts'][j]['id']
		except:
			posterID = "No ID"
		postID = individualThread['posts'][j]['no']
		if 'sub' in individualThread['posts'][j]:
			subjectText = individualThread['posts'][j]['sub']
		else:
			subjectText = "No Subject Text Provided"
		if 'com' in individualThread['posts'][j]:
			commentText = individualThread['posts'][j]['com']
		else:
			commentText = "No Comment Text Provided"
		#Was there an image posted? Let's snag it!
		if 'tim' in individualThread['posts'][j]:
			OGfilename = unidecode(individualThread['posts'][j]['filename'])
			#OGfilename = unidecode(OGfilename)
			renamedFile = str(individualThread['posts'][j]['tim'])
			fileExtension = str(individualThread['posts'][j]['ext'])
			filename = OGfilename + " - " + renamedFile + fileExtension
			postFile = urllib.URLopener()
			try:
				postFile.retrieve("https://i.4cdn.org/" + boardLetter + "/" + renamedFile + fileExtension, saveDirectory + "/" + boardLetter + "/" + str(frontPage[i]['no']) + " - " + frontPage[i]['semantic_url'] + "/" + filename)
				downloadCounter = downloadCounter + 1
			except:
				print("Fille Download Error :(")
				filename = filename + " - Download Error"
		else:
			filename = "No File Posted"

###############
frontPage = threadCatalog[0]['threads']
print(frontPage)
frontPage = threadCatalog[2]['threads']
print(frontPage)
frontPage = threadCatalog[3]['threads']
print(frontPage)
frontPage = threadCatalog[10]['threads']
len(frontPage[0])
len(threadCatalog)
len(frontPage)
threadCatalog[0]['threads'])


l = frontPage
str(frontPage['sub'])

for i in range(len(l)):
    print(l[i])
    
