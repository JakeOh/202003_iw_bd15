# HTML 문서 분석(parsing)에 필요한 라이브러리: bs4, html5lib, lxml, ...
# anaconda 패키지에 기본으로 포함되어 있음 -> import해서 사용.

from bs4 import BeautifulSoup

# HTML 문서 open
with open('web01.html', mode='r', encoding='utf-8') as f:
    # BeautifulSoup 클래스의 객체를 생성
    soup = BeautifulSoup(markup=f, features='html5lib')
    print(type(soup))
    # print(soup)
    # soup: HTML 문서의 모든 구조, 내용을 담고 있는 객체

    # HTML 문서에서 h1 요소(element)를 찾음.
    h1 = soup.find('h1')  # find('태그이름')
    print(type(h1), h1)

    # h1 태그 안의 텍스트(text)만 찾음.
    print(h1.text)
    print(soup.find('h1').text)

    # HTML 문서에서 h2 태그 안의 텍스트를 출력
    print(soup.find('h2').text)

    # find('태그이름'): HTML 문서에서 가장 처음 등장하는 태그 요소 1개만 반환.
    print(soup.find('a'))  # HTML 문서에서 첫번째 a 태그가 반환됨.
    print(soup.find('a').text)  # a 태그의 텍스트

    # 태그가 가지고 있는 속성(attribute)의 값을 알아내는 방법: Tag.get(attr)
    link = soup.find('a')
    link_href = link.get('href')
    print(link_href)

    # soup.find('tag_name')와 soup.tag_name는 동일한 기능
    print(soup.h1.text)
    print(soup.h2.text)
    print(soup.a.text)
    print(soup.a.get('href'))

    # HTML 문서에 있는 모든 a 태그를 찾는 방법: find_all('tag_name')
    links = soup.find_all('a')
    print(links)  # a 태그들의 리스트
    for link in links:
        print(link.get('href'))

    # soup.find_all('tag_name')와 soup('tag_name')는 동일한 기능.
    for link in soup('a'):  # for link in soup.find_all('a'):
        print(link.get('href'))
