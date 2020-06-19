import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC, SVC

from ch05.ex02_svm import plot_decision_boundary

if __name__ == '__main__':
    X = np.array([[1, 50],
                  [5, 20],
                  [3, 80],
                  [5, 60]])
    y = np.array([0, 0, 1, 1])

    lin_svm = LinearSVC(C=float('inf'), max_iter=10_000)
    # lin_svm = SVC(kernel='linear')
    lin_svm.fit(X, y)

    plot_decision_boundary(lin_svm, 1, 5)
    plt.scatter(X[y == 0, 0], X[y == 0, 1], c='blue')
    plt.scatter(X[y == 1, 0], X[y == 1, 1], c='green')
    plt.show()

    std_scaler = StandardScaler()
    X_scaled = std_scaler.fit_transform(X)
    lin_svm2 = LinearSVC(C=float('inf'), max_iter=10_000)
    # lin_svm2 = SVC(kernel='linear')
    lin_svm2.fit(X_scaled, y)

    plot_decision_boundary(lin_svm2, -2, 2)
    plt.scatter(X_scaled[y == 0, 0], X_scaled[y == 0, 1], c='blue')
    plt.scatter(X_scaled[y == 1, 0], X_scaled[y == 1, 1], c='green')
    # plt.axis([-2, 2, -2, 2])
    plt.show()
