import requests
from bs4 import BeautifulSoup

#내가 정보를 가져오고 싶은 URL를 변수로 저장
Webtoon_URL = f'https://comic.naver.com/webtoon/weekdayList?week=thu'
#get 요청으로 페이지 정보 저장해두기
webtoon_html = requests.get(Webtoon_URL)
#설치했던 bs4f라이브러리로 불러서 저장했던 html을 원하는 형태로 파싱(원하는 상태로 정보를 가공하는 것)해서 soup변수에 저장
webtoon_soup = BeautifulSoup(webtoon_html.text, "html.parser")

webtoon_list_box = webtoon_soup.find("ul",{"class":"img_list"})
webtoon_list = webtoon_list_box.find_all("li")

# title = webtoon_list[1].find("dl").find("dt").find("a").string
# author = webtoon_list[1].find("dl").find("dd",{"class":"desc"}).find("a").text

# webtoon_list2 = webtoon_list[1].find("dl").find_all("dd")
# rating = webtoon_list2[1].find("div",{"class":"rating_type"}).find("strong").text

def extract_info(webtoon_list): 
    result = []

    for webtoon in webtoon_list:
        title = webtoon.find("dl").find("dt").find("a").string
        author = webtoon.find("dl").find("dd",{"class":"desc"}).find("a").text

        rating_list = webtoon.find("dl").find_all("dd")
        rating = rating_list[1].find("div",{"class":"rating_type"}).find("strong").text

        webtoon_info = {
            'title': title,
            'author': author,
            'rating' : rating,
        }
        result.append(webtoon_info)
    return result