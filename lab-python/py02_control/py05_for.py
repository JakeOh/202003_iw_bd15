"""
반복문(for, while) 안에서
    break: iteration을 종료(반복문을 종료)
    continue: 그 다음 iteration을 수행함.
"""

for x in range(5):
    if x == 3:
        break
    print(x)

print('-' * 20)

for x in range(5):
    if x == 3:
        continue
    print(x)

print('-' * 20)
# 구구단 2단은 2x2, 3단은 3x3, ... 9단은 9x9까지 출력
for dan in range(2, 10):
    for x in range(1, 10):
        print(f'{dan} x {x} = {dan * x}')
        if dan == x:
            break
    print('-' * 20)
