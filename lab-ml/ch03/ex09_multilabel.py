# Multi-label Classification
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

from ch03.ch03_all import load_mnist_from_pickle, split_mnist

if __name__ == '__main__':
    mnist = load_mnist_from_pickle()
    X_train, y_train, X_test, y_test = split_mnist(mnist)

    # multi-label을 만듦.
    y_train_large = (y_train >= 7)  # 큰 숫자(True)/작은 숫자(False)
    y_train_odd = (y_train % 2 == 1)  # 홀수(True)/짝수(False)
    y_multilabel = np.c_[y_train_large, y_train_odd]
    print(y_train)
    print(y_multilabel)

    # ML 모델(알고리즘) 선택
    knn_clf = KNeighborsClassifier()
    # 학습 데이터와 학습 레이블로 모델을 학습시킴.
    knn_clf.fit(X=X_train, y=y_multilabel)
    # 예측
    y_train_pred = knn_clf.predict(X_train[:5])
    print('예측값:')
    print(y_train_pred)
    print('실제값:')
    print(y_multilabel[:5])



