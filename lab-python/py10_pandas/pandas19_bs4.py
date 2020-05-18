"""
웹 주소(URL)의 형식
    프로토콜://서버주소[:포트번호]/경로?쿼리스트링
    https://sports.news.naver.com/news.nhn?oid=421&aid=0004637974
    프로토콜: https
    서버주소: sports.news.naver.com
    경로: news.nhn
    쿼리스트링(query string): oid=421&aid=0004637974

query string: 클라이언트(브라우저)가 서버로 보내는 정보
    파라미터_이름=파라미터_값
    파라미터가 여러개일 때는 &로 파라미터들을 구분
"""

import requests
from bs4 import BeautifulSoup

# 다음 뉴스 검색에서 '머신 러닝'으로 검색한 결과 50개의 뉴스 제목과 URL을 출력.
url = 'https://search.daum.net/search?nil_suggest=btn&w=news&DA=PGD&cluster=y&q=%EB%A8%B8%EC%8B%A0+%EB%9F%AC%EB%8B%9D'

# 5번 요청(request)를 보내고 응답(response) 처리
for i in range(1, 6):
    print(f'===== page {i} =====')
    req_params = {'p': i}  # 요청 파라미터(request parameter)
    # 쿼리 스트링에 요청 파라미터를 추가해서 요청을 보냄.
    res = requests.get(url, req_params)
    # 응답(response)의 결과를 BeautifulSoup 객체로 생성.
    html = res.text.strip()
    soup = BeautifulSoup(markup=html, features='html5lib')
    # HTML 문서에서 필요한 부분만 선택
    news_link = soup.select('#clusterResultUL li div.wrap_cont a.f_link_b')
    for link in news_link:
        news_url = link.get('href')
        news_title = link.text
        print(news_url, news_title)


# 다음 뉴스 검색에서 임의의 검색어로 검색한 결과를 원하는 페이지 수만큼 출력할 수
# 있도록 함수를 작성.

