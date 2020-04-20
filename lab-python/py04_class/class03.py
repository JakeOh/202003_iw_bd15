# 클래스 = 데이터 + 기능
class Contact:
    # class 변수(모든 인스턴스가 공유하는 변수) 선언/초기화
    num_of_contacts = 0

    def __init__(self, name, phone, email):
        # instance 변수들을 초기화(initialization)
        self.name = name
        self.phone = phone
        self.email = email

        Contact.num_of_contacts += 1  # 클래스 변수 값 변경

    def show(self):
        print(f'Contact(name: {self.name}, phone: {self.phone}, email: {self.email})')

    def update(self, phone):
        self.phone = phone


if __name__ == '__main__':
    print(Contact.num_of_contacts)
    # 클래스 변수들은 인스턴스 생성 전에도 접근 가능함.
    # ClassName.class_var 형식으로 사용.

    # Contact 클래스의 인스턴스 생성
    contact1 = Contact('오쌤', '010-1234-5678', 'jake@itwill.co.kr')
    # 인스턴스의 기능 사용 - 메서드 호출
    contact1.show()
    print(contact1.email)
    print(Contact.num_of_contacts)

    contact2 = Contact('홍길동', '02-1111-2222', 'hgd@yuldo.com')
    contact2.show()
    print(Contact.num_of_contacts)

    contact2.update('010-1122-3344')
    contact2.show()
