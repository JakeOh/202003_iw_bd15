import random

# 1) 1 + 2 + 3 + ... + 99 + 100의 결과를 출력하는 코드를 작성하세요.
total = 0
for x in range(1, 101):
    total += x  # total = total + x
print(f'total = {total}')


# 2) 1 + 2 + 3 + ... + x >= 100 을 만족하는 가장 작은 x를 찾는 코드를 작성하세요.
total = 0  # 합계를 저장할 변수
x = 1  # 1씩 증가시키면서 더해갈 변수
while True:  # 무한 루프
    total += x
    if total >= 100: # 총합이 100 이상이 되면
        break  # 무한 루프를 종료
    x += 1  # x의 값을 1 증가
print(f'x = {x}, total = {total}')

total = 0
x = 0
while total <= 100:
    x += 1
    total += x
print(f'x = {x}, total = {total}')


# 3) Fibonacci Sequence(피보나치 수열)
fibo = [0, 1]  # fibo[0] = 0, fibo[1] = 1
for n in range(2, 20):
    fn = fibo[n - 1] + fibo[n - 2]  # f[n] = f[n-1] + f[n-2], n>=2
    fibo.append(fn)
print(fibo)


# 4) 주사위 2개를 던졌을 때 가능한 모든 경우의 수 (x, y)
dice = [(x, y) for x in range(1, 7) for y in range(1, 7)]
print(dice)

dice = []  # empty list
for x in range(1, 7):  # 첫번째 주사위가 가질 수 있는 경우의 수
    for y in range(1, 7):  # 두번째 주사위가 가질 수 있는 경우의 수
        dice.append((x, y))  # (x, y) 튜플을 리스트에 추가
print(dice)


# 5) 주사위 2개를 던졌을 때, 두 눈의 합이 6이상이 될 확률
dice_ge6 = [(x, y) for x, y in dice if x + y >= 6]
# dice_ge6 = [(x, y) for x in range(1, 7)
#             for y in range(1, 7) if x + y >= 6]
print(dice_ge6)
print('probability =', len(dice_ge6) / len(dice))

dice_ge6 = []
for x, y in dice:
    if x + y >= 6:
        dice_ge6.append((x, y))
print(dice_ge6)


# 6) 주사위 1개를 2번 던졌을 때, 처음 나온 숫자가 두번째 나온 숫자보다 클 확률
dice2 = [(x, y) for x, y in dice if x > y]
print(dice2)
print('probability =', len(dice2) / len(dice))


# 7) 0 이상 10 이하의 점수 10개를 가지고 있는 리스트에서,
# 10개 값의 평균 이상인 점수들로 이루어진 리스트를 새로 생성하고 출력
scores = [random.randint(0, 10) for _ in range(10)]
print(scores)
mu = sum(scores) / len(scores)  # 평균 = 합계 / 개수
print('평균 =', mu)
above_average = [x for x in scores if x >= mu]
print(above_average)


# 8) numbers: names 짝으로 이루어진 dict
numbers = [1, 2, 3, 4, 5]
names = ['a', 'b', 'c', 'd', 'e']
num_names = {}  # empty dict
for i in range(len(numbers)):
    num_names[numbers[i]] = names[i]  # dict에 key-value 저장
print(num_names)

num_names = {numbers[i]: names[i] for i in range(len(numbers))}
print(num_names)

num_names = {num: name for num, name in zip(numbers, names)}
print(num_names)


# 9)
colors = ['white', 'black']
sizes = ['S', 'M', 'L']
tshrits = []  # empty list
for color in colors:
    for size in sizes:
        tshrits.append((color, size))
print(tshrits)

tshrits = [(color, size) for color in colors for size in sizes]
print(tshrits)


# 10)
pants = []
for size in sizes:
    for color in colors:
        pants.append((color, size))
print(pants)

pants = [(color, size) for size in sizes for color in colors]
print(pants)
