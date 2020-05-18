from bs4 import BeautifulSoup

# web03.html 파일을 open
with open('web03.html', mode='r', encoding='utf-8') as f:
    # HTML 파일을 BeautifulSoup 클래스 객체로 생성
    soup = BeautifulSoup(markup=f, features='html5lib')
    # class 속성의 값이 menu_item인 모든 요소들을 찾아서 출력
    print(soup(class_='menu_item'))

    # class 속성의 값이 menu_item인 요소의 자식 요소인 a 태그 찾음.
    # soup.select('CSS selector 형식')
    item = soup.select('.menu_item > a')
    print(item)
    # 클래스 menu_item의 자식(child) 요소 a의 href 속성만 출력
    for link in soup.select('.menu_item > a'):
        print(link.get('href'))

    # 클래스 menu의 자손(descendant) 요소 a의 href 속성을 출력
    for link in soup.select('.menu a'):
        print(link.get('href'))
