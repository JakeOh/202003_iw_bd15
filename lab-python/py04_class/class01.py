"""
class(클래스): 데이터(변수)와 기능(함수)을 갖는 데이터 타입.
method(메서드): 클래스 안에서 정의한 함수.
"""
# help(str)
name = 'itwill'
print(type(name))  # class str
# str 클래스가 가지고 있는 데이터: 'itwill'
# str 클래스가 가지고 있는 기능(method)는 변수이름.메서드이름() 형식으로 사용
print(name.capitalize())
print(name.upper())
print(name.startswith('it'))

article = 'Hello, Python! 안녕하세요 파이썬'
words = article.split()
print(words)


numbers = list()
# numbers: 클래스 list의 인스턴스(instance)
# list(): 클래스 list의 인스턴스 생성(instantiate) <- 클래스 이름을 함수처럼 호출.
print('type of numbers:', type(numbers))
print(numbers)
numbers.append(10)  # 인스턴스의  메소드를 호출 - append 기능
numbers.append(5)
print(numbers)
numbers.sort()  # sort 기능 - 메소드 호출
print(numbers)

