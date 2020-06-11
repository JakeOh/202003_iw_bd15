import matplotlib.pyplot as plt
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


if __name__ == '__main__':
    # -10 <= x <= 10 구간을 동일한 간격으로 1000개로 나눔
    x = np.linspace(-10, 10, 1_000)
    y = sigmoid(x)

    plt.plot(x, y)
    plt.hlines(y=[0, 0.5, 1], xmin=-10, xmax=10, linestyles='dotted')
    plt.vlines(x=[-10, 0, 10], ymin=0, ymax=1, linestyles='dotted')
    plt.show()

    p = np.linspace(0, 1, 1000)
    y1 = -np.log(p)
    y2 = -np.log(1 - p)
    plt.plot(p, y1, label='y = -log(p)', color='blue')
    plt.plot(p, y2, label='y = -log(1-p)', color='red')
    plt.vlines(x=[0, 1], ymin=0, ymax=10, linestyles='dotted')
    plt.legend()
    plt.xlabel('Probability')
    plt.show()
