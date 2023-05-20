#U23
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
import pandas as pd
headers = {
    "User-Agent" : "Yoojihyun"
}
webpage = requests.get("https://www.transfermarkt.com/premier-league/marktwerte/wettbewerb/GB1/pos/Sturm/detailpos/0/altersklasse/u23", headers=headers)
#print(webpage)
soup=BeautifulSoup(webpage.content, "html.parser")
player_info = soup.find_all('tr',{'class':['odd','even']})
for info in player_info:
    player = info.find_all('td',{'class':['hauptlink','rechts hauptlink']})
print(player)
# 이름과 가치를 담을 빈 리스트 만들기
tr_name = []
tr_value = []

# player_info에서 'td' 태그만 모두 찾기
for info in player_info:
    player = info.find_all('td', {'class': ['hauptlink', 'rechts hauptlink']})
    # 이름과 가치 정보 추출 및 리스트에 추가
    tr_name.append(player[0].text.strip())
    tr_value.append(player[1].text.strip())

# 결과 출력
for i in range(len(tr_name)):
    print("이름:", tr_name[i])
    print("가치:", tr_value[i])
    print("----------")

