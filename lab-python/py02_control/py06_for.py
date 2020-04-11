import random

scores = [99, 20, 100, 40, 50]

# scores의 모든 점수들의 합
s = 0
for x in scores:
    s += x  # s = s + x
print(f'sum = {s}')

# scores 평균
average = s / len(scores)
print(f'mean = {average}')

print(sum(scores))

# list comprehension
# 빈 리스트(empty list)를 생성하고,
# 0 ~ 10 사이의 난수를 10개를 만들어서 저장
scores = []  # empty list
for _ in range(10):
    scores.append(random.randint(0, 10))
print(scores)

scores2 = [random.randint(0, 10) for _ in range(10)]
print(scores2)

# 0 ~ 9 숫자들이 차례대로 저장된 리스트를 생성
# numbers = []
# for x in range(10):
#     numbers.append(x)
numbers = [x for x in range(10)]
print(numbers)

# 1 이상 100 이하의 홀수들이 차례로 저장된 리스트 odds를 만들고 출력
# odds = []
# for x in range(1, 101, 2):
#     odds.append(x)
odds = [x for x in range(1, 101, 2)]
print(odds)

# odds = []
# for x in range(1, 101):
#     if x % 2:  # 2로 나눈 나머지가 있으면
#         odds.append(x)
odds = [x for x in range(1, 101) if x % 2]
print(odds)
