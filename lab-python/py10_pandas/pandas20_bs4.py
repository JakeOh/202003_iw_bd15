import requests
from bs4 import BeautifulSoup


def hani_search(keyword, npage):
    # 기사 링크 주소, 기사 제목, 기사 등록 시간
    url = 'http://search.hani.co.kr/Search?command=query&media=news&submedia=&sort=d&period=all'
    for i in range(npage):
        print(f'\n===== page {i + 1} =====')
        req_params = {
            'keyword': keyword,
            'pageseq': i
        }
        res = requests.get(url, params=req_params)
        html = res.text.strip()
        soup = BeautifulSoup(html, 'html5lib')
        results = soup.select('ul.search-result-list li dl dt a')
        dates = soup.select('ul.search-result-list li dl dd.date dd')
        for link, date in zip(results, dates):
            news_url = link.get('href')
            news_title = link.text
            news_date = date.text
            print(news_url, news_date, news_title)
            # new_url 주소로 GET 요청을 보내고, 응답 처리 -> 각 기사 본문 내용
            hani_article(news_url)


def hani_article(url):
    res = requests.get(url)  # url 주소로 GET 방식의 요청을 보내고, 응답을 받음.
    html = res.text.strip()  # 응답(response)의 텍스트만 추출
    soup = BeautifulSoup(html, features='html5lib')
    article = soup.select('div.article-text div.text')[0]  # 리스트에서 첫번째 요소
    for s in article.stripped_strings:
        print(s)
    print('***** end of article *****\n')


def daum_search(keyword, npage):
    url = 'https://search.daum.net/search?nil_suggest=btn&w=news&DA=PGD&cluster=y'
    for i in range(1, npage + 1):
        print(f'===== page {i} =====')
        # 요청 파라미터 추가하고 GET 요청을 보냄
        req_params = {
            'q': keyword,  # 검색어(q=keyword)
            'p': i  # 검색 페이지(p=1)
        }
        res = requests.get(url, req_params)
        # 응답 결과 처리
        html = res.text.strip()
        soup = BeautifulSoup(markup=html, features='html5lib')
        news_link = soup.select('#clusterResultUL li div.wrap_cont a.f_link_b')
        for link in news_link:
            news_url = link.get('href')
            news_title = link.text
            print(news_url, news_title)


if __name__ == '__main__':
    keyword = input('검색어 >>> ')
    pages = int(input('페이지 개수>>> '))
    # daum_search(keyword, pages)
    hani_search(keyword, pages)
