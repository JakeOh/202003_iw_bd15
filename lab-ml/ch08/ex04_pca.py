# MNIST 데이터 로드
# Train(60,000)/Test(10,000)로 분리
# Random Forest 알고리즘에 Train 셋을 훈련 - fit
# 훈련 시간을 측정, 출력
# 훈련된 모델로 Test 셋의 성능 측정 - 정확도 계산

# explained variance ratio의 누적값이 95%이상이 되는 주성분 축만큼 선택
# PCA(주성분 분석)를 적용해서 Train 셋을 변환 - 차원 축소
# 차원이 축소된 훈련 셋에서 Random Forest를 훈련.
# Random Forest 훈련 시간 측정
# 훈련된 모델로 Test 셋의 성능(정확도)를 계산

# LogisticRegression 모델을 선택해서 위의 과정 반복
# PCA를 적용했을 때와 PCA를 적용하지 않았을 때의 훈련시간/정확도 차이 비교

import pickle
import time

import numpy as np
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


def performance_train_test(X_train, X_test, y_train, y_test,
                           classifer, pca=False):
    print(f'\n===== {classifer.__class__.__name__} =====')
    if pca:
        print('PCA fitting and transforming ......')
        # 주성분 분석을 사용해서 Train/Test 셋의 차원을 축소
        reducer = PCA(n_components=0.95, random_state=42)
        reducer.fit(X_train)  # Train 셋을 학습 -> principal components 찾음.
        X_train = reducer.transform(X_train)  # Train 셋 차원 축소
        X_test = reducer.transform(X_test)  # Test 셋 차원 축소
    t_start = time.time()  # 훈련 시작 시간
    classifer.fit(X_train, y_train)  # 학습(훈련)
    t_end = time.time()  #  훈련 종료 시간
    print(f'Training time: {round(t_end - t_start, 2)} seconds')
    score = classifer.score(X_test, y_test)
    print(f'Test score: {round(score, 4)}')


if __name__ == '__main__':
    with open('../ch03/mnist.pkl', mode='rb') as file:
        mnist = pickle.load(file)  # dict
    X = mnist['data']  # 손글씨 이미지 데이터
    y = mnist['target'].astype(np.int)  # 분류 클래스(0, 1, 2, ..., 9)
    print(X.shape, y.shape)

    train_size = 60_000
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    clf1 = RandomForestClassifier(random_state=42)
    clf2 = RandomForestClassifier(random_state=42)
    clf3 = LogisticRegression(random_state=42)
    clf4 = LogisticRegression(random_state=42)

    tests = [(clf1, False), (clf2, True), (clf3, False), (clf4, True)]
    for clf, pca in tests:
        performance_train_test(X_train, X_test, y_train, y_test,
                               classifer=clf, pca=pca)

    # t_start = time.time()  # 훈련 시작 시간
    # clf1.fit(X_train, y_train)
    # t_end = time.time()  # 훈련 종료 시간
    # print(f'Training time: {round(t_end - t_start, 2)} seconds')
    # score = clf1.score(X_test, y_test)
    # print(f'Test score: {round(score, 4)}')
    # performance_train_test(X_train, X_test, y_train, y_test, clf1, False)










