import requests
from bs4 import BeautifulSoup
from Webtoon import extract_info
import csv

file = open('webtoon.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title","author","rating"])

#내가 정보를 가져오고 싶은 URL를 변수로 저장
Webtoon_URL = f'https://comic.naver.com/webtoon/weekdayList?week=thu'
#get 요청으로 페이지 정보 저장해두기
webtoon_html = requests.get(Webtoon_URL)
#설치했던 bs4f라이브러리로 불러서 저장했던 html을 원하는 형태로 파싱(원하는 상태로 정보를 가공하는 것)해서 soup변수에 저장
webtoon_soup = BeautifulSoup(webtoon_html.text, "html.parser")

webtoon_list_box = webtoon_soup.find("ul",{"class":"img_list"})
webtoon_list = webtoon_list_box.find_all("li")
final_result = extract_info(webtoon_list)

for result in final_result:
    row=[]
    row.append(result['title'])
    row.append(result['author'])
    row.append(result['rating'])
    writer.writerow(row)
print(final_result)