import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression

from ch04.ex13_sigmoid import sigmoid

if __name__ == '__main__':
    # scikit-learn 예제 샘플 iris를 로드
    iris = datasets.load_iris()

    # 특성들 중 petal length, petal width를 선택한 데이터 셋 준비
    X = iris.data[:, [2, 3]]  # iris['data'], iris.data
    # 2진 분류 - 레이블을 virginica와 virginica가 아닌 것으로 준비
    y = (iris.target == 2)

    print(X[:5])
    print(y[:5])

    # LogisticRegression 모델 선택, 학습
    log_reg = LogisticRegression(solver='liblinear', random_state=1)
    log_reg.fit(X, y)

    # 모델이 계산한 intercept_, coef_를 출력
    bias, weights = log_reg.intercept_, log_reg.coef_
    print('bias:', bias)
    print('weights:', weights)

    # 데이터 중에서 [0, 50, 100]번째 샘플들을 선택, 확률 p를 직접 계산
    samples = X[[0, 50, 100]]
    print('\nSamples:')
    print(samples)

    t = bias + samples @ weights.T
    print('\nLinear Hypothesis:')
    print(t)

    p = sigmoid(t)
    print('\nProbabilities(Sigmoid):')
    print(p)

    # 모델이 예측한 확률, 예측값과 비교
    pred_prob = log_reg.predict_proba(samples)
    predicts = log_reg.predict(samples)
    print('\nPredicted Probabilities:')
    print(pred_prob)
    print('\nPredicts:')
    print(predicts)

    # 위에서 선택한 샘플들의 비용(손실)을 계산
    y_true = y[[0, 50, 100]]
    print('\ny_true:')
    print(y_true)
    cost_sum = 0
    for i in range(3):
        cost = -(y_true[i] * np.log(p[i]) +
                 (1-y_true[i]) * np.log(1-p[i]))
        print('cost =', cost)
        cost_sum += cost
    print('cost_sum =', cost_sum)

    cost = -(y_true @ np.log(p) + (1 - y_true) @ np.log(1-p))
    print(cost)
