import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.svm import LinearSVC


def plot_decision_boundary(model, x_min, x_max):
    b, (w1, w2) = model.intercept_[0], model.coef_[0]
    x_pts = np.linspace(x_min, x_max, 100)
    y_pts = (-1/w2) * (b + w1 * x_pts)
    plt.plot(x_pts, y_pts, 'k-')  # 최대 마진(maximum margin) 평면
    plt.plot(x_pts, y_pts + (1/w2), 'r:')  # 마진(margin) 평면
    plt.plot(x_pts, y_pts - (1/w2), 'r:')  # 마진(margin) 평면


if __name__ == '__main__':
    # iris 데이터 로드
    iris = datasets.load_iris()
    X, y = iris['data'], iris['target']

    # feature: petal length, petal width를 선택
    X = X[:, (2, 3)]
    # target: viginica / not virginica (binary-class 분류)
    y = (y == 2).astype(np.int)  # virginica(1)/ not virginica(0)
    # print(y)

    # LinearSVC 모델을 사용해서 타겟을 분류하는 직선을 그래프로
    # C = 1/alpha
    # C 커지면 alpha가 작아짐 -> 규제가 작아짐 -> 학습 데이터에 더 fitting
    # C 작아지면, alpha가 커짐 -> 규제가 커짐 -> 학습 데이터의 오차를 키움
    # SVM에서 C가 커지면 마진 평면이 줄어듦.
    # SVM에서 C가 작아지면 마진 평면이 늘어남.
    lin_svm = LinearSVC(random_state=1, C=100)
    lin_svm.fit(X, y)

    plt.scatter(X[y == 1, 0], X[y == 1, 1], c='blue', label='virginica')
    plt.scatter(X[y == 0, 0], X[y == 0, 1], c='green',
                label='not virginica')
    plot_decision_boundary(lin_svm, 0.5, 7.5)
    plt.legend()
    plt.show()

    # 분류 리포트
    y_pred = lin_svm.predict(X)
    conf_mat = confusion_matrix(y, y_pred)
    print(conf_mat)

    report = classification_report(y, y_pred)
    print(report)



