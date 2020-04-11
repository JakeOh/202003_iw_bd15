"""
while 반복문:
(초기화 문장)
while 조건식:
    조건식이 참인 동안에 실행할 문장들
    (조건식의 내용을 변경할 수 있는 문장)
"""

# 구구단 2단: 2 x 1, 2 x 2, 2 x 3, ...,  2 x 9
n = 1
while n < 10:
    print(f'2 x {n} = {2 * n}')
    n += 1  # n = n + 1

# while 문을 이용해서 구구단 2단 ~ 9단까지 출력
dan = 2
while dan < 10:
    n = 1
    while n < 10:
        print(f'{dan} x {n} = {dan * n}')
        if dan == n:
            break
        n += 1
    print('-' * 20)
    dan += 1
