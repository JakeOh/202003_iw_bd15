import requests  # Python 기본 모듈 - 웹 서버로 요청을 보내고 응답을 처리.
from bs4 import BeautifulSoup

# 접속할 사이트 주소, 요청(request)를 보낼 웹 서버 주소
url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%20%EB%9F%AC%EB%8B%9D&DA=YZR&spacing=0'

# 웹 서버로 GET 방식의 요청(request)을 보냄
# GET 요청: 웹 서버로 보내는 정보(파라미터)가 URL 주소에 노출되는 방식
# POST 요청: 웹 서버로 보내는 정보가 URL 주소에 노출되지 않고, 패킷에 포함되는 방식.
response = requests.get(url)
print(response)  # <Response [200]>: 정상적으로 응답(response) 수신.

# 응답 객체에서 HTML 텍스트를 추출
html = response.text.strip()
print(html[:100])

# HTML 텍스트를 BeautifulSoup 객체로 생성
soup = BeautifulSoup(markup=html, features='html5lib')

# HTML 문서에서 id="clusterResultUL"인 요소(element)를 찾음.
cluster_result = soup.find(id='clusterResultUL')
print(cluster_result)

news_links = soup.select('#clusterResultUL li div.wrap_cont a.f_link_b')
for link in news_links:
    print(link.text, link.get('href'))
