from bs4 import BeautifulSoup

# web03.html 파일을 open
with open('web03.html', mode='r', encoding='utf-8') as f:
    # HTML 문서를 분석할 수 있도록 준비
    soup = BeautifulSoup(markup=f, features='html5lib')
    # 모든 div 태그 요소들을 찾아서, div의 텍스트만 출력
    for div in soup('div'):  # for div in soup.find_all('div'):
        print(div.text)

    # HTML 문서에서 속성(attribute)의 이름으로 요소들을 찾는 방법:
    # soup.find_all(attrs={'attr_name': 'attr_val', ...})
    # soup(attrs={'attr_name': 'attr_val', ...})

    # class 속성의 값이 c1인 모든 요소(element)들의 리스트
    print(soup.find_all(attrs={'class': 'c1'}))
    print(soup(attrs={'class': 'c1'}))

    # class 속성의 값이 c2인 모든 요소들의 텍스트를 출력.
    for c2 in soup(attrs={'class': 'c2'}):
        print(c2.text)

    # class 속성의 값이 c2이고, id 속성의 값이 id1인 요소들
    print(soup(attrs={'class': 'c2', 'id': 'id1'}))
    # class 속성의 값이 c1이고, id 속성의 값이 id1인 요소들
    print(soup(attrs={'class': 'c1', 'id': 'id1'}))

    # class 이름으로 HTML 요소를 찾는 방법:
    # soup.find_all(class_='class_name')
    # soup(class_='class_name')

    # id 이름으로 HTML 요소를 찾는 방법:
    # soup.find_all(id='id_name')
    # soup(id='id_name')

    # class 속성의 값이 c1인 요소들의 텍스트 출력
    for c1 in soup(class_='c1'):
        print(c1.text)

    # id 속성의 값이 id1인 요소들의 텍스트를 출력
    for id1 in soup(id='id1'):
        print(id1.text)
