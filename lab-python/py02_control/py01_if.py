"""
if 조건식:
    조건식이 참일 때 실행할 문장들
"""

x = -10
if x > 0:
    print('x는 양수')

print('if 종료')

"""
if 조건식:
    조건식이 참일 때 실행할 문장들
else:
    조건식이 거짓일 때 실행할 문장들
"""

x = 123
if x % 2 == 0:
    print('even number')
else:
    print('odd number')

"""
if condition1:
    condition1이 참일 때 실행할 문장들
elif condition2:
    condition2이 참일 때 실행할 문장들
else:
    위의 모든 조건들이 거짓을 때 실행할 문장들
"""

x = -100
if x > 0:
    print(f'{x} is positive.')
elif x < 0:
    print(f'{x} is negative.')
else:
    print('zero')


if x == 0:
    print('zero...')
else:
    if x > 0:
        print('양수...')
    else:
        print('음수...')

"""
Python에서 True/False 판별 기준
1) ==, !=, >=, >, <, <=, is, is not
2) 숫자 타입의 변수인 경우, 0은 False, 0 이외의 숫자들은 True 취급.
3) list와 같이 여러개의 원소들을 가질 수 있는 데이터 타입인 경우,
비어 있으면(empty) False, 비어있지 않으면 True 취급 
"""

x = 3
if x % 2:  # x를 2로 나눈 나머지가 있다면
    print('홀수')
else:      # x를 2로 나눈 나머지가 없다면
    print('짝수')
