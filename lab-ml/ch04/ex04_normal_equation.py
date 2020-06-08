import matplotlib.pyplot as plt
import numpy as np


def line(x, theta0, theta1):
    # y = (y절편) + (기울기) * x
    return theta0 + theta1 * x


if __name__ == '__main__':
    np.random.seed(1)
    # 대문자 변수 -> 2차원 행렬(배열), 소문자 변수 -> 스칼라, 열 벡터
    x = 3 * np.random.rand(100, 1)  # 0 <= x < 3인 숫자들로 이루어진 (100,1) 행렬
    y = 4 + 3 * x + np.random.randn(100, 1)

    plt.scatter(x, y)
    plt.show()

    # y ~ theta0 + theta1 * x 선형 관계식을 만족하는
    # 최적의 theta0와 theta1은 무엇일까?
    X = np.c_[np.ones((100, 1)), x]  # (100, 2)
    w = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    print(w)

    x_pts = np.linspace(0, 3, 100)  # 0 <= x <= 3인 구간을 균등하게 100개로 나눔.
    y_pts = line(x_pts, w[0, 0], w[1, 0])
    plt.scatter(x, y)
    plt.plot(x_pts, y_pts, color='red')
    plt.show()
