import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.metrics import classification_report
from sklearn.svm import LinearSVC

if __name__ == '__main__':
    iris = datasets.load_iris()  # dict
    print(iris.keys())
    X, y = iris.data, iris.target  # iris['data'], iris['target']
    print(X.shape, y.shape)
    print(iris.feature_names)
    print(X[:5])
    print(iris.target_names)
    print(y)
    # 분류 - LogisticRegression, SGDClassifier
    # SVM(Support Vector Machine): 분류(SVC), 회귀(SVR)

    # 특징(feature)은 petal length, petal width만 선택
    X = X[:, (2, 3)]
    print(X[:5])
    # binary-class 분류(setosa vs not-setosa)
    y = (y == 0).astype(np.int)  # setosa=1(True), not-setosa=0(False)
    print(y)

    # x축은 petal length, y축은 petal width
    # setosa를 파란색 점, not-setosa를 초록색 점.
    plt.scatter(X[y == 1, 0], X[y == 1, 1], c='blue', label='setosa')
    plt.scatter(X[y == 0, 0], X[y == 0, 1], c='green',
                label='not setosa')

    # 임의의 직선 2개
    x_pts = np.linspace(0.5, 7.5, 100)
    y_pts1 = 0.1 * x_pts + 0.55
    y_pts2 = x_pts - 1.8
    plt.plot(x_pts, y_pts1, 'r-')
    plt.plot(x_pts, y_pts2, 'r:')

    plt.axis([0.5, 7.5, 0, 3.0])
    plt.legend()
    plt.show()

    lin_svm = LinearSVC(random_state=1, C=100)  # 모델 선택
    lin_svm.fit(X, y)  # 모델 학습
    y_pred = lin_svm.predict(X)
    report = classification_report(y, y_pred)
    print(report)

    b, (w1, w2) = lin_svm.intercept_[0], lin_svm.coef_[0]
    print(f'b = {b}, w1 = {w1}, w2 = {w2}')
    # b + w1 * x1 + w2 * x2 = 0
    # x2 = (-1/w2) * (b + w1 * x1)
    y_pts = (-1/w2) * (b + w1 * x_pts)

    plt.scatter(X[y == 1, 0], X[y == 1, 1], c='blue', label='setosa')
    plt.scatter(X[y == 0, 0], X[y == 0, 1], c='green',
                label='not setosa')
    plt.plot(x_pts, y_pts, 'k-')
    plt.plot(x_pts, y_pts + (1/w2), 'r:')
    plt.plot(x_pts, y_pts - (1/w2), 'r:')

    plt.legend()
    plt.xlabel('petal length')
    plt.ylabel('petal width')
    plt.axis([0.5, 7.5, 0, 3])
    plt.show()













