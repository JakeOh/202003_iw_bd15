"""
분류(Classification) 문제에서 레이블(label)과 클래스(class)
    - 숫자: 0, 1, 2, ..., 9
    - 사람: True, False
    - 옷: T-shirts, 바지, 치마, ...
    - 신발: 구두, 운동화, 슬리퍼, ...
1) Multi-class Classification:
    하나의 레이블에 속하는 데이터들을 여러개의 클래스로 분류
    예) mnist(숫자 분류), iris(붓꽃 품종 분류)
2) Multi-label Classification:
    여러개의 레이블에 속하는 데이터들을 각각의 클래스로 분류
3) 다중 출력 분류(Multi-output classification)
"""
import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict

from ch03.ch03_all import load_mnist_from_pickle, split_mnist
from ch03.ex02_mnist import plot_digit

if __name__ == '__main__':
    mnist = load_mnist_from_pickle()
    X_train, y_train, X_test, y_label = split_mnist(mnist)

    # ML 모델(알고리즘) 선택
    # sgd_clf = SGDClassifier(random_state=1)
    # 학습 데이터를 사용해서 모델을 학습시킴.
    # sgd_clf.fit(X=X_train, y=y_train)
    # 학습 결과를 저장
    # joblib.dump(sgd_clf, 'ex07_1.joblib')

    # 저장된 파일에서 ML 모델(알고리즘) 불러옴.
    sgd_clf = joblib.load('ex07_1.joblib')
    print(sgd_clf)

    # 학습 데이터의 예측값
    sgd_train_predicts = sgd_clf.predict(X_train[:5])
    print('예측값:', sgd_train_predicts)
    print('실제값:', y_train[:5])

    # 학습 데이터의 decision_function 값
    sgd_train_decision = sgd_clf.decision_function(X_train[:5])
    print(sgd_train_decision)

    # 전체 학습 세트의 예측값을 찾고, 정확도를 계산
    sgd_train_predicts = sgd_clf.predict(X_train)
    accuracy = np.mean(y_train == sgd_train_predicts)
    print('정확도(accuracy):', accuracy)

    # 교차 검증(cross validation)을 사용한 예측 및 오차 분석
    # sgd_cv_train_predicts = cross_val_predict(estimator=sgd_clf,
    #                                           X=X_train,
    #                                           y=y_train,
    #                                           cv=3,
    #                                           method='predict')
    # joblib.dump(sgd_cv_train_predicts, 'ex07_2.joblib')

    sgd_cv_train_predicts = joblib.load('ex07_2.joblib')

    print('CV SGD 정확도:', np.mean(y_train == sgd_cv_train_predicts))

    # confusion matrix(오차(혼동) 행렬)
    conf_mat = confusion_matrix(y_true=y_train,
                                y_pred=sgd_cv_train_predicts)
    print(conf_mat)

    # confusion matrix 시각화
    plt.matshow(conf_mat, cmap=plt.cm.gray)
    plt.show()

    # 샘플들마다 개수가 달라서, 오차의 개수보다 비율 더 중요.
    # confusion matrix에서 각 row의 sum을 계산 - sample의 개수를 계산
    row_sum = conf_mat.sum(axis=1, keepdims=True)
    # row_sum = conf_mat.sum(axis=1).reshape((10, 1))
    print(row_sum)
    print(conf_mat[0, :].sum(), conf_mat[1, :].sum())

    norm_conf_mat = conf_mat / row_sum
    print(norm_conf_mat)

    # 대각선(정답을 정확히 예측) - 관심 없음.
    # 대각선 바깥 - 틀리게 예측. 오차. - 관심 있음.
    # 대각선 이외의 부분에서 가장 큰 숫자(비율)을 찾고 싶음.
    # 오차 행렬의 대각선을 모두 0으로 채우면, 다른 숫자들이 상대적으로 커짐.
    np.fill_diagonal(norm_conf_mat, 0)

    plt.matshow(norm_conf_mat, cmap=plt.cm.gray)
    plt.show()

    # '8'을 '5'로 잘못 예측한 경우
    X_85 = X_train[(y_train == 8) &  # 실제값 == 8
                   (sgd_cv_train_predicts == 5)]  # 예측값 == 5
    # '3'을 '5'로 잘못 예측한 경우
    X_35 = X_train[(y_train == 3) &
                   (sgd_cv_train_predicts == 5)]

    for i in range(5):
        plot_digit(X_85[i])

    for i in range(5):
        plot_digit(X_35[i])
