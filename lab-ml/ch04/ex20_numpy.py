import numpy as np
from sklearn import datasets

a = np.array([1, 2, 3])
print(a)  # 1D array
print(a.shape)  # (3,)

b = np.array([2, 2, 2])

result = a @ b  # 1x2 + 2x2 + 3x2 = 12
# (3,) @ (3,) = (,3) @ (3,) = scalar
print(result)  # scalar
# 1D array @ 1D array = scalar

# @ 연산이 가능하려면 두 1D array의 len이 같아야 함!
# c = np.array([2, 2])  # (2,)
# result = a @ c

# 1D array와 2D array 간의 dot product?
a = np.array([1, 2, 3])  # (3,)
b = np.array([[2, 2, 2]])  # (1,3)
print(b.shape)
# result = a @ b  # (3,) @ (1,3): error
result = b @ a  # (1,3) @ (3,) = (1,): 1D array
print(result)

# 2D array @ 2D array
a = np.array([[1, 2, 3]])
print(a, a.shape)  # (1,3)
b = np.array([[2],
              [2],
              [2]])
print(b, b.shape)  # (3,1)
result = a @ b  # (1,3) @ (3,1) = (1,1): 2D array
print(result)

result = b @ a  # (3,1) @ (1,3) = (3,3): 2D array
print(result)

print('\n', '*' * 30, '\n')

iris = datasets.load_iris()
X, y = iris['data'], iris['target']
print(X.shape, y.shape)
# y = X @ theta
# (150,) = (150,4) @ (4,)
# y = theta @ X.T
# (,150) = (,4) @ (4,150)

# 선형 회귀의 정규 방정식(Normal Equation)
# (X.T @ X)^-1 @ X.T @ y
# X.T @ X = (4,150) @ (150,4) = (4,4)
# (X.T @ X)^-1 @ X.T = (4,4) @ (4,150) = (4,150)
# (X.T @ X)^-1 @ X.T @ y = (4,150) @ (150,) = (4,)

print('\n', '*' * 30, '\n')

X = np.arange(40).reshape((10, 4))  # (10,4)
print(X)
w = np.arange(1, 5)  # (4,)
print(w, w.shape)
result = X @ w  # (10,4) @ (4,) = (10,)
print(result, result.shape)
result = w @ X.T  # (4,) @ (4,10) = (,4) @ (4,10) = (,10) = (10,)
print(result, result.shape)

W = np.array([[1, 2, 3, 4]])
print(W, W.shape)  # (1,4)  2D array
result = X @ W.T  # (10,4) @ (4,1) = (10,1): 2D array
print(result)
result = W @ X.T  # (1,4) @ (4,10) = (1,10): 2D array
print(result)

print('\n', '*' * 30, '\n')
X = np.arange(12).reshape((3, 4))
print(X)
y = np.array([1, 2, 3, 4])
print(y)  # (4,)
result = X - y
print(result)

X = np.array([[1], [2], [3]])  # (3,1) shape
y = np.array([1, 2, 3, 4])  # (4,) shape
result = X - y
# X와 y 모두 broadcast
print(result)  # (3,4) shape

X = np.arange(12).reshape((3, 4))
w = np.arange(4)
y = np.array([1, 1, 1])
result = X @ w - y  # (3,4) @ (4,) - (3,) = (3,)
print(result)

X = np.arange(12).reshape((3, 4))
W = np.arange(4).reshape((4, 1))
y = np.array([1, 1, 1])
result = X @ W - y  # (3,4) @ (4,1) - (3,) = (3,1) - (3,) = (3,3)
print(result)
