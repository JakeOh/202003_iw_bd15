import pickle
import time

import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.pipeline import Pipeline


def dimension_reduction(title, reducer, X, y):
    t0 = time.time()
    X_reduced = reducer.fit_transform(X)
    t1 = time.time()
    print(f'{title} reduction time: {round(t1 - t0, 2)} seconds')

    plt.scatter(X_reduced[:, 0], X_reduced[:, 1],
                c=y, cmap=plt.cm.jet)
    plt.colorbar()
    plt.title(title)
    plt.show()


if __name__ == '__main__':
    # pickle에서 MNIST 데이터 로드
    with open('../ch03/mnist.pkl', mode='rb') as file:
        mnist = pickle.load(file)
    X, y = mnist['data'], mnist['target'].astype(np.int)

    # 784(28x28) 차원 -> 2차원 축소
    # 10,000개의 샘플만 선택 차원 축소 알고리즘 적용
    # X = X[:10_000]
    index = np.random.permutation(70_000)[:10_000]
    X, y = X[index], y[index]

    # Manifold 방법: t-SNE
    tsne = TSNE(n_components=2, n_jobs=-1, random_state=1)
    # t_start = time.time()  # 시작 시간 측정
    # X_reduced = tsne.fit_transform(X)  # 784 -> 2차원 축소
    # t_end = time.time()  # 종료 시간 측정
    # print(f't-SNE time: {round(t_end - t_start, 2)} seconds')
    # plt.scatter(X_reduced[:, 0], X_reduced[:, 1],
    #             c=y, cmap=plt.cm.jet)
    # plt.colorbar()
    # plt.title('t-SNE')
    # plt.show()

    # MNIST 데이터에 PCA(주성분 분석)을 적용 -> 2차원으로 축소 -> 2D Scatter
    # PCA 변환 시간 측정
    pca = PCA(n_components=2, random_state=1)

    # PCA와 tSNE를 Pipeline으로 연결 -> 2차원으로 축소
    # 차원 축소 시간 측정, 2D Scatter
    pca_tsne = Pipeline([
        ('pca', PCA(n_components=0.95, random_state=1)),
        ('tsne', TSNE(n_components=2, n_jobs=-1, random_state=1))
    ])

    titles = ['tSNE', 'PCA', 'PCA + t-SNE']
    reducers = [tsne, pca, pca_tsne]
    for title, reducer in zip(titles, reducers):
        dimension_reduction(title, reducer, X, y)

    # LLE
    # PCA + LLE

    # MDS
    # PCA + MDS

    # Isomap
    # PCA + Isomap









