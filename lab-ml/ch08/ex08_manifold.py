import matplotlib.pyplot as plt
from sklearn.datasets import make_swiss_roll
from sklearn.manifold import LocallyLinearEmbedding, MDS, Isomap, TSNE

if __name__ == '__main__':
    # 차원 축소: (1) 투영(Project)-주성분 분석, (2) Manifold
    # Manifold 방법:
    # 1) LLE(Locally Linear Embedding):
    #   각 훈련 샘플들이 가장 가까운 이웃들에 얼마나 선형적으로 연관되어 있는지를 측정.
    X, y = make_swiss_roll(n_samples=1000, noise=0.2, random_state=41)
    lle = LocallyLinearEmbedding(n_neighbors=10,
                                 n_components=2,
                                 random_state=1)
    # X_reduced = lle.fit_transform(X)
    # plt.scatter(X_reduced[:, 0], X_reduced[:, 1],
    #             c=y, cmap=plt.cm.hot)
    # plt.show()

    # MDS(Multi-Distance Scaling):
    #   샘플들 간의 거리(distance)를 유지하면서 차원을 축소하는 기법.
    mds = MDS(n_components=2, random_state=1)

    # Isomap(Isometric Mapping):
    #   각 샘플들을 가장 가까운 이웃에 연결하는 그래프를 만듦.
    #   그래프 거리(graph distance, geodesic distance)를 유지하도록 차원을 축소.
    isomap = Isomap(n_components=2)

    # t-SNE(t-distribution Stochastic Neighbor Embedding)
    #   비슷한 샘플들은 가까이, 비슷하지 않은 샘플들은 멀리 떨어지도록 차원 축소하는 기법.
    tsne = TSNE(n_components=2, random_state=1)

    titles = ['LLE', 'MDS', 'Isomap', 't-SNE']
    manifold_reducers = [lle, mds, isomap, tsne]
    for title, reducer in zip(titles, manifold_reducers):
        plt.title(title)  # reducer.__class__.__name__
        # 원본 데이터를 manifold 방법을 사용해서 차원 축소
        X_reduced = reducer.fit_transform(X)
        # 차원 축소된 데이터를 2차원 scatter plot으로 그림.
        plt.scatter(X_reduced[:, 0], X_reduced[:, 1],
                    c=y, cmap=plt.cm.hot)
        plt.show()

