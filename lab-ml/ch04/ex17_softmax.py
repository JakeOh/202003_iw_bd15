import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

if __name__ == '__main__':
    iris = datasets.load_iris()
    X, y = iris['data'], iris['target']  # iris.data, iris.target

    # petal width만 데이터로 선택
    X = X[:, [3]]  # (150, 1) 2D array

    # multi-class 분류: 0-setosa, 1-versicolor, 2-virginica
    log_reg = LogisticRegression()  # 모델 생성
    log_reg.fit(X, y)  # 모델 학습
    y_pred = log_reg.predict(X)

    conf_mat = confusion_matrix(y, y_pred)
    print(conf_mat)

    cls_report = classification_report(y, y_pred,
                                       target_names=iris.target_names)
    print(cls_report)

    sample0 = X[0]
    # sample0의 예측 확률
    sample0_probs = log_reg.predict_proba([sample0])
    print(sample0_probs, np.argmax(sample0_probs, axis=1))
    # [class0일 확률, class1일 확률, class2일 확률]
    print('class:', y_pred[0])

    bias, weights = log_reg.intercept_, log_reg.coef_
    print('\nbias')
    print(bias)
    # [class0에서 필요한 bias, class1에서 필요한 bias, ...]
    print('\nweights')
    print(weights)
    # [
    #   [class0에서 필요한 theta1, theta2, ...]
    #   [class1에서 필요한 theta1, theta2, ...]
    #   ...
    # ]

    # sample0의 softmax 점수
    print('sample0:', sample0)
    # sample0가 class0(setosa)가 될 점수
    score_0 = bias[0] + weights[0, 0] * sample0[0]
    # sample0가 class1(versicolor)가 될 점수
    score_1 = bias[1] + weights[1, 0] * sample0[0]
    # sample0가 class2(virginica)가 될 점수
    score_2 = bias[2] + weights[2, 0] * sample0[0]
    print('\nscores:')
    print(score_0, score_1, score_2)

    # sample0가 각 클래스에 속할 확률
    sum_scores = np.exp(score_0) + np.exp(score_1) + np.exp(score_2)
    p_0 = np.exp(score_0) / sum_scores
    p_1 = np.exp(score_1) / sum_scores
    p_2 = np.exp(score_2) / sum_scores
    print('\nprobabilities:')
    print(p_0, p_1, p_2)

    # sample0의 cross-entropy
    print('\nsample0의 실제 target 값:', y[0])
    y_0, y_1, y_2 = 1, 0, 0
    cross_ent = -(y_0 * np.log(p_0) + y_1 * np.log(p_1) +
                  y_2 * np.log(p_2))
    print(cross_ent)


