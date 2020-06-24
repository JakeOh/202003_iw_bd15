import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


def plot_decision_boundaries(model, X):
    # X: (m, 2) 모양의 데이터
    # mins, maxes: 각 컬럼에서 최솟값, 최댓값을 찾음.
    mins = np.min(X, axis=0) - 0.1  # (2,)
    maxes = np.max(X, axis=0) + 0.1  # (2,)
    # 최솟값 ~ 최댓값 구간을 일정한 간격으로 쪼갬.
    x_pts = np.linspace(mins[0], maxes[0], 1000)
    y_pts = np.linspace(mins[1], maxes[1], 1000)
    # meshgrid 만듦. (1000x1000 조합)
    Xs, Ys = np.meshgrid(x_pts, y_pts)
    XY = np.c_[Xs.ravel(), Ys.ravel()]  # 결정 경계면을 예측할 좌표
    Z = model.predict(XY).reshape(Xs.shape)  # 예측값

    plt.contourf(Xs, Ys, Z, cmap='Pastel2')  # 경계선 안을 색으로 채움.
    plt.contour(Xs, Ys, Z, colors='k')  # 경계선을 그림.

    # 데이터들을 scatter plot
    plt.scatter(X[:, 0], X[:, 1], s=2, c='darkgray')

    # 비지도 학습 모델이 예측한 클러스터들의 중심(센트로이드)을 그림.
    centroids = model.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x')


if __name__ == '__main__':
    blob_centers = np.array([[0.2, 2.3],
                             [-1.5, 2.3],
                             [-2.0, 1.8],
                             [-2.0, 2.8],
                             [-2.0, 1.3]])
    blob_stds = np.array([0.4, 0.3, 0.1, 0.1, 0.1])
    X, y = make_blobs(n_samples=2_000,
                      centers=blob_centers,
                      cluster_std=blob_stds,
                      random_state=1)
    print(X.shape, y.shape)
    print(y[:10])
    print(np.unique(y))

    plt.scatter(X[:, 0], X[:, 1], s=2)
    plt.show()

    # k-Means 비지도 학습 알고리즘
    k = 5
    kmeans = KMeans(n_clusters=k, random_state=10)  # 모델 선택, 생성
    kmeans.fit(X)  # 비지도 학습 - 타겟(레이블) 없이 데이터만 훈련
    y_pred = kmeans.predict(X)  # 예측
    print(y_pred[:10])
    # k-Means 알고리즘 학습 후 찾을 수있는 특성들(attributes):
    print('label:', kmeans.labels_)  # predict가 리턴하는 예측값(레이블)
    print('cluster centers:', kmeans.cluster_centers_)
    print('inertia:', kmeans.inertia_)

    plot_decision_boundaries(kmeans, X)
    plt.show()

    k_ranges = range(2, 10)
    inertias = []
    for k in k_ranges:
        model = KMeans(n_clusters=k, random_state=1)
        model.fit(X)
        inertias.append(model.inertia_)
        plot_decision_boundaries(model, X)
        plt.title(f'k = {k}')
        plt.show()

    plt.plot(k_ranges, inertias, marker='o')
    plt.xlabel('k')
    plt.ylabel('inertia')
    plt.show()
    # inertia: 각 샘플들과 가장 가까운 센트로이드(클러스터의 중심) 사이의
    # 평균 제곱 거리
    # k가 결정된 경우에는 inertia가 작아지는 (또는 최소가 되는) 경계면을
    # 찾는 게 kMeans 알고리즘.
    # k가 커질 수록(클러스터의 개수가 많아질 수록) inertia는 작아짐.
