# 직사각형, 원, 정사각형 -> 도형
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Shape(x={self.x}, y={self.y})'

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


# Circle IS-A Shape
class Circle(Shape):
    def __init__(self, r, x, y):
        Shape.__init__(self, x, y)  # 원의 중심 좌표
        # super().__init__(x, y)
        self.radius = r  # 원의 반지름

    def __repr__(self):
        return f'Circle(r={self.radius}, x={self.x}, y={self.y})'

    def area(self):
        return 3.14 * self.radius ** 2


# Rectangle IS-A Shape
class Rectangle(Shape):
    def __init__(self, w, h, x, y):
        Shape.__init__(self, x, y)  # 직사각형 기준점
        self.width = w  # 직사각형의 가로 길이(너비)
        self.height = h  # 직사각형의 세로 길이(높이)

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height}, x={self.x}, y={self.y})'

    def area(self):
        return self.width * self.height


# Square IS-A Rectangle
class Square(Rectangle):
    def __init__(self, side, x, y):
        Rectangle.__init__(self, side, side, x, y)

    def __repr__(self):
        return f'Square(side={self.width}, x={self.x}, y={self.y})'


if __name__ == '__main__':
    # Shape 클래스의 인스턴스 생성 -> 참조 변수에 저장
    shape = Shape(0, 0)
    print(shape)
    shape.move(1, -1)
    print(shape)

    c1 = Circle(10, 0, 0)
    print(c1)
    area = c1.area()
    print('c1 area =', area)

    c2 = Circle(1, 0, 0)
    print(c2)
    print('c2 area =', c2.area())

    rect1 = Rectangle(w=2, h=3, x=0, y=0)
    print(rect1)
    print('rect1 area =', rect1.area())

    rect2 = Rectangle(w=10, h=10, x=0, y=0)
    print(rect2)
    print('rect2 area =', rect2.area())

    square1 = Square(side=10, x=0, y=0)
    print(square1)
    print('square1 area =', square1.area())

    square1.move(1, 1)
    print(square1)


