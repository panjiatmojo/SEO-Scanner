import urllib.parse
import urllib.request
import sys

from module.metadata import MetaData as meta
from module.keyword import Keyword as keyword
from module.export import Export as export
from module.title import Title as title
from module.description import Description as description
from module.image import Image as image
from module.link import Link as link

import json

url = sys.argv[1]

document = export()

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

print('starting access')

req = urllib.request.Request(url, data=None, headers={'User-Agent':userAgent})


content = ""
with urllib.request.urlopen(req) as response:
   content = str(response.read())

with open('./result/original.html', 'w') as outfile:
	outfile.write(str(content))
   
print('successfully fetch ', url)

title = title()
titleResult = title.extract(content)

document.add_content(title.format(titleResult))

with open('./result/title.json', 'w') as outfile:
    json.dump(titleResult, outfile)

description = description()
descriptionResult = description.extract(content)

document.add_content(description.format(descriptionResult))

with open('./result/title.json', 'w') as outfile:
    json.dump(titleResult, outfile)

#	gather the images
image = image()
imageResult = image.extract(content)

document.add_content(image.format(imageResult))

#	gather the links
link = link()
linkResult = link.extract(content)

document.add_content(link.format(linkResult))

#	gather the metadata
metaData = meta()
metaDataResult = metaData.extract(content)

document.add_content(metaData.format(metaDataResult))

with open('./result/metadata.json', 'w') as outfile:
    json.dump(metaDataResult, outfile)

keyword = keyword()
keywordResult = keyword.extract(content)	

document.add_content(keyword.format(keywordResult))

with open('./result/keyword.json', 'w') as outfile:
    json.dump(keywordResult, outfile)


document.set_title("Result for " + url)
document.generate()