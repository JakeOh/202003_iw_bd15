class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'안녕하세요, 저는 {self.name}입니다.')


# 회사원(BusinessPerson)은 사람(Person)입니다.
class BusinessPerson(Person):
    # Child class에서 __init__ 메소드를 작성하지 않으면,
    # Parent class의 __init__ 메소드를 자동으로 호출해줌.
    # Child class에서 __init__을 작성하면,
    # Parent class의 __init__ 메소드를 자동으로 호출하지 않음!
    # Parent class의 __init__ 메소드를 명시적으로 호출해야 함.
    # Child class에서 Parenet class의 메소드를 명시적으로 호출할 때는
    # super().method_name(arg, ...) 형식으로 호출함.
    # 또는, ClassName.method_name(self, arg, ...) 형식으로 호출
    def __init__(self, name, company):
        Person.__init__(self, name)
        # super().__init__(name)
        self.company = company

    # 메소드 override:
    # 부모 클래스의 메소드를 자식 클래스에서 덮어쓰는 것(재정의).
    def say_hello(self):
        # print(f'안녕하세요, {self.company}의 {self.name}입니다.')
        super().say_hello()
        # Person.say_hello(self)
        print(f'저는 {self.company}에서 일합니다.')


if __name__ == '__main__':
    person = Person('오쌤')
    person.say_hello()

    person2 = BusinessPerson('홍길동', '율도국')
    person2.say_hello()



"""
method override vs method overload
1) method override:
    상속이 전제되어야 함.
    Super(Parent) 클래스의 메소드를 Sub(Child) 클래스에서 같은 이름으로 재정의.
2) method overload:
    argument의 개수 또는 타입이 다른 여러개의 메소드를 같은 이름으로 작성하는 것.
    Python은 method overload를 제공하지 않음.
    대신에 default argument를 사용함.
"""
def fn_test(p1=0, p2=0, p3=0):
    pass

fn_test()
fn_test(1)
fn_test(1, 2)
fn_test(1, 2, 3)






