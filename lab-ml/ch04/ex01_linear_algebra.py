import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.array([[1], [2], [3]])
    print(x)

    y = np.array([[3], [5], [7]])
    print(y)

    print(2 * x + 1)  # y = 2 * x + 1

    x_b = np.c_[np.ones((3, 1)), x]
    print(x_b)

    w = np.array([[1], [2]])
    print(w)

    print(x_b.dot(w))  # y = x_b @ w

    # 정규 방정식(Normal Equation):
    w_best = np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(y)
    print(w_best)



