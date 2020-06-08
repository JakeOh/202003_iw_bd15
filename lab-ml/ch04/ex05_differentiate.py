import matplotlib.pyplot as plt
import numpy as np


def square(x):
    return x ** 2   # y = x ** 2


def derivative(f, x, h=0.0001):
    return (f(x + h) - f(x)) / h


def tangent(x, slope, x1, y1):
    return y1 + slope * (x - x1)  # y = y1 + a(x - x1)


if __name__ == '__main__':
    # -5 <= x <= 5 구간을 균등하게 1000개로 나눔.
    x_pts = np.linspace(-5, 5, 1000)
    y_pts = square(x_pts)

    x = np.array([1, 4])
    y = square(x)  # [1, 16]
    # 직선의 기울기 = (y의 증가분)/(x의 증가분) = (16 - 1)/(4 - 1)

    plt.plot(x_pts, y_pts)
    plt.plot(x, y, color='red')
    plt.show()

    y_derivatives = derivative(square, x_pts)
    plt.plot(x_pts, y_derivatives)
    plt.show()

    plt.plot(x_pts, y_pts)  # y = x**2
    x = np.linspace(0, 5, 100)
    for x1 in range(0, 5):
        y = tangent(x, derivative(square, x1), x1, square(x1))
        plt.plot(x, y)
    plt.show()
