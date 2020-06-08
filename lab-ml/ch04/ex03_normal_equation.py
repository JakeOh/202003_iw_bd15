import numpy as np

X = np.array([[1, 4],
              [2, 5],
              [3, 6]])  # (3, 2)
print(X)

# bias를 포함한 X
X_b = np.c_[np.ones((3, 1)), X]
print(X_b)

y = np.array([[18],
              [23],
              [28]])  # (3, 1)
print(y)

# W = [[theta0], [theta1], [theta2]]
# W = INV(X.T @ X) @ X.T @ y
W = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y
print(W)

print(X_b @ W)

W2 = np.array([[2],
               [3],
               [1]])
print(X_b @ W2)  # X_b @ W2 = y

print(X_b.T)
print(X_b.T @ X_b)
print(np.linalg.inv(X_b.T @ X_b))



