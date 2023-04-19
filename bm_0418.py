from bs4 import BeautifulSoup
import requests
from google.cloud import translate
from datetime import datetime

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
           "Accept-Language": "en-US,en;q=0.5",
           "Pragma": "no-cache",
           "Cache-Control": "no-cache"}

cookies = {'muid': 'LY3EGO86Xdlr9TN'}
#### 慢慢慢慢慢慢慢慢慢慢慢慢慢慢慢 ####
url = input("news url: ")
#### 慢慢慢慢慢慢慢慢慢慢慢慢慢慢慢 ####
resp = requests.get(url, headers = headers, cookies=cookies)
soup = BeautifulSoup(resp.content, 'html.parser')
print(resp.status_code)

result =''
def translate_text(text="", project_id="able-hull-381502"):
    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": "en-US",
            "target_language_code": "zh-TW",
        }
    )
    for translation in response.translations:
        result = "Translated text: {}".format(translation.translated_text)
    return result

now = datetime.now()
year = now.year
month = now.month
day = now.day

content_box=''
title = soup.find('h1', 'm-detail-header--title').get_text()
print(title)
contents = soup.find('div', 'm-detail--body')
for i in contents.find_all('p'):
    content_box = content_box + i.get_text()
print(content_box)

#### 慢慢慢慢慢慢慢慢慢慢慢慢慢慢慢 ####
#### 慢慢慢慢慢慢慢慢慢慢慢慢慢慢慢 ####
result = translate_text(text = f'{title}\n\n{content_box}')
print(result)
# path = f'/Users/jacobhuang/news/{month}/{title}.txt'
# with open(path,'a') as file:
#     file.writelines(f'{url}\n\n{title}\n\n{result}')

#### 慢慢慢慢慢慢慢慢慢慢慢慢慢慢慢 ####
#### 慢慢慢慢慢慢慢慢慢慢慢慢慢慢慢 ####