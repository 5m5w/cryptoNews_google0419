import tweepy
import config
from tweepy.auth import OAuthHandler
from time import sleep

client = tweepy.Client(config.Bearer_Token,config.API_KEY,config.API_KEY_SECRET, config.Access_Token, config.Access_Token_Select)

auth = tweepy.OAuth1UserHandler(config.API_KEY, config.API_KEY_SECRET)
auth.set_access_token(config.Access_Token, config.Access_Token_Select)
api = tweepy.API(auth)

url = ''
long_text = f""

# 將長文切成每一tweet不超過250字元的限制（中文字佔2個字元）
chunks = [long_text[i:i+140] for i in range(0, len(long_text), 140)]
# 先發布第一則tweet
tweet1 = api.update_status(chunks[0])
# 取得第一則tweet的ID
previous_tweet_id = tweet1.id
# 用for迴圈接續第一則tweet的下方，發布第二則tweet，以此類推
for text in chunks[1:]:
    tweet = api.update_status(text, in_reply_to_status_id=previous_tweet_id)
    previous_tweet_id = tweet.id
    sleep(2)
# 在最後一段tweet貼上新聞網址
tweet = api.update_status(url,in_reply_to_status_id=previous_tweet_id)

# 將每個tweet在後面加上頁數
# for i, chunk in enumerate(chunks):
#     tweet1 = api.update_status(f'{chunk}({i+1}/{len(chunks)})')
#     print(tweet1)

# try:
#     api.verify_credentials()
#     print('yes')
# except:
#     print('failed')
