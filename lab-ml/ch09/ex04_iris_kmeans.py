# k-Means 알고리즘을 사용한 iris 데이터를 clustering
# 1) iris 데이터를 로드
# 2) k=2, 3, 4, 5, 6, 7, 8 변경하면서, KMeans 모델을 적용
# 3) k vs inertia 그래프
# 4) k vs silhouette score 그래프
# 5) silhouette diagram

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import SilhouetteVisualizer

if __name__ == '__main__':
    X, y = load_iris(return_X_y=True)
    print(X.shape, y.shape)

    k_values = range(2, 9)
    kmeans_models = []  # k값에 따른 KMeans 모델들을 저장하기 위한 리스트
    inertias = []  # k값에 따른 inertia들을 저장하기 위한 리스트
    silhouettes = []  # k값에 따른 실루엣 점수를 저장하기 위한 리스트
    for k in k_values:
        print(f'\n----- k={k} -----')
        kmeans = KMeans(n_clusters=k, random_state=1)
        kmeans_models.append(kmeans)  # KMeans 모델을 리스트에 추가
        kmeans.fit(X)  # 비지도 학습 모델 훈련 - 타겟 포함하지 않음.
        inertias.append(kmeans.inertia_)  # 모델의 inertia를 리스트에 추가
        print('labels:', kmeans.labels_)
        ss = silhouette_score(X, kmeans.labels_)
        silhouettes.append(ss)  # 실루엣 점수를 리스트에 추가

    fig, ax = plt.subplots(nrows=1, ncols=2)

    # k vs inertia plot
    ax[0].plot(k_values, inertias, marker='o')
    ax[0].set_xlabel('k')
    ax[0].set_ylabel('inertia')

    # k vs silhouette score
    ax[1].plot(k_values, silhouettes, marker='o')
    ax[1].set_xlabel('k')
    ax[1].set_ylabel('silhouette score')

    plt.show()

    # 실루엣 다이어그램
    for model in kmeans_models[:4]:  # k=2,3,4,5
        visualizer = SilhouetteVisualizer(model)
        visualizer.fit(X)
        visualizer.show()

    # k=3일 때, petal length vs petal width plot - cluster 구분





