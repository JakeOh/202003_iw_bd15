import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.svm import LinearSVC, SVC

from ch05.ex05 import train_test_report


def plot_moon(X, y):
    plt.scatter(X[y == 0, 0], X[y == 0, 1], c='green', marker='o')
    plt.scatter(X[y == 1, 0], X[y == 1, 1], c='red', marker='^')
    plt.grid(b=True, which='both')
    plt.xlabel('x1')
    plt.ylabel('x2')


def plot_nonlinear_boundary(clf, axes):
    # clf: 학습(훈련)이 끝난 모델(분류기)
    # axes: [x1_min, x1_max, x2_min, x2_max]
    # 1D array
    x1 = np.linspace(axes[0], axes[1], 100)
    x2 = np.linspace(axes[2], axes[3], 100)
    # 2D array
    X1, X2 = np.meshgrid(x1, x2)
    X = np.c_[X1.ravel(), X2.ravel()]  # (100x100, 2) shape
    y_pred = clf.predict(X).reshape(X1.shape)
    plt.contourf(X1, X2, y_pred, cmap=plt.cm.brg, alpha=0.2)


if __name__ == '__main__':
    X, y = datasets.make_moons(n_samples=100,
                               noise=0.15,
                               random_state=1)
    print(X.shape, y.shape)
    classes, counts = np.unique(y, return_counts=True)
    print(classes, counts)

    # plot_moon(X, y)
    # plt.show()

    clf1 = LinearSVC(random_state=1, loss='hinge')
    # train_test_report(X, y, clf1, title='LinearSVC')
    clf1.fit(X, y)  # 훈련
    print(clf1.intercept_, clf1.coef_)
    b = clf1.intercept_[0]
    w1, w2 = clf1.coef_[0]
    x_pts = np.linspace(-1.5, 2.5, 100)
    y_pts = (-1/w2) * (b + w1 * x_pts)
    plt.plot(x_pts, y_pts, 'k-')  # decision boundary(결정 경계)
    plot_moon(X, y)
    plt.show()

    # 고차항(PolynomialFeatures)을 추가한 모델
    clf2 = Pipeline([
        ('poly_features', PolynomialFeatures(degree=3, include_bias=False)),
        ('scaler', StandardScaler()),
        ('classifier', LinearSVC(random_state=1, loss='hinge'))
    ])
    clf2.fit(X, y)
    print(clf2['classifier'].intercept_,
          clf2['classifier'].coef_)
    axes = [-1.5, 2.5, -1, 1.5]
    plot_nonlinear_boundary(clf2, axes)
    plot_moon(X, y)
    plt.title('Linear SVC')
    plt.show()

    clf3 = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', SVC(kernel='poly', degree=3, coef0=10, random_state=1))
        # kernel: rbf(기본값), linear, poly
        # coef0: 고차항들에게 어느정도 중요도를 줄 것인지
        #   숫자가 작을 수록 저차항이 중요, 숫자가 커질 수록 고차항이 중요.
    ])
    clf3.fit(X, y)
    plot_nonlinear_boundary(clf3, axes)
    plot_moon(X, y)
    plt.title('SVC(kernel=poly)')
    plt.show()

    clf4 = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', SVC(kernel='rbf', gamma=10))
        # kernel='rbf'인 경우,
        #   gammma가 작을 수록(0에 가까울 수록) 직선에 가까운 경계면
        #   gamma가 커질 수록 모델에 overfitting되는 경계면
    ])
    clf4.fit(X, y)
    plot_nonlinear_boundary(clf4, axes)
    plot_moon(X, y)
    plt.title('SVC(kernel=rbf)')
    plt.show()
