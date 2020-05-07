import numpy as np

a = np.arange(1, 5).reshape((2, 2))
print(a)
b = np.ones(shape=(2, 2), dtype=np.int)
print(b)

# 행렬의 덧셈/뺄셈: 인덱스가 같은 원소들끼리 덧셈/뺄셈
print(a + b)
print(a - b)

# 행렬의 스칼라 곱(scalar multiply)
# print(a * 2)
print(2 * a)

# 2-d array 간의 곱셈/나눗셈: 같은 인덱스에 있는 원소들끼리 계산.
print(a * b)
print(b / a)

# 행렬의 내적(inner product, dot product)
print(a @ b)
print(b @ a)  # 행렬의 내적은 교환법칙이 성립하지 않는다(a @ b != b @ a)
# a @ b, np.dot(a, b), a.dot(b)

# 임의의 행렬 A에 대해서, A @ I = I @ A = A를 만족하는 행렬 I를
# 항등 행렬(identity matrix)이라고 함.
i = np.eye(2, dtype=np.int)  # np.identity(2)
print(i)
print(a @ i)
print(i @ a)

# 임의의 행렬 A에 대해서, A @ B = B @ A = I를 만족하는 행렬 B를
# A의 역행렬(inverse matrix)라고 함.
a_inverse = np.linalg.inv(a)
print(a_inverse)
print(a @ a_inverse)
print(a_inverse @ a)

# NumPy.linalg를 사용한 연립 방정식의 해(solution) 찾기
a = np.array([[3, 1],
              [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(a, b)  # a @ x = b를 만족하는 x를 찾음.
print(x)

a_inverse = np.linalg.inv(a)
print(a_inverse @ b)  # x = a_inv @ b

# 전치 행렬(transpose matrix): 행렬의 행과 열을 서로 바꾼 행렬
a = np.arange(4).reshape((2, 2))
print(a)
print(a.T)
