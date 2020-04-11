import random
import math

# 0 ~ 10의 정수 난수 10개를 저장하는 scores 리스트 생성
scores = [random.randint(0, 10) for _ in range(10)]
print(scores)

# scores의 총합(total)을 계산, 출력
total = 0
for score in scores:
    total += score
print(f'total = {total}')

# scores의 평균을 계산, 출력
average = total / len(scores)
print(f'average = {average}')

# scores의 분산을 계산, 출력
sum_of_squares = 0
for score in scores:
    sum_of_squares += (score - average) ** 2
variance = sum_of_squares / (len(scores) - 1)
print(f'variance = {variance}')

# scores의 표준편차를 계산, 출력: import math -> math.sqrt() 이용
std_dev = math.sqrt(variance)
print(f'standard deviation = {std_dev}')

# scores의 최댓값, 최솟값 찾아서 출력
max = scores[0]
min = scores[0]
for score in scores:  # 리스트의 모든 원소들을 반복하면서
    if score > max:  # 리스트의 한 원소가 max보다 크다면
        max = score  # max의 값을 더 큰 값으로 변경
    if score < min:  # 리스트의 원소가 min보다 작다면
        min = score  # min의 값을 더 작은 값으로 변경

print(f'max = {max}, min = {min}')
