"""
for 변수 in 리스트(튜플, 사전, 집합, 문자열, ...):
    반복해서 실행할 문장들

iterable 객체: list, tuple, set, dict, str, range, ...
"""

for x in range(5):  # (0, 1, 2, 3, 4), 0 <= x < 5
    print(x, end=' ')
print()

for x in range(1, 6):  # 1 <= x < 6
    print(x, end=' ')
print()

for x in range(0, 10, 2):
    print(x, end=' ')
print()

print('-' * 20)

# for문을 사용해서 구구단 2을 출력: 2x1, 2x2, ..., 2x8, 2x9
for x in range(1, 10):  # 1 <= x < 10
    print(f'2 x {x} = {2 * x}')
    # print('2 x', x, '=', 2*x)

# 구구단 2단부터 9단까지 출력
for dan in range(2, 10):
    for x in range(1, 10):
        print(f'{dan} x {x} = {dan * x}')
    print('-' * 20)

# 아래의 4줄을 출력하는 코드를 작성하세요.
# 1 little 2 little 3 little indian
# 4 little 5 little 6 little indian
# 7 little 8 little 9 little indian
# 10 little indian boys!
for n in range(1, 11):  # 1 <= n < 11
    print(f'{n} little', end=' ')
    if n % 3 == 0:
        print('indian')
    if n == 10:
        print('indian boys!')

# 369 게임
# 1 ~ 100 옆으로 출력
# 10, 20, 30, ... 다음에서 줄바꿈
# 숫자 중에 3, 6, 9가 포함된 경우에는 숫자 대신 '*' 출력
# 1 2 * 4 5 * 7 8 * 10
# 11 12 * 14 15 * 17 18 * 20
# ...
# * * * * * * * * * 100
for x in range(1, 101):  # 1 <= x <= 100
    n1 = x % 10  # x의 1의 자릿수 = 10으로 나눈 나머지
    n10 = x // 10  # x의 10의 자릿수 = 10으로 나눈 몫
    # 1의 자릿수가 3 또는 6 또는 9이면
    cond1 = n1 in (3, 6, 9)  # (n1 == 3) or (n1 == 6) or (n1 == 9)
    # 10의 자릿수가 3 또는 6 또는 9이면
    cond2 = n10 in (3, 6, 9)  # (n10 == 3) or (n10 == 6) or (n10 == 9)
    if cond1 or cond2:
        print('*', end=' ')
    else:
        print(x, end=' ')
    if n1 == 0:
        print()
