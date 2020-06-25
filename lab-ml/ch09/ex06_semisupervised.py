# Semi-supervised learning(준지도 학습)
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    X, y = load_digits(return_X_y=True)
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=0.2, random_state=1)
    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

    # 1437개 훈련 샘플들 중에서 레이블이 있는 샘플의 개수가 50개라고 가정:
    # 레이블을 알고 있는 50개 샘플만 훈련 시킨 후, 테스트 셋에서 정확도 계산?
    n_labeled = 50
    # 지도 학습 모델 선택 생성
    log_reg = LogisticRegression(random_state=1,
                                 multi_class='ovr',
                                 n_jobs=-1)
    # 모델 훈련 - 레이블을 알고 있는 50개 샘플만 훈련
    log_reg.fit(X_train[:n_labeled], y_train[:n_labeled])
    # 360개 샘플을 테스트
    score = log_reg.score(X_test, y_test)
    print('score:', score)  # 83.33%

    # KMeans 알고리즘을 사용해서 훈련 셋을 50개의 클러스터로 분류
    k = 50
    kmeans = KMeans(n_clusters=50, random_state=1)
    X_train_dist = kmeans.fit_transform(X_train)
    print(X_train_dist.shape)  # 차원 축소 (1437, 50)
    # 축소된 컬럼들에서, 각 컬럼의 최솟값의 위치
    representative_index = np.argmin(X_train_dist, axis=0)
    print(representative_index)
    # 대표 인덱스 위치에 있는 테스트 샘플들만 선택
    X_repr_train = X_train[representative_index]

    # 대표 인덱스로 선택된 샘플들을 plot
    for i, digit in enumerate(X_repr_train):
        plt.subplot(5, 10, 1 + i)  # nrow=5, ncol=10, index=1,2,3,...
        image = digit.reshape((8, 8))
        plt.imshow(image, cmap=plt.cm.binary)
        plt.axis('off')
    plt.show()

    # 50개의 대표 훈련 샘플의 레이블을 작성 - 전문가 시스템
    y_repr_train = np.array([
        7, 3, 6, 4, 0, 8, 9, 5, 8, 1,
        7, 1, 2, 5, 0, 3, 2, 9, 8, 1,
        6, 4, 2, 1, 7, 8, 9, 5, 5, 1,
        2, 7, 5, 0, 6, 4, 7, 4, 8, 2,
        4, 8, 1, 0, 3, 9, 8, 9, 6, 7
    ])

    # 대표 훈련 샘플, 대표 레이블로 지도 학습
    log_reg = LogisticRegression(multi_class='ovr', n_jobs=-1,
                                 random_state=1, max_iter=1_000)
    log_reg.fit(X_repr_train, y_repr_train)
    # 테스트 셋의 정확도 계산
    score = log_reg.score(X_test, y_test)
    print('Semi-supervised score:', score)  # 89.72%
    # 랜덤하게 50개를 선택해서 레이블을 작성하는 것 보다
    # 클러스터링을 먼저 하고, 각 클러스터에서 대표 샘플을 선택해서
    # 대표 샘플들에게 레이블을 할당하고 지도 학습을 하는 것이 더 효과적.

    # 레이블 전파(label propagation)
    # 1) 같은 클러스터에 포함되는 샘플들에는 같은 레이블을 할당하고 전체 셋을 학습
    print(kmeans.labels_.shape)
    y_prop_train = np.zeros(kmeans.labels_.shape, dtype=np.int)
    for i in range(k):
        y_prop_train[kmeans.labels_ == i] = y_repr_train[i]
    print(y_prop_train)
    log_reg = LogisticRegression(multi_class='ovr',
                                 n_jobs=-1,
                                 max_iter=1_000,
                                 random_state=1)
    log_reg.fit(X_train, y_prop_train)
    score = log_reg.score(X_test, y_test)
    print('label propagation score:', score)  # 92.78%

    print(np.mean(y_train == y_prop_train))

    # 2) 같은 클러스터에 포함된 샘플들 중 일부(예, 20%)에만 같은 레이블을
    # 할당한 후, 레이블이 할당된 셋을 학습





