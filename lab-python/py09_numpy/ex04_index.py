import numpy as np

a = np.arange(0, 11, 2)
print(a)
# numpy.ndarray의 인덱스는 리스트와 마찬가지로 0부터 시작
# 마지막 인덱스는 len - 1
print(a[2], a[-4])
print(a[1:4])
# 범위 연산자(start:end)
#   start를 지정하지 않은 경우, 기본값은 0
#   end를 지정하지 않은 경우, 기본값은 array의 마지막 원소까지
print(a[0:3], a[:3])
print(a[4:6], a[4:], a[-2:])

# 인덱스 연산자([]) 안에 인덱스들의 리스트를 줄 수 있음
print(a[[0, 4, 5]])

# boolean indexing
indexer = [True, False, False, False, True, True]
print(a[indexer])

# 10 이하의 정수 난수 10개로 이루어진 array를 생성
numbers = np.random.randint(1, 10, size=10)
print(numbers)
# 위에서 만든 array에서 짝수들로만 이루어진 부분집합(array)를 생성
evens = numbers[numbers % 2 == 0]
print(evens)

# boolean indexing에서는 Python의 and, or, not 키워드를 사용할 수 없음!
# 대신에 &, |, ~ 연산자를 사용하고, 연산 순서를 명시하기 위해서 ()를 반드시 사용.
# numbers에서 2이상 7이하인 숫자들로 이루어진 부분집합(array)
subset = numbers[(numbers >= 2) & (numbers <= 7)]
print(subset)

a = np.arange(32).reshape((8, 4))
print(a)
# 2-d array: [x, y] 두개의 인덱스
print(a[0][0])  # Python의 list에서 인덱스를 사용하는 방식. numpy에서도 가능.
print(a[0, 0])  # NumPy.ndarray에서 인덱스를 사용하는 방식. list는 사용 못함.
print(a[:3])  # row 선택
print(a[:3, :2])  # row, column 선택
print(a[[0, 1], [1, 2]])
# a[0, 1]과 a[1, 2] 두개의 원소로 이루어진 1-d array를 만들어줌.

# boolean indexing
print(a[a % 2 == 0])
