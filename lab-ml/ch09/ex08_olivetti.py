import time

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import fetch_olivetti_faces
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import silhouette_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


def plot_olivetti_faces(faces, labels, ncol=5):
    """

    :param faces: olivetti 얼굴 사진 배열(array)
    :param labels: olivetti 얼굴 사진의 타겟 레이블
    :param ncol: 한개의 row에 그려야할 이미지 개수(컬럼 개수)
    :return: None
    """
    n_faces = len(faces)
    nrow = (n_faces - 1) // ncol + 1
    for i, (face, label) in enumerate(zip(faces, labels)):
        plt.subplot(nrow, ncol, i + 1)
        plt.imshow(face.reshape((64, 64)), cmap=plt.cm.gray)
        plt.title(label)
        plt.axis('off')
    plt.show()


if __name__ == '__main__':
    olivetti = fetch_olivetti_faces()
    print(olivetti.keys())
    print(olivetti.DESCR)

    X, y = olivetti['data'], olivetti['target']
    print(X.shape, y.shape)
    # 샘플 개수 m = 400
    # 특성(feature) 개수 n = 4096 = 64x64 (이미지 가로 64px, 세로 64px)

    plot_olivetti_faces(X[-10:], y[-10:], ncol=5)

    # 데이터(X), 타겟(y)를
    # 훈련 셋(X_train, y_train): 280개 샘플
    # 검증 셋(X_val, y_val): 80개 샘플
    # 테스트 셋(X_test, y_test): 40개 샘플
    # 계층적 샘플링(stratified) 방식으로 나눔.

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

    print(np.unique(y_train, return_counts=True))
    print(np.unique(y_val, return_counts=True))
    print(np.unique(y_test, return_counts=True))
    # train/validataion/test 셋으로 나눠짐.
    # 모든 클래스들(0 ~ 39)이 같은 비율로 나눠짐. - stratified sampling

    # PCA(Principal Components Analysis, 주성분 분석) - 차원 축소
    # 머신 러닝 알고리즘을 적용하기 전에 학습/테스트 시간을 줄이기 위해서,
    # 또는 머신 러닝 알고리즘의 성능을 개선하기 위해서, 전처리 과정에서
    # 너무 많은 특성의 개수를 줄여서(차원을 축소해서) 시도.

    # 원본 데이터 분산의 99%를 설명할 수 있는 주성분 분석을 하세요.
    # X_train, X_val, X_test 셋을 모두 변환.
    pca = PCA(n_components=0.99, random_state=1)  # 모델 생성
    X_train_pca = pca.fit_transform(X_train)  # 모델 훈련/변환
    X_val_pca = pca.transform(X_val)  # 변환
    X_test_pca = pca.transform(X_test)

    print('주성분(PC) 개수:', pca.n_components_)
    print(X_train_pca.shape, X_val_pca.shape, X_test_pca.shape)

    # 차원이 축소된 훈련 셋(X_train_pca)을 사용하고,
    # KMeans 알고리즘을 적용해서 최적 클러스터 개수를 찾아보세요.
    # k값을 변경하면서 KMeans를 생성하고, inertia, silhouette score 값 찾음.
    k_values = range(5, 150, 5)  # cluster 개수 = 5, 10, 15, 20, ...
    kmeans_models = []  # 각 k값에 해당하는 KMeans 모델들을 저장할 리스트
    inertias = []  # 각 k값에 해당하는 inertia 값들을 저장할 리스트
    silhouettes = []  # 각 k값에 해당하는 실루엣 점수들을 저장할 리스트
    for k in k_values:
        kmeans = KMeans(n_clusters=k, random_state=1)
        t_start = time.time()  # fit 시작 시간 측정
        kmeans.fit(X_train_pca)
        t_end = time.time()  # fit 종료 시간 측정
        print(f'k={k}: {t_end - t_start} seconds')
        kmeans_models.append(kmeans)
        inertias.append(kmeans.inertia_)
        ss = silhouette_score(X_train_pca, kmeans.labels_)
        silhouettes.append(ss)

    # 하나의 figure에 k-inertia, k-실루엣 점수 그래프를 그려보세요.
    plt.subplot(1, 2, 1)  # nrow, ncol, index
    plt.plot(k_values, inertias, marker='o')
    plt.xlabel('k')
    plt.ylabel('inertia')

    plt.subplot(1, 2, 2)
    plt.plot(k_values, silhouettes, marker='o')
    plt.xlabel('k')
    plt.ylabel('silhouette score')
    plt.show()

    # 실루엣 점수가 최대인 k값을 찾아보세요.
    best_index = np.argmax(silhouettes)  # 실루엣 점수 최댓값의 인덱스
    best_k = k_values[best_index]  # 실루엣 점수가 최대인 k 값
    best_score = silhouettes[best_index]  # 실루엣 점수 최댓값
    print(f'best k: {best_k}, best silhouette score: {best_score}')

    # best k = 115 을 사용한 모델에서 찾은 클러스트들을 조사
    best_model = kmeans_models[best_index]
    print('best model:', best_model)
    print('labels:', best_model.labels_, best_model.labels_.shape)
    # model.labels_: KMeans 알고리즘이 학습 셋을 분류한 클러스터들
    clusters = np.unique(best_model.labels_)  # 중복되지 않은 클러스터 번호

    # 훈련 셋(X_train)에서 cluster 0으로 분류된 이미지들을 찾고,
    # 그래프로 그려보세요.
    cluster_0 = (best_model.labels_ == 0)
    faces_0 = X_train[cluster_0]
    label_0 = y_train[cluster_0]
    plot_olivetti_faces(faces_0, label_0)

    # cluster 1 ~ cluster 9으로 분류된 얼굴 사진들을 그래프로 그려 보세요.
    for cluster_id in range(1, 10):
        # cluseter n의 인덱스들
        cluster_n = (best_model.labels_ == cluster_id)
        faces = X_train[cluster_n]  # cluster n으로 분류된 얼굴 사진들
        labels = y_train[cluster_n]  # cluster n으로 분류된 사진 레이블
        plot_olivetti_faces(faces, labels)

    # k=40, 50일 때, model.labels_ 클러스터에 속한 이미지들을 조사.

    # 차원 축소된 학습 셋(X_train_pca)을 지도 학습 모델인
    # LogisticRegression, RandomForestClassier 알고리즘으로 훈련.
    # 검증 셋(X_val_pca)에서 정확도를 비교.
    clf1 = LogisticRegression(random_state=1, max_iter=1_000)
    clf1.fit(X_train_pca, y_train)
    acc1 = clf1.score(X_val_pca, y_val)
    print('Logistic Regression acc:', acc1)  # 0.9625
    # Log_Reg에서 max_iter(=1000) 변경 후 테스트  -> 0.9625

    clf2 = RandomForestClassifier(random_state=1, n_estimators=150)
    clf2.fit(X_train_pca, y_train)
    acc2 = clf2.score(X_val_pca, y_val)
    print('Random Forest acc:', acc2)  # 0.9
    # R.F.에서 n_estimators(=150)를 변경 후 테스트 -> 0.9375

    # PCA(주성분 분석 -> 차원 축소), KMeans(클러스터링)를 전처리 과정에서 사용
    # Logistic Regression, Random Forest 분류기의 정확도 비교
    # Pipeline(PCA -> KMeans -> Classifier).fit, score
    model = Pipeline([
        ('pca', PCA(n_components=0.99, random_state=1)),
        ('kmeans', KMeans(n_clusters=best_k, random_state=1)),
        ('classifier', LogisticRegression(random_state=1, max_iter=1000))
    ])
    model.fit(X_train, y_train)
    acc = model.score(X_val, y_val)
    print('Logistic Regression with KMeans acc:', acc)  # 0.925

    model2 = Pipeline([
        ('pca', PCA(n_components=0.99, random_state=1)),
        ('kmeans', KMeans(n_clusters=best_k, random_state=1)),
        ('classifier', RandomForestClassifier(n_estimators=150, random_state=1))
    ])
    model2.fit(X_train, y_train)
    acc2 = model2.score(X_val, y_val)
    print('Random Forest with KMeans acc:', acc2)  # 0.7875

    # k 값을 변경하면서, 여러가지 KMeans 알고리즘을
    # Random Forest의 전처리 단계로 사용하면 테스트
    scores = []
    for k in range(5, 150, 5):
        # Pipeline(PCA -> KMeans(k) -> R.F).fit & score
        model = Pipeline([
            ('pca', PCA(n_components=0.99, random_state=1)),
            ('kmeans', KMeans(n_clusters=k, random_state=1)),
            ('classifier', RandomForestClassifier(n_estimators=150,
                                                  random_state=1))
        ])
        model.fit(X_train, y_train)
        acc = model.score(X_val, y_val)
        scores.append(acc)
        print(f'k={k}, score: {acc}')

    max_index = np.argmax(scores)  # 모델 점수(정확도) 최댓값 위치(인덱스)
    print(k_values[max_index], scores[max_index])  # np.max(scores)

    # k-scores 그래프
    plt.plot(k_values, scores, marker='o')
    plt.show()
