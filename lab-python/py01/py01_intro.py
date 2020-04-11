"""
multi-line comment
스크립트 설명, 함수 설명, ...
"""

print('Hello, Python!')
# Ctrl + Shift + F10: 현재 스크립트 실행

print('안녕', '파이썬')
print('1 + 1 =', (1 + 1))

x = 10  # 변수 x에 값 10을 할당(assignment)
y = 20
print('x =', x, ', y =', y)
print('x = {}, y = {}, x + y = {}'.format(x, y, x+y))
print(f'x = {x}, y = {y}, x + y = {x+y}')
# formatted string(f'...')은 Python 3.6 버전 이상에서
# 지원됨.

# 연산자(operator)
print(10 / 3)   # /: 나눗셈 연산자(실수 연산)
print(10 // 3)  # //: 나눈 몫
print(10 % 3)   # %: 나눈 나머지
print(2 ** 3)   # ** 거듭제곱

print(1 == 1.0)
print(1 is 1.0)
print(type(1), type(1.0))
# == (equal to), != (not equal to): 값만 비교
# is, is not: 값과 타입을 함께 비교
