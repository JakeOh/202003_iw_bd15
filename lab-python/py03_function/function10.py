"""
Python에서 함수(function)는 1급 객체(fisrt-class object):
- 함수를 변수에 저장할 수 있음.
- 함수의 argument로 다른 함수를 전달할 수 있음.
- 함수가 다른 함수를 반환(return)할 수 있음.
- 함수 내부에서 다른 함수를 정의할 수 있음.
"""


def twice(x):
    return 2 * x


print(twice(3))
print(twice)
print(type(twice))

double = twice  # twice 함수를 double 변수에 저장
print(double, type(double))
print(double(100))  # 변수 double을 함수 이름으로 사용해서 호출할 수 있음.


def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def calculator(x, y, operation):
    return operation(x, y)

print(calculator(1, 2, plus))
print(calculator(1, 2, minus))




