# olivetti 예제 데이터 셋을 로드
# 샘플을 Train(280)/Validation(80)/Test(40) 분리
# 특성 개수가 4,096(=64x64)이기 때문에, PCA(99% 유지)를 적용 차원 축소
# Gaussian Mixture 모델을 훈련시키면서, 적절한 k 값 선택.(10, 20, 30, ...)

import matplotlib.pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import train_test_split

from ch09.ex08_olivetti import plot_olivetti_faces

if __name__ == '__main__':
    # 예제 데이터 셋 로드
    X, y = fetch_olivetti_faces(return_X_y=True)
    print(X.shape, y.shape)

    # Train/Test 분리
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, stratify=y, test_size=40,
                         random_state=1)
    # Train/Validation 분리
    X_train, X_val, y_train, y_val = \
        train_test_split(X_train, y_train, stratify=y_train,
                         test_size=80, random_state=1)

    print(X_train.shape, X_val.shape, X_test.shape)
    print(y_train.shape, y_val.shape, y_test.shape)

    # 원본 데이터 분산의 99%를 설명할 수 있는 주성분 분석을 하세요.
    # X_train, X_val, X_test 셋을 모두 변환.
    pca = PCA(n_components=0.99, random_state=1)  # 모델 생성
    X_train_pca = pca.fit_transform(X_train)  # 모델 훈련/변환
    X_val_pca = pca.transform(X_val)  # 변환
    X_test_pca = pca.transform(X_test)

    print(X_train_pca.shape, X_val_pca.shape, X_test_pca.shape)

    k_values = range(10, 150, 10)
    bics, aics = [], []
    for k in k_values:
        gm = GaussianMixture(n_components=k, random_state=1)
        gm.fit(X_train_pca)
        bics.append(gm.bic(X_train_pca))
        aics.append(gm.aic(X_train_pca))
    plt.plot(k_values, bics, marker='o', label='BIC')
    plt.plot(k_values, aics, marker='o', label='AIC')
    plt.legend()
    plt.xlabel('k')
    plt.show()

    # gm.sample(): 학습된(fitted) 가우시안 분포(정규 분포)를 따르는 랜덤 샘플을 생성.
    gm = GaussianMixture(n_components=40, random_state=1)
    gm.fit(X_train_pca)
    gm_faces, gm_labels = gm.sample(n_samples=20)
    print(gm_faces.shape, gm_labels.shape)
    gm_faces = pca.inverse_transform(gm_faces)  # 차원 축소 -> 원래 차원 복원
    print(gm_faces.shape, gm_labels.shape)
    plot_olivetti_faces(gm_faces, gm_labels)