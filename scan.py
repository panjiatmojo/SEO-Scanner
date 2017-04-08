import urllib.parse
import urllib.request
import sys

from module.metadata import MetaData as meta
from module.keyword import Keyword as keyword

import json

url = sys.argv[1]

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

print('starting access')

req = urllib.request.Request(url, data=None, headers={'User-Agent':userAgent})


content = ""
with urllib.request.urlopen(req) as response:
   content = str(response.read())
   
print('successfully fetch ', url)

metaData = meta()
metaDataResult = metaData.extract(content)

with open('./result/metadata.json', 'w') as outfile:
    json.dump(metaDataResult, outfile)

keyword = keyword()
keywordResult = keyword.extract(content)	

with open('./result/keyword.json', 'w') as outfile:
    json.dump(keywordResult, outfile)