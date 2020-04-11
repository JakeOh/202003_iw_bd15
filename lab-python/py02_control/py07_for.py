import random  # 난수를 사용하기 위해서

# 2차원 리스트: 1차원 리스트를 원소로 갖는 리스트
numbers = [[1, 2, 3],
           [3, 4],
           [5, 6, 7, 8]]
print(numbers)
print(numbers[0][0])

# numbers를 3x2 형태로 출력
"""
1 2
3 4
5 6
"""
for row in numbers:
    for x in row:
        print(x, end=' ')
    print()  # 줄바꿈(new line)

print('length of numbers =', len(numbers))
print('length of row =', len(numbers[2]))
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print(numbers[i][j], end=' ')
    print()

# 15개의 난수(random number)로 이루어진
# 5 rows x 3 columns 모양의 2차원 리스트를 생성하고 출력
# append() 이용
# list comprehension을 이용
# random.random(): 0 <= r < 1
# random.randint(a, b): a <= r <= b 정수

# empty list 생성
random_numbers = []  # random_numbers = list()
for _ in range(5):
    row = []  # row에 추가할 리스트
    for _ in range(3):  # row에 난수를 3번 추가
        row.append(random.randint(0, 10))
    # 난수 3개를 갖는 리스트를 random_numbers에 추가
    random_numbers.append(row)

print(random_numbers)

rand_nums = [[random.randint(0, 10) for _ in range(3)]
             for _ in range(5)]
for row in rand_nums:
    for x in row:
        print(x, end=' ')
    print()


# 정수 난수(0 ~ 10) 10개를 원소로 갖는 리스트를 생성
rand_ints = [random.randint(0, 10) for _ in range(10)]
print(rand_ints)
# rand_ints 중에서 5 이상인 숫자들로만 이루어진 리스트를 생성
ints_ge5 = []
for x in rand_ints:
    if x >= 5:
        ints_ge5.append(x)
print(ints_ge5)

nums = [x for x in rand_ints if x >= 5]
print(nums)

integers = [-3, -2, -1, 0, 1, 2, 3]
# integers의 원소들의 제곱값들로 이루어진 리스트
squares = []
for x in integers:
    squares.append(x ** 2)
print(squares)

squares = [x ** 2 for x in integers]
print(squares)

# dictionary comprehension
languages = ['Python', 'R', 'Java', 'C', 'SQL']
lengths = dict()  # language: length
for lang in languages:
    lengths[lang] = len(lang)
print(lengths)

lengths = {k: len(k) for k in languages}
print(lengths)
