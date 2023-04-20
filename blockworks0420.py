from selenium import webdriver
from selenium.webdriver.common.by import By
from google.cloud import translate
from datetime import datetime

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

url = "https://blockworks.co/news/romania-nft-trading-multiversx"
webdriver = webdriver.Firefox()
webdriver.get(url)

content_box=''
title = webdriver.find_element(By.XPATH, "//*[@id='__next']/div/main/section[1]/div[1]/article/div[1]/h1")
print(title.text)
summary = webdriver.find_element(By.CSS_SELECTOR, '#__next > div > main > section.flex.flex-row.flex-wrap.lg\:flex-nowrap > div.basis-1\/1.lg\:basis-4\/6.h-full.p-5.md\:p-8.lg\:p-10.border-r-0.lg\:border-r.border-b.lg\:border-b-0 > article > div.flex.flex-col.justify-start.items-start.flex-grow-0.flex-shrink-0.relative.gap-3.w-full > p')
print(summary.text)
contents = webdriver.find_element(By.XPATH, '//*[@id="__next"]/div/main/section[1]/div[1]/article/div[3]/div[2]/section[1]/div')
for i in contents.find_elements(By.TAG_NAME, 'p')[:-3]:
    content_box = content_box + i.text
    
result = translate_text(text = f'{title}\n{summary}\n{content_box}')
print(result)
# path = f'/Users/jacobhuang/news/{month}/{title}.txt'
# with open(path,'a') as file:
#     file.writelines(f'{url}\n\n{title}\n\n{result}')
