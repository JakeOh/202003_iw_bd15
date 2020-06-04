import pickle
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix

from ch03.ch03_all import split_mnist
from ch03.ex02_mnist import plot_digit

if __name__ == '__main__':
    # 파일에서 데이터 로드
    with open('mnist.pkl', mode='rb') as file:
        mnist = pickle.load(file)

    # mnist 딕셔너리에서 데이터, 레이블 분리
    X, y = mnist['data'], mnist['target'].astype(np.int8)
    # print(y[:10])
    # print(y[-10:])
    # 데이터와 레이블은 무작위로 섞여 있음
    # -> 앞에서부터 일정 비율(6:1)로 train/test 나눔.
    N = 60_000
    X_train, X_test = X[:N], X[N:]
    y_train, y_test = y[:N], y[N:]
    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

    X_train, y_train, X_test, y_test = split_mnist(mnist)
    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

    # 분류(classification)
    # 1) 2진 분류(binary classification)
    # 2) 다중 분류(multi-class classification)

    # 2진 분류: 5인지(True, 1) 아닌지(False, 0) 분류
    print(y_train[:20])
    y_train_5 = (y_train == 5)  # 2진 분류를 위한 레이블(타겟)
    print(y_train_5[:20])

    # 2진 분류 알고리즘 선택
    # 확률적 경사 하강법 분류기(Stochastic Gradient Descent Classifier)
    sgd_clf = SGDClassifier(random_state=1)  # 모델 선택.
    sgd_clf.fit(X=X_train, y=y_train_5)  # 모델을 데이터로 학습시킴.
    y_train_predicts = sgd_clf.predict(X=X_train)  # 예측
    print(y_train_predicts[:20])

    # 정확도(accuracy): 전체 타겟 중 예측이 맞춘 비율.
    # (정확한 예측값 개수)/(전체 example 개수)
    # print(np.mean([True, False, False, True, False]))
    accuarcy = np.mean(y_train_5 == y_train_predicts)
    print('정확도(accuracy):', accuarcy)
    # '5' vs '5 아님' 비율은 1:9 - 균일하지 못한 2진 분류
    # 만약 전부 '5가 아님'이라는 예측만 하는 분류기 이더라도 정확도는 90% 정도가 됨.
    # 정확도가 분류(classification)의 유일한 성능 지표는 아님.
    # 정밀도(precision), 재현율(recall), F1 점수(F1-score)
    # 정밀도: 양성(positive) 예측 들 중에서 정답률. TP / (TP + FP)
    # 재현율: 실제 양성(positive)들 중에서 정답률. TP / (TP + FN)
    # F1-score: 정밀도와 재현률의 조화 평균.
    # 2/(1/precision + 1/recall) = (2 * precision * recall)/(precision + recall)

    # confusion matrix(혼동 행렬, 오차 행렬)
    conf_mat = confusion_matrix(y_true=y_train_5,
                                y_pred=y_train_predicts)
    print(conf_mat)
    tn = 53381  # 5가 아닌 이미지를 5가 아니라고 정확히 예측(true negative)
    fp = 1198  # 5가 아닌 이미지를 5라고 틀리게 예측(false positive)
    fn = 690  # 5인 이미지를 5가 아니라고 틀리계 예측(false negative)
    tp = 4731  # 5인 이미지를 5라고 정확하게 예측(true positive)

    precision = tp / (tp + fp)  # 정밀도
    recall = tp / (tp + fn)  # 재현률
    f1 = 2 / (1 / precision + 1 / recall)  # f1-score
    print('정밀도(precision):', precision)
    print('재현률(recall):', recall)
    print('F1 점수(F1-score):', f1)

    # 예측이 틀린 이미지 1개를 찾아서 그래프로 출력
    predict_results = (y_train_5 == y_train_predicts)
    wrong_predicts = np.where(predict_results == False)
    print(wrong_predicts)
    first_index = wrong_predicts[0][0]
    print(y_train[first_index], y_train_predicts[first_index])
    plot_digit(X_train[first_index])
