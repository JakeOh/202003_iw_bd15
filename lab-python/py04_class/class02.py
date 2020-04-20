import math

"""
class 클래스이름:
    클래스 변수 선언/초기화

    def __init__(self, attr1, attr2, ...):
        인스턴스 변수 선언/초기화

    def method_name(self, param1, param2, ...):
        메소드 본문(body)
"""


# 클래스 정의
class Point:
    def __init__(self, x, y):  # initialize - 인스턴스 초기화
        # field, attribute, instance variable
        self.x = x
        self.y = y

    def info(self):
        print(f'Point ({self.x}, {self.y})')

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


if __name__ == '__main__':
    # 인스턴스(instance): 클래스 정의를 이용해 만들어진 객체(object)
    # 인스턴스 생성(instantiate): 변수 = 클래스이름()
    pt1 = Point(1, 2)
    print(type(pt1))  # 인스턴스 pt1의 데이터 타입
    print(id(pt1))  # 인스턴스 pt1의 메모리 주소
    pt1.info()
    pt1.x = 2
    pt1.info()

    pt2 = Point(0, 0)  # intantiate(인스턴스 생성)
    pt2.info()
    pt2.move(1, -1)
    pt2.info()

    origin = Point(0, 0)
    pt = Point(1, 1)
    dist = origin.distance(pt)
    print('distance =', dist)







