import pickle

import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import IncrementalPCA
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    # Incremental PCA(Principal Component Analysis)
    # 주성분 분석(PCA)은 샘플의 개수가 많을 수록, 특성의 개수(차원)가 많을 수록
    # fit할 때 시간과 메모리가 많이 소요.
    # 메모리가 부족한 경우, 부분적으로 주성분 분석을 하는 방법:
    # 샘플의 미니 배치를 연속적으로 주성분 분석 실행.

    # mnist.pkl을 로드
    with open('../ch03/mnist.pkl', mode='rb') as file:
        mnist = pickle.load(file)  # pickle binary -> python dict

    X = mnist['data']
    y = mnist['target'].astype(np.int)  # 문자열 -> 정수 타입 변환

    # Train/Test 셋으로 분리
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=0.2, random_state=1)
    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

    # Incremental PCA 수행
    n_batches = 100  # 미니 배치 횟수 - PCA를 나눠서 실행하는 횟수
    n_pc = 154  # 전체 PC(principal component)들 중에서 선택할 PC 개수
    inc_pca = IncrementalPCA(n_components=n_pc)
    for X_batch in np.split(X_train, n_batches):
        print('=', end='')
        inc_pca.partial_fit(X_batch)  # fit 아니라 partial_fit 호출
    print()

    # 훈련 셋의 차원을 784 -> 154로 축소
    X_train_reduced = inc_pca.transform(X_train)
    print(X_train_reduced.shape)  # (56000, 154)

    # 차원이 축소된 훈련 셋을 다시 784차원으로 복원
    X_train_recovered = inc_pca.inverse_transform(X_train_reduced)
    print(X_train_recovered.shape)
    # 원본 데이터와 얼마나 차이가 나는지 그래프로 확인
    fig, ax = plt.subplots(nrows=1, ncols=2)

    idx = 1000
    image_original = X_train[idx].reshape((28, 28))
    image_recovered = X_train_recovered[idx].reshape((28, 28))

    ax[0].imshow(image_original, cmap=plt.cm.binary)
    ax[1].imshow(image_recovered, cmap=plt.cm.binary)
    plt.show()

