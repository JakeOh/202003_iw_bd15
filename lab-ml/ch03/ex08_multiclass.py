import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict

from ch03.ch03_all import load_mnist_from_pickle, split_mnist

if __name__ == '__main__':
    # ex07의 과정 연습
    # RandomForestClassifier 학습, 예측, 교차 검증, 정확도, 오차 행렬

    # 데이터 준비
    mnist = load_mnist_from_pickle()
    X_train, y_train, X_test, y_test = split_mnist(mnist)

    # 모델 선택
    forest_clf = RandomForestClassifier(n_estimators=10, random_state=1)
    # 모델 학습
    forest_clf.fit(X=X_train, y=y_train)
    # 예측
    y_train_pred = forest_clf.predict(X_train[:5])
    print('predicts:', y_train_pred)
    print('actual:', y_train[:5])

    # 검증
    y_train_pred = forest_clf.predict(X_train)
    accuracy = np.mean(y_train == y_train_pred)
    print('Random Forest Accuracy:', accuracy)

    # Overfitting 여부 확인 - 교차 검증(Cross Validation)
    y_train_pred = cross_val_predict(estimator=forest_clf,
                                     X=X_train,
                                     y=y_train,
                                     cv=3,
                                     method='predict')
    accuracy = np.mean(y_train == y_train_pred)
    print('Random Forest CV Accuracy:', accuracy)

    # 오차 행렬(Confusion Matrix)
    conf_mat = confusion_matrix(y_true=y_train, y_pred=y_train_pred)
    print(conf_mat)

    # Normalized Confusion Matrix: (예측 값 개수)/(샘플 개수)
    row_sum = np.sum(conf_mat, axis=1).reshape((10, 1))  # 각 샘플 개수
    print(row_sum)
    print(np.sum(conf_mat[0, :]), np.sum(conf_mat[1, :]))
    norm_conf_mat = conf_mat / row_sum
    # 대각선의 값을 0으로 만들어서, 오차들을 분석
    np.fill_diagonal(norm_conf_mat, 0)

    plt.matshow(norm_conf_mat, cmap=plt.cm.gray)
    plt.show()

    # SVM 분류기(Support Vector Machine Classifier): SVC
    # kNN 분류기(k-Nearest Neighbors Classifier): KNeighborsClassifier
    # 연습










