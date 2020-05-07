import random
import numpy as np
import matplotlib.pyplot as plt

# ndarray 생성 함수
# np.array(list/tuple/...): list/tuple 등을 ndarray 타입으로 변환
arr = np.array([[1, 2, 3],
                [4, 5, 6]])  # 2-d array
print('shape:', arr.shape)  # array의 모양(row, column, ...)
print('length:', len(arr))  # array의 길이
print('dtype:', arr.dtype)  # array의 원소들의 데이터 타입
print('size:', arr.size)

arr = np.array([1, 2, 3, 4, 5])  # 1-d array
print('shape:', arr.shape)
print('length:', len(arr))
print('size:', arr.size)

# python의 range()와 비슷한 기능
l = [x for x in range(1, 11, 2)]
print(l)

arr = np.arange(1, 11, 2)  # array using range
print(arr)

# np.arange()를 사용해서 2-d array 생성
arr = np.arange(6).reshape(2, 3)  # reshape((2, 3)) 가능
print(arr)

# np.zeros(): 모든 원소(element)들이 0인 array
arr = np.zeros(5, dtype=np.int)
print(arr)

arr = np.zeros((2, 2))
print(arr)

# np.ones(): 모든 원소들을 1로 채워줌.
print(np.ones(5))
print(np.ones((2, 3)))

# np.eye(), np.identity(): identity matrix
print(np.eye(2))
print(np.eye(3))

# random 모듈을 사용해서 list 생성
l = [random.random() for _ in range(5)]
print(l)

# np.random.함수를 사용한 n-d array 생성
# np.random.rand(*d0): 0 <= r < 1 uniform distribution
arr = np.random.rand(5)  # 1-d 5개의 난수를 갖는 array
print(arr)
arr = np.random.rand(2, 3)  # 2-d 2*3개의 난수를 갖는 array
print(arr)

# np.random.randn(*d): 표준정규분포를 따르는 난수 생성
print(np.random.randn(5))  # 1-d array
print(np.random.randn(2, 3))  # 2-d array

# np.random.randint(low, high, size): low <= r < high인 정수 난수
print(np.random.randint(1, 4, size=10))  # 1-d
print(np.random.randint(1, 4, size=(3, 3)))  # 2-d

# Python random 모듈을 사용해서
# 1 이상 10 이하의 정수 10개로 이루어진 1차원 리스트를 생성
numbers = [random.randint(1, 10) for _ in range(10)]
print(numbers)
# 위에서 생성한 리스트의 각 원소들이 짝수이면 True, 그렇지 않으면 False를
# 저장하는 리스트를 생성
# is_even = []  # True/False를 append할 리스트
# for n in numbers:
#     if n % 2 == 0:
#         is_even.append(True)
#     else:
#         is_even.append(False)
is_even = [True if n % 2 == 0 else False for n in numbers]
print(is_even)


# np.random 모듈을 사용해서
# 1 이상 10 이하의 정수 10개로 이루어진 1차원 ndarray를 생성
numbers = np.random.randint(1, 11, size=10)
print(numbers)
# boolean 1-d array를 생성
is_even = (numbers % 2 == 0)
print(is_even)

x = np.arange(-5, 5, 0.01)
y = x ** 2
plt.plot(x, y)
plt.show()



