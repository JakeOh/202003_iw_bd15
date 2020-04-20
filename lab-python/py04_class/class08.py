class MyPoint:
    # 2-D 평면 위의 점: (x, y)
    # __init__, __repr__, __eq__, __ne__
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, MyPoint):
            # other가 MyPoint 클래스의 인스턴스이면
            return (self.x == other.x) and (self.y == other.y)
        else:  # other가 MyPoint 클래스의 인스턴스가 아니면
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        if isinstance(other, MyPoint):
            self.x += other.x
            self.y += other.y
            return self
        else:
            raise ValueError('other는 MyPoint 타입이어야 함!')


if __name__ == '__main__':
    pt1 = MyPoint(1, 2)  # reference_var = instance 생성(__init__)
    pt2 = MyPoint(1, 2)
    print(pt1, id(pt1))  # __repr__
    print(pt2, id(pt2))

    print(pt1 == pt2)  # pt1.__eq__(pt2)
    print(pt1 != pt2)  # pt1.__ne__(pt2)

    print(pt1 + pt2)  # pt1.__add__(pt2)

    print([1, 2, 3] + [4, 5])
    # list 클래스에서 __add__ 메소드가 정의되어 있기 때문에 + 연산이 가능함.
