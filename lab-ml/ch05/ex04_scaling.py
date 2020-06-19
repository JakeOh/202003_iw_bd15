import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC, LinearSVC

from ch05.ex02_svm import plot_decision_boundary


def find_conf_mat(model, X, y, scaler=None):
    if scaler:  # scaler 값이 있다면(None이 아니라면)
        model = Pipeline([
            ('scaler', scaler),
            ('classifier', model)
        ])
    model.fit(X, y)
    y_pred = model.predict(X)
    conf_mat = confusion_matrix(y, y_pred)
    print(conf_mat)
    # model.intercept_, coef_
    if scaler:
        plot_decision_boundary(model['classifier'], -2, 2)
        X = model['scaler'].transform(X)
        plot_iris_virginica_or_not(X, y)
        plt.axis([-2, 2, -2, 2])
    else:
        plot_decision_boundary(model, 0.5, 7.5)
        plot_iris_virginica_or_not(X, y)
        plt.axis([0.5, 7.5, 0, 3])
    plt.show()


def plot_iris_virginica_or_not(X, y):
    plt.scatter(X[y == 1, 0], X[y == 1, 1], c='blue', marker='o',
                label='virginica')
    plt.scatter(X[y == 0, 0], X[y == 0, 1], c='green', marker='s',
                label='not virginica')


if __name__ == '__main__':
    iris = datasets.load_iris()
    X = iris.data[:, (2, 3)]  # petal length, petal width
    y = (iris.target == 2).astype(np.int)  # virginica(1)/not-vir(0)

    svc = SVC(kernel='linear', random_state=1)
    # svc.fit(X, y)
    # y_pred = svc.predict(X)
    # conf_mat = confusion_matrix(y, y_pred)
    # print(conf_mat)
    find_conf_mat(svc, X, y)

    find_conf_mat(model=SVC(kernel='linear', random_state=1),
                  X=X,
                  y=y,
                  scaler=StandardScaler())

    find_conf_mat(model=LinearSVC(random_state=1),
                  X=X, y=y)

    find_conf_mat(model=LinearSVC(random_state=1),
                  X=X, y=y,
                  scaler=StandardScaler())
