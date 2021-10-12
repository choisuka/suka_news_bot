"""
import telegram

chat_token = "2099015091:AAHFrqoe7ezCRHkLSB63cQ34ATn04Xn82-s"
bot = telegram.Bot(token = chat_token)
updates = bot.getUpdates()
for u in updates:
    print(u.message['chat']['id'])
#choi : 2078832433
#suseongpark : 1339532440
"""

import telegram, datetime as dt, time

chat_token = "2099015091:AAHFrqoe7ezCRHkLSB63cQ34ATn04Xn82-s"
bot = telegram.Bot(token = chat_token)
updates = bot.getUpdates()
print(updates)
user_set = set()
for u in updates:
    user_set.add(u.message['chat']['id'])

user_lst = list(user_set)
print(user_lst)
"""
while True:
    date = dt.datetime.now()
    print(date)

    time.sleep(30)
    text = str(date)
    for usr in user_lst:
        bot.sendMessage(chat_id = usr, text=text)
"""

import requests
from bs4 import BeautifulSoup
import telegram

# 서치 키워드
search_word = '아마존'

# 기존에 보냈던 링크를 담아둘 리스트
old_links = []

# 스크래핑 함수 
def extract_links(old_links=[]):
    url = f'https://m.search.naver.com/search.naver?where=m_news&sm=mtb_jum&query={search_word}'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    search_result = soup.select_one('#news_result_list')
    news_list = search_result.select('.bx > .news_wrap > a')

    links = []
    for news in news_list[:5]:
        link = news['href']
        links.append(link)
    
    new_links=[]
    for link in links:
        if link not in old_links:
            new_links.append(link)
    
    return new_links

# 이전 링크를 매개변수로 받아서, 비교 후 새로운 링크만 출력
# 차후 이 부분을 메시지 전송 코드로 변경하고 매시간 동작하도록 설정
# 새로운 링크가 없다면 빈 리스트 반환

new_links = extract_links(old_links)
print('===보낼 링크===\n', new_links,'\n')

text = str(new_links)
for usr in user_lst:
    bot.sendMessage(chat_id = usr, text=text)    
