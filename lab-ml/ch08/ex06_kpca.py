import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_swiss_roll
from sklearn.decomposition import KernelPCA

if __name__ == '__main__':
    X, y = make_swiss_roll(n_samples=1000, noise=0.2, random_state=42)
    print(X.shape, y.shape)
    print(X[:5])
    print(y[:5])

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y, cmap=plt.cm.hot)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # ax.view_init(180, 0)
    plt.show()

    # Kernel PCA: 커널 트릭을 사용한 주성분 분성
    lin_kpca = KernelPCA(n_components=2, kernel='linear',
                         random_state=1)
    X_reduced = lin_kpca.fit_transform(X)
    print(X_reduced.shape)

    plt.scatter(X_reduced[:, 0], X_reduced[:, 1],
                c=y, cmap=plt.cm.hot)
    plt.show()

    rbf_kpca = KernelPCA(n_components=2, kernel='rbf', gamma=0.043,
                         random_state=1)
    X_reduced = rbf_kpca.fit_transform(X)
    plt.scatter(X_reduced[:, 0], X_reduced[:, 1],
                c=y, cmap=plt.cm.hot)
    plt.show()

    sigmoid_kpca = KernelPCA(n_components=2, kernel='sigmoid', gamma=0.001,
                             random_state=1)
    # X를 차원 축소 -> scatter plot
    X_reduced = sigmoid_kpca.fit_transform(X)
    plt.scatter(X_reduced[:, 0], X_reduced[:, 1],
                c=y, cmap=plt.cm.hot)
    plt.show()




