import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, classification_report

if __name__ == '__main__':
    iris = datasets.load_iris()
    print(iris.keys())
    # 아이리스 데이터 중에서 petal length, petal width만 갖는 데이터
    X = iris.data[:, [2, 3]]
    # setosa인지 아닌지(2진 분류)
    y = (iris.target == 0).astype(np.int)

    print(X[:5])
    print(y[:5])

    # scatter plot
    # - x축: petal length, y축: petal width
    # - y 값에 따라서 점의 색깔을 달리해서 표현
    X_setosa = X[y == 1]
    X_non_setosa = X[y != 1]
    plt.scatter(X_setosa[:, 0], X_setosa[:, 1],
                c='green', marker='o', label='Setosa')
    plt.scatter(X_non_setosa[:, 0], X_non_setosa[:, 1],
                c='blue', marker='^', label='Setosa')
    plt.legend()
    plt.xlabel('petal length')
    plt.ylabel('petal width')
    # plt.show()

    # LogisticRegression 모델 생성, 학습
    log_reg = LogisticRegression(solver='liblinear', C=1e5, random_state=1)
    log_reg.fit(X, y)

    # intercept_, coef_ 계수들을 찾음.
    bias, weights = log_reg.intercept_, log_reg.coef_
    print('bias:', bias)
    print('weights:', weights)

    theta0, (theta1, theta2) = bias[0], weights[0]
    x_pts = np.linspace(0, 7.5, 100)
    y_pts = (-1/theta2) * (theta0 + theta1 * x_pts)

    plt.plot(x_pts, y_pts, color='red', linestyle='solid')
    plt.axis([0, 7.5, 0, 3])
    plt.show()

    # 분류(classification)의 평가 지표(metrics)
    # 정확도(accuracy), 정밀도(precision), 재현률(recall)=민감도(sensitivity)
    # confusion matrix(혼동 행렬, 오차 행렬)
    y_pred = log_reg.predict(X)
    conf_mat = confusion_matrix(y, y_pred)
    print(conf_mat)
    acc = accuracy_score(y, y_pred)
    precision = precision_score(y, y_pred)
    recall = recall_score(y, y_pred)
    print('정확도:', acc)
    print('정밀도:', precision)
    print('재현률:', recall)

    report = classification_report(y, y_pred,
                                   target_names=['Non-Setosa', 'Setosa'])
    print(report)

    # virginica, virginica 아님 - 2진 분류(binary-class classification)
    # LogisticRegression 모델 생성, 학습
    # x축(petal length), y축(petal width) scatter plot, 분류 경계 직선
    # confusion matrix, classification report
    X = iris.data[:, [2, 3]]  # petal length, petal width
    y = (iris.target == 2).astype(np.int)  # virginica=1, non-virginica=0

    log_reg = LogisticRegression(solver='liblinear', C=1e5, random_state=1)
    log_reg.fit(X, y)

    bias, weights = log_reg.intercept_, log_reg.coef_
    theta0, (theta1, theta2) = bias[0], weights[0]

    x_pts = np.linspace(0, 7, 100)
    y_pts = (-1/theta2) * (theta0 + theta1 * x_pts)

    virginica = (y == 1)
    plt.scatter(X[virginica, 0], X[virginica, 1],
                c='blue', marker='^', label='Virginica')
    plt.scatter(X[~virginica, 0], X[~virginica, 1],
                c='green', marker='o', label='Not Virginica')
    plt.plot(x_pts, y_pts, 'r-')
    plt.xlabel('petal length')
    plt.ylabel('petal width')
    plt.legend()
    plt.axis([0, 7.5, 0, 3.5])
    plt.show()

    y_pred = log_reg.predict(X)
    conf_mat = confusion_matrix(y, y_pred)
    print(conf_mat)

    report = classification_report(y, y_pred)
    print(report)
