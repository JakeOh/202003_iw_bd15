class MyNumber:
    def __init__(self, x=0):  # initialization
        self.x = x

    def __repr__(self):  # representation
        # 객체의 내용을 콘솔에 출력할 때 사용됨 - e.g print(num)
        # 반드시 문자열을 리턴!
        return f'MyNumber({self.x})'

    # def __str__(self):  # string
    #     return f'MyNumber={self.x}'

    def __eq__(self, other):  # equal to
        # ==(비교 연산자)는 원래 인스턴스의 id(주소값)을 비교함.
        # 인스턴스의 주소값을 비교하지 않고, 데이터(속성)을 비교해서
        # 같은지(True) 다른지(False)를 리턴하고자 할 때 사용.
        # 반드시 논릿값(True/False)를 리턴!
        if isinstance(other, MyNumber):
            return self.x == other.x
        else:
            return False

    # 객체 비교에 사용되는 predefined methods:
    # __ge__: greater than or equal to(>=)
    # __gt__: greater than(>)
    # __le__: less than or equal to(<=)
    # __lt__: less than(<)
    # __ne__: not equal to(!=)


if __name__ == '__main__':
    num1 = MyNumber()
    print('type:', type(num1))
    print('num1:', num1)  # __repr__ 메소드 작성하기 전/후 결과를 비교

    numbers = [MyNumber(0), MyNumber(1), MyNumber(2)]
    print(numbers)

    print('id:', id(num1))

    numbers1 = list([1, 2, 3])
    numbers2 = list([1, 2, 3])
    print(numbers1, id(numbers1))
    print(numbers2, id(numbers2))
    print(numbers1 == numbers2)

    num1 = MyNumber(123)
    num2 = MyNumber(123)
    print(num1, id(num1))
    print(num2, id(num2))
    print(num1 == num2)  # __eq__ 메소드를 작성하기 전/후 결과 비교
