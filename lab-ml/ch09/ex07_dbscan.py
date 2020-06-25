# DBSCAN(Density-Based Spatial Clustering of Applications with Noise)
# 1) 각 샘플들에 대해서, 작은 거리 e(epsilon) 안에 놓여 있는 샘플들의 개수를 셈.
# 2) 만약 어떤 샘플이, e 거리 안에 자기 자신을 포함해서 적어도 min_samples개의
# 샘플들을 가지고 있다면, 그 샘플을 핵심 샘플(core sample)이라고 부름.
# 3) 핵심 샘플의 e 거리 이웃에 있는 모든 샘플들은 같은 클러스터로 분류.
# 4) 핵심 샘플도 아니고, e 거리 이웃 안에 다른 샘플이 없는 경우, 그 샘플을
# 이상치(anomaly)로 간주함.

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons

if __name__ == '__main__':
    X, y = make_moons(n_samples=1_000, noise=0.05, random_state=1)
    print(X.shape, y.shape)

    # 데이터 시각화
    plt.scatter(X[:, 0], X[:, 1], s=3)
    plt.show()

    dbscan = DBSCAN(eps=0.1, min_samples=20)
    dbscan.fit(X)
    print('labels:', dbscan.labels_)
    # label_: 클러스터 아이디
    # label_이 -1인 경우는 이상치(anomaly) - eps 거리 이웃에 아무도 없는 경우.
    print('unique labels:', np.unique(dbscan.labels_))

    print('core sample index:', dbscan.core_sample_indices_)
    # core_sample_indices_: 전체 데이터 X 중에서 핵심 샘플의 인덱스들

    print('core samples:', dbscan.components_)
    # components_: 핵심 샘플들

    # 클러스터 시각화
    labels = dbscan.labels_
    clusters = np.unique(labels)
    for cluster_id in clusters:
        if cluster_id == -1:  # 이상치
            plt.scatter(X[labels == cluster_id, 0],
                        X[labels == cluster_id, 1],
                        label=f'Anomaly', marker='x', c='red')
        else:
            plt.scatter(X[labels == cluster_id, 0],
                        X[labels == cluster_id, 1],
                        label=f'Cluster {cluster_id}')
    plt.legend()
    plt.show()







