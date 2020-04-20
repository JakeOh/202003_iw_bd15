"""
상속(inheritance)
Super class(상위 클래스), Parent class(부모 클래스), Base class(기본 클래스)
Sub class(하위 클래스), Child class(자식 클래스), Derived class(유도 클래스)
부모 클래스의 속성(attribute) 또는 기능(method) 코드들을
자식 클래스에서 재활용(reuse)하는 것.
IS-A 관계일 때 상속을 사용함.
    학생은 사람이다. (Student IS-A Person)
"""


class Parent:
    def __init__(self):
        self.money = 10000  # attribute, field, instance variable

    def get_money(self):  # 기능(method)
        return self.money


# class ChildClass(ParentClass)
class Child(Parent):  # Child가 Parent를 상속함
    def spend_money(self):
        print(self.money, '원을 다 써버립니다...')


if __name__ == '__main__':
    p = Parent()
    print(p.get_money())

    c = Child()  # Child 클래스의 인스턴스 생성
    print(c.get_money())
    c.spend_money()





