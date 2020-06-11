import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

from ch04.ex13_sigmoid import sigmoid

if __name__ == '__main__':
    iris = datasets.load_iris()
    print(iris.keys())
    # print(iris['DESCR'])
    print(iris['feature_names'])  # 데이터 프레임 컬럼 이름들
    print(iris['target_names'])  # 레이블(품종)의 클래스(setosa, versicolor, virginica)

    X = iris['data']  # 데이터
    y = iris['target']  # 레이블
    print(X.shape, y.shape)

    # 4개의 특성(변수, 컬럼) 중에서 petal width(꽃잎 너비)만 선택
    X = X[:, [3]]  # (150, 1) 모양의 2차원 배열
    # print(X[:3])
    # 2진 분류 - virginica(양성) / virginica 아님(음성)
    y = (y == 2)
    # print(y)

    # 모델 선택
    log_reg = LogisticRegression(solver='liblinear', random_state=1)
    # 모델 학습: 최적의 계수(theta0, theta1)를 찾음
    log_reg.fit(X, y)
    # 모델 평가: 예측(predict)
    y_pred = log_reg.predict(X)
    # 평가 지표
    acc = np.mean(y == y_pred)
    print('정확도(accuracry):', acc)

    # 품종(y축) vs 꽃잎 너비(x축) 그래프
    plt.scatter(X, y)
    plt.xlabel('petal width)')
    plt.ylabel('species')
    plt.vlines(x=1.6, ymin=0, ymax=1, linestyles='dotted', color='red')
    plt.show()

    # 예측 확률(predicted probabilities)
    y_pred_prob = log_reg.predict_proba(X)
    print(y_pred_prob)  # (150, 2) [[1-p, p], ....] 2차원 배열

    X_test = np.linspace(0, 3, 1000).reshape((-1, 1))
    y_test_prob = log_reg.predict_proba(X_test)
    plt.plot(X_test, y_test_prob[:, 0], label='1-p')
    plt.plot(X_test, y_test_prob[:, 1], label='p')
    plt.legend()
    plt.show()

    print()
    # 선형 회귀에서 찾은 계수들
    bias, weights = log_reg.intercept_, log_reg.coef_
    print('bias:', bias)
    print('weights:', weights)

    # 0번째 샘플의 예측 확률, 예측값
    print(f'prob: {y_pred_prob[0]}, pred: {y_pred[0]}')
    sample = X[0]
    print(sample)
    theta0 = bias[0]
    theta1 = weights[0, 0]
    x = sample[0]
    print(theta0, theta1, x)
    t = theta0 + theta1 * x  # 선형 가설
    p = sigmoid(t)  # 선형 가설을 이용한 양성 확률
    print('p =', p)

    # 0번째 샘플의 비용(손실)
    # -[y_actual * log(p) + (1 - y_actual) * log(1 - p)]
    cost = -(y[0] * np.log(p) + (1 - y[0]) * np.log(1 - p))
    print('loss=', cost)




