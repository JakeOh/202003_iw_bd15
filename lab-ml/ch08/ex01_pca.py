import pickle

import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    # PCA(Principal Component Analysis, 주성분 분석)
    # 차원 축소 기법 중에서 projection 방법
    # 주성분 축(원본 데이터의 분산을 가장 많이 유지하는 축)을 찾아서 투영.

    # MNIST 데이터 준비
    with open('../ch03/mnist.pkl', mode='rb') as file:
        # pickle 형식의 파일을 binary read 모드로 오픈
        mnist = pickle.load(file)  # dict
        print(mnist.keys())

    X = mnist['data']
    y = mnist['target'].astype(np.int)  # 문자열 -> 정수 타입 변환
    print(X.shape, y.shape)
    # 70,000개 샘플, 784개 특성

    # Train/Test 분리
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=0.2, random_state=1)
    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

    # 주성분 분석(PCA)
    pca = PCA(n_components=5)
    pca.fit(X_train)  # PCA를 학습 데이터에 fitting
    # explained variance(설명된 분산): 주성분 축을 따라서 계산된 분산들의 리스트
    print('explained variance:', pca.explained_variance_)
    # explained variance ratio(설명된 분산 비율):
    # 주성분 축을 따라서 계산된 분산들의 비율
    print('explained variance ratio:', pca.explained_variance_ratio_)

    # 주성분 축의 개수를 지정하지 않고, 모든 주성분을 찾음.
    pca = PCA()
    pca.fit(X_train)
    # explained variance ratio
    evr = pca.explained_variance_ratio_
    print(np.sum(evr))  # 분산 비율의 합 = 1

    # 전체 훈련 데이터 셋의 분산의 95% 이상을 설명할 수 있는 PC의 개수
    # 누적 합계(cumulative sum)
    evr_cumsum = np.cumsum(evr)
    print(evr_cumsum[:5])

    n_pc = np.argmax(evr_cumsum >= 0.95) + 1
    print('n_pc =', n_pc, ',', evr_cumsum[153])

    # 설명된 분산 비율의 누적 합계 그래프
    plt.plot(evr_cumsum, lw=2)
    plt.axhline(y=0.95, c='red', ls='dashed')
    plt.axvline(x=153, c='green', ls='dotted')
    plt.show()

    # PCA() 생성자의 n_components 파라미터를 분산 비율(0 <= n_comp <= 1)로 설정
    pca = PCA(n_components=0.95)
    pca.fit(X_train)
    print(pca.explained_variance_ratio_.shape)

    # 95% 분산을 설명하는 주성분 축(principal component axes)을 사용해서
    # 784 features 공간 -> 154 features 공간은 차원 축소
    X_train_reduced = pca.transform(X_train)
    # (56000, 784) -> (56000, 154): 차원 축소 - 데이터 손실
    print(X_train_reduced.shape)

    # 154 차원의 MNIST 데이터를 다시 784 차원의 MNIST 데이터로 복원
    # 차원을 축소할 때 데이터 손실이 있었기 때문에 복원할 때 손실이 생길 수 밖에 없음.
    # -> 재구성 오차
    X_train_recovered = pca.inverse_transform(X_train_reduced)
    # (56000, 154) -> (56000, 784)
    print(X_train_recovered.shape)

    # 원본 훈련 셋(X_train)과 차원 축소 후 복원된 훈련 셋(X_train_recovered) 비교
    idx = 25000
    image = X_train[idx].reshape((28, 28))
    plt.imshow(image, cmap=plt.cm.binary)
    plt.show()

    image_recovered = X_train_recovered[idx].reshape((28, 28))
    plt.imshow(image_recovered, cmap=plt.cm.binary)
    plt.show()



