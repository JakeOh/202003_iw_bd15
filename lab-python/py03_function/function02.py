"""
함수 정의(선언)
def function_name(param1, param2, ...):
    함수 기능 작성
    [return 값]
"""


# 함수 정의(선언)
def say_hello():
    """
    '안녕하세요'를 출력하는 함수
    :return: None
    """
    print('안녕하세요')


say_hello()  # 함수 호출


def subtract(x, y):
    """
    두 숫자의 차이 x - y를 리턴.

    :param x: 숫자
    :param y: 숫자
    :return: x - y
    """
    return x - y


result = subtract(1, 2)
print('result =', result)


# 두 개 이상의 값을 반환(return)하는 함수
def plus_and_product(x, y):
    """
    두 숫자의 합과 곱을 리턴.

    :param x: 숫자
    :param y: 숫자
    :return: x + y, x * y
    """
    return x + y, x * y


plus, product = plus_and_product(2, 3)
print(plus, product)


# default argument를 갖는 함수
# default arguement: 함수를 정의(선언)할 때, parameter의 기본값을 설정.
def repeat_message(msg, repeat=1):
    """
    msg를 repeat 횟수만큼 반복해서 출력.

    :param msg: str. 출력할 메시지.
    :param repeat: int. 메시지를 반복할 횟수
    :return: None
    """
    print(msg * repeat)


repeat_message('Hello')
repeat_message('Hello', 5)
repeat_message('졸리세요?', 10)


# (주의): Python 함수를 정의할 때, default argument를 갖는 파라미터들은
# default 값이 없는 파라미터들 뒤에 선언해야만 함!
# def test(x=1, y):
#     return x + y
# 기본값이 없는 파라미터 y가 기본값이 있는 파라미터 x 뒤에 올 수 없다.

