import tweepy
import config
from tweepy.auth import OAuthHandler
from time import sleep

client = tweepy.Client(config.Bearer_Token,config.API_KEY,config.API_KEY_SECRET, config.Access_Token, config.Access_Token_Select)

auth = tweepy.OAuth1UserHandler(config.API_KEY, config.API_KEY_SECRET)
auth.set_access_token(config.Access_Token, config.Access_Token_Select)
api = tweepy.API(auth)

url = 'https://www.coindesk.com/consensus-magazine/2023/04/15/true-consumer-protection-in-crypto-lies-between-centralization-and-decentralization/'
long_text = f"加密貨幣中真正的消費者保護，介於中心化和去中心化之間\n政府監管機構越來越關注加密貨幣的集中點。如何將這些用於每個人的利益？\n關於加密貨幣法規和合規性或缺乏合規性的敘述越來越沒有抓住要點。金融監管的總體目的是最大限度地保護消費者，防止欺詐和濫用，並確保市場秩序井然。從廣義上講，任何司法管轄區和任何金融監管機構的使命都是相同的。加密領域的對話過度集中在加密行業，而以犧牲加密用戶為代價。只要我們過分關注特定交易所是否必須遵守新的或現有的法規，我們就錯過了考慮消費者如何最大程度地受益的機會Timothy Cradle 是 Blockchain Intelligence Group 的監管事務總監和 Biokript 的合規顧問。作為監管事務作為董事和合規顧問，我傾向於從冷靜的角度看待加密監管和合規。在向客戶推薦或嘗試實施合規框架時，我必須將意識形態放在一邊。它歸結為一個簡單的問題：“需要做什麼來確保合規性。”限制太多，會對他們的商業模式產生負面影響。過於寬容會導致他們長期失敗（通常以執法行動的形式）。我當然並不孤單。作為一家加密貨幣初創公司的前首席合規官，我認識其他合規專業人士，他們對他們推薦的合規計劃承擔個人責任，因此犯錯是一個職業生存問題。在審視加密服務、去中心化服務和中心化服務這兩種相反的運營模式時，只有相互借鑒才能解決各自潛在的失敗。事實上，在過去的一周裡，美國財政部強調了許多值得注意的問題去中心化金融 (DeFi) 帶來的金融犯罪風險——包括洗錢、盜竊、詐騙和逃避制裁。該機構指出，“DeFi 服務通常有一個控制組織，該組織提供集中管理和治理的措施。”在我的合規觀念中，這意味著實施與中央機構預期的相同類型的監管控制既不是不可能，也不是不合理的。事實上，2022 年 12 月提交給美國參議院的數字資產反洗錢法案似乎得出了相同的結論，因為它試圖將任何“促進數字資產交易”的服務納入銀行保密法（美國銀行保密法）的範圍。反洗錢法）。我們不需要政府告訴我們 DeFi 具有獨特的風險；對加密盜竊、盜竊、黑客攻擊和詐騙進行簡單搜索，就會發現一連串的 DeFi 失敗。中心化參與者顯然有自己的問題。就在過去的一個月裡，我們看到了關於幣安及其避免最基本合規形式的嚴厲揭露，即了解你的客戶（KYC）和監管註冊規則。 Binance 在美國被起訴，可能會退出加拿大和英國，並可能失去其在澳大利亞的牌照（其監管機構在牌照公告中列出了 Binance 監管失誤的完整清單）。我們在美國也看到了多家公司。因未在美國證券交易委員會註冊其證券產品而被罰款，這當然意味著這些產品的用戶幾乎沒有或根本沒有消費者保護措施。這一切都發生在 2022 年的恥辱年之後，當時價值數十億美元的加密貨幣因公然欺詐、市場操縱、挪用公款和破產而損失——如果這些玩家不直接控制其用戶的資產，損失在很大程度上是可以避免的。我們需要雙方才能使對方運作良好？來自中心化實體：透明度和問責制。一個本質上負責的組織，擁有面向公眾的個人。換句話說，受監管的參與者需要確保其以用戶的最大利益行事，以誠實的方式披露風險，並可能被迫為此提供必要的披露。 （不，區塊鏈上未歸屬的交易的透明度不夠高。）這些公司還必須實施網絡安全、欺詐和洗錢控制——僅靠智能合約審計是不行的。另請參閱：讓我們實際承諾證明這次預約好嗎？ |來自去中心化實體的意見：交易結算在服務中，而資產保管始終在用戶手中。我們需要記住，加密的最終目標是為個人提供比他們從遺留系統中獲得的更好的金融系統。監管的最終目標是確保消費者受到保護。我們通過混合這兩種哲學來獲得最好的結果，就像我們需要混合中心化金融和去中心化金融的哲學以實現一個對所有參與者公平和有用的系統一樣。監督加密貨幣的正確規則已經到位為了保護消費者，行業現在需要的是在不失去權力下放原則的情況下接受集中化的正確方面。"

chunks = [long_text[i:i+140] for i in range(0, len(long_text), 140)]
tweet1 = api.update_status(chunks[0])
previous_tweet_id = tweet1.id
for text in chunks[1:]:
    tweet = api.update_status(text, in_reply_to_status_id=previous_tweet_id)
    previous_tweet_id = tweet.id
    sleep(3)
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