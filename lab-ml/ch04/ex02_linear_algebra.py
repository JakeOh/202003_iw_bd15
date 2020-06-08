import numpy as np

X = np.array([[1, 2, 3],
              [4, 5, 6]])
print(X)  # 2x3 행렬

# Transpose(전치행렬): 행과 열을 바꾼 행렬
print(X.T)  # 3x2 행렬

print()
X = np.array([[1, 2, 3]])
print(X)  # 1x3 행렬 - 행 벡터(row vector)
print(X.T)  # 3x1 행렬 - 열 벡터(column vector)

# 항등 행렬: I @ X = X @ I = X를 만족하는 행렬 I
# 역행렬: Y @ X = X @ Y = I를 만족하는 행렬 Y를 행렬 X의 역행렬
X = np.array([[1, 2],
              [3, 4]])
X_inv = np.linalg.inv(X)
print(X_inv)
print(X_inv.dot(X))  # Y @ X = I
print(X.dot(X_inv))  # X @ Y = I

# 행렬 dot product: X @ Y
# dot product(내적)가 계산되려면, X의 컬럼 개수와 Y의 row 개수가 같아야 함!
# X가 n x m 크기의 행렬이고 Y가 m x l 크기의 행렬일 때,
# X @ Y는 n x l 크기의 행렬이 됨.

A = np.array([[1, 2, 3],
              [4, 5, 6]])  # 2x3
B = np.array([[1, 2],
              [3, 4],
              [5, 6]])  # 3x2
# A @ B: (2,3) @ (3,2) = (2,2)
# B @ A: (3,2) @ (2,3) = (3,3)
# 행렬의 내적은 교환 법칙이 성립하지 않는다.
print(A.dot(B))
print(B.dot(A))

# np.dot(A, B) == A.dot(B) == A @ B
# np.dot(B, A) == B.dot(A) == B @ A
