import requests
import pandas as pd

# Get json and open
boardLetter = 'pol'
url = "https://a.4cdn.org/" + boardLetter + "/catalog.json"


response = requests.get(url)
threadCatalog = json.loads(response.text)

# First page of catalog

frontPage = threadCatalog[0]['threads']
#print(frontPage)
#type(frontPage)
    
# columns, keys

cols = ['no', 'now', 'name', 'sub', 'com', 'filename', 'ext', 'w', 'h', 'tn_w', 'tn_h', 'tim', 'time', 'md5', 'fsize', 'resto', 'id', 'country', 'm_img', 'bumplimit', 'imagelimit', 'semantic_url', 'country_name', 'replies', 'images', 'omitted_posts', 'omitted_images', 'last_replies', 'last_modified' ]


# Parsing front page threads/posts; Creating df

individualThreads = frontPage
test_df = pd.DataFrame(individualThreads, columns=cols)
