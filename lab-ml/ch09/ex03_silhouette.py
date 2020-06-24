import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import SilhouetteVisualizer

from ch09.ex02_kmeans import plot_decision_boundaries

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

    # 적절한 k 값 찾기 - 적절한 클러스터 개수 찾기
    # k 값을 변경시키면서 성능 지표를 계산
    k_ranges = range(2, 10)
    inertias = []
    silhouettes = []
    kmeans_models = []
    for k in k_ranges:
        model = KMeans(n_clusters=k, random_state=1)  # 모델 선택
        model.fit(X)  # 모델 훈련
        kmeans_models.append(model)
        inertias.append(model.inertia_)
        silhouettes.append(silhouette_score(X, model.labels_))
    print('inertias:', inertias)
    print('silhouettes:', silhouettes)

    # k - 실루엣 점수 그래프
    plt.plot(k_ranges[1:], silhouettes[1:], marker='o')
    plt.xlabel('k')
    plt.ylabel('silhouette score')
    plt.show()

    # 실루엣 점수(silhouette score) = (b - a) / max(a, b)
    # a: 동일한 클러스터 안에서 다른 샘플들과의 거리의 평균
    # b: 가장 가까운 클러스터까지의 평균 거리
    # -1 <= ss <= 1
    # 실루엣 점수가 큰 모델의 클러스터 개수가 적절한 클러스터 개수
    # ss = 1: 샘플들이 자기 클러스터 안에 잘 모여 있고,
    # 다른 클러스터와는 멀리 떨어져 있는 경우
    # ss = 0: 샘들들이 클러스터 경계에 몰려 있는 경우
    # ss = -1: 샘플들이 잘못된 클러스터에 포함되는 경우.

    # 실루엣 다이어그램
    # pip install yellowbrick
    for model in kmeans_models[1:]:  # 훈련된 각각의 KMeans 모델들에 대해서
        visualizer = SilhouetteVisualizer(model, color='yellowbrick')
        visualizer.fit(X)
        visualizer.show()
