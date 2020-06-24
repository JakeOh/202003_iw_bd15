import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from sklearn.mixture import GaussianMixture

if __name__ == '__main__':
    iris = load_iris()  # dict
    X, y = iris['data'], iris['target']
    print(X.shape, y.shape)
    # print(y)

    # x축: petal length, y축: petal width -> 2D scatter plot
    # 1) target별 색깔, 레이블
    # 2) target 구분 없이
    fig, ax = plt.subplots(nrows=1, ncols=2)
    ax[0].scatter(X[y == 0, 2], X[y == 0, 3],
                  label=iris.target_names[0])
    ax[0].scatter(X[y == 1, 2], X[y == 1, 3],
                  label=iris.target_names[1])
    ax[0].scatter(X[y == 2, 2], X[y == 2, 3],
                  label=iris.target_names[2])
    ax[0].legend()
    ax[0].set_xlabel('petal length')
    ax[0].set_ylabel('petal width')

    ax[1].scatter(X[:, 2], X[:, 3], c='darkgray')

    plt.show()

    # 비지도 학습(Unsupervised Learning) 모델 선정 생성
    gaussian_mixture = GaussianMixture(n_components=3, random_state=1)
    # 모델 학습(훈련) - 레이블(타겟) 없이 훈련 시킴.
    gaussian_mixture.fit(X)
    # 훈련된 ML 모델로 예측
    y_pred = gaussian_mixture.predict(X)
    print(y_pred, y_pred.shape)

    clusters = np.unique(y_pred)  # [0 1 2]
    # 비지도 학습에서 예측된 값들을 scatter plot
    for cluster_id in clusters:
        plt.scatter(X[y_pred == cluster_id, 2],
                    X[y_pred == cluster_id, 3],
                    label=f'Cluster {cluster_id}')
    plt.legend()
    plt.show()

    # 실제 타겟(레이블) y와 예측값 y_pred를 비교해서 예측의 정확도
    # y_pred2 = []
    # for pred in y_pred:
    #     if pred == 1:
    #         y_pred2.append(0)  # setosa
    #     elif pred == 2:
    #         y_pred2.append(1)  # versicolor
    #     else:
    #         y_pred2.append(2)  # virginica

    # 예측 1 -> 0, 예측 2 -> 1, 예측 0 -> 2
    mapping = [2, 0, 1]
    y_pred2 = [mapping[cluster_id] for cluster_id in y_pred]
    y_pred2 = np.array(y_pred2)  # python list -> numpy ndarray 변환
    print(y_pred2 == y)
    acc = np.mean(y_pred2 == y)
    print('비지도 학습 예측 정확도:', acc)

