# Gaussian Mixture Model
# 가우시안 분포(= 정규 분포): 평균, 표준편차 2개의 파라미터를 갖는 확률 분포.
# 샘플들이 여러개의 가우시안 분포에서 생성되었다고 가정하는 모델.
# 하나의 가우시안 분포에서 생성된 모든 샘플들은 같은 클러스터에 있다고 간주.

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

if __name__ == '__main__':
    X1, y1 = make_blobs(n_samples=1000,
                        centers=[[4, -4], [0, 0]],
                        random_state=1)
    print(X1.shape, y1.shape)
    plt.scatter(X1[:, 0], X1[:, 1], s=5)
    plt.show()

    # 데이터들의 분포를 길쭉한 타원형으로 만들기 위해서
    X1 = X1 @ np.array([[0.374, 0.95],
                        [0.737, 0.598]])
    plt.scatter(X1[:, 0], X1[:, 1], s=5)
    # plt.show()

    X2, y2 = make_blobs(n_samples=250, centers=1, random_state=1)
    plt.scatter(X2[:, 0], X2[:, 1], s=5)
    plt.show()

    # 데이터들을 x축의 방향으로 6만큼, y축의 방향으로 -8만큼 평행 이동
    X2 = X2 + [6, -8]
    print(X2.shape)

    # X1과 X2를 행 합치기(row concatenate)
    X, y = np.r_[X1, X2], np.r_[y1, y2]
    print(X.shape, y.shape)

    plt.scatter(X[:, 0], X[:, 1], s=5)
    plt.show()

    # 모델 선택, 생성
    gm = GaussianMixture(n_components=3, random_state=1)
    # 모델 fitting(훈련, 학습)
    gm.fit(X)
    # Gaussian Mixture 모델이 예측한 클러스터들의 중심(센트로이드)
    print(gm.means_)
    # Gaussian Mixture 모델이 예측한 공분산(Covariance)
    print(gm.covariances_)

    # Gaussian Mixture 클러스터 예측값/예측 확률
    predicts = gm.predict(X)
    print(predicts)
    pred_probs = gm.predict_proba(X)
    print(pred_probs)

    # Gaussian Mixture의 성능 지표:
    # 1) BIC(Bayesian Information Criterion)
    # 2) AIC(Akaike Information Criterion)
    print('BIC:', gm.bic(X))
    print('AIC:', gm.aic(X))
    # Gaussian Mixture 모델에서는 BIC/AIC가 작은 k 값을 선택

    k_values = range(2, 10)  # GMM에서 시도해 볼 클러스터 개수들
    # 각각의 k 값들에 대해서 GM 생성 -> 훈련 셋(X)를 fit -> bic/aic 계산
    # k-bic, k-aic 그래프
    bics, aics = [], []
    for k in k_values:
        gm = GaussianMixture(n_components=k, random_state=1)
        gm.fit(X)
        bics.append(gm.bic(X))
        aics.append(gm.aic(X))
    plt.plot(k_values, bics, marker='o', label='BIC')
    plt.plot(k_values, aics, marker='o', label='AIC')
    plt.legend()
    plt.xlabel('k')
    plt.show()