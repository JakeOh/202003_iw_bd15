# Randomized PCA과 PCA의 시간 차이
# 1) 특성(feature) 개수는 일정하고, 샘플의 개수가 달라질 때
# 2) 샘플 개수(row)는 일정하고, 특성의 개수가 달라질 때
import time

import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA

if __name__ == '__main__':
    rpca_times = []  # Randomized PCA에서 측정한 시간들을 저장할 리스트
    pca_times = []  # PCA에서 측정한 시간들을 저장할 리스트

    # 1) 특성(feature) 개수는 일정하고, 샘플의 개수가 달라질 때
    sample_sizes = [1_000, 10_000, 20_000, 30_000, 40_000,
                    50_000, 70_000, 100_000, 200_000, 500_000,
                    1_000_000]
    np.random.seed(42)
    for n_samples in sample_sizes:
        # 특성 개수가 5개인 가상의 (더미) 데이터 생성
        X = np.random.randn(n_samples, 5)
        # randomize PCA(주성분 분석): 5차원 -> 2차원 축소
        rpca = PCA(n_components=2, svd_solver='randomized',
                   random_state=42)
        t_start = time.time()
        rpca.fit(X)
        t_end = time.time()
        rpca_times.append(t_end - t_start)

        pca = PCA(n_components=2, svd_solver='auto', random_state=42)
        t_start = time.time()
        pca.fit(X)
        t_end = time.time()
        pca_times.append(t_end - t_start)

    plt.plot(sample_sizes, rpca_times,
             color='blue', ls='solid', lw=2, marker='o',
             label='Randomized PCA')
    plt.plot(sample_sizes, pca_times,
             color='red', ls='solid', lw=2, marker='s',
             label='PCA')
    plt.legend()
    plt.xlabel('# of samples')
    plt.ylabel('time')
    plt.show()

    # 2) 샘플 개수(row)는 일정하고, 특성의 개수가 달라질 때
    rpca_times = []
    pca_times = []
    feature_sizes = [1_000, 2_000, 3_000, 4_000, 5_000, 6_000]
    # 샘플 개수는 2,000개로 고정, 특성 개수를 위와 같이 바꾸면서
    # Randomized PCA, PCA의 시간 차이를 측정, 그래프로 그림.
    for n_features in feature_sizes:
        # 샘플 개수가 2,000개인 더미 데이터
        X = np.random.randn(2_000, n_features)

        rpca = PCA(n_components=2, svd_solver='randomized',
                   random_state=42)
        t_start = time.time()
        rpca.fit(X)
        t_end = time.time()
        rpca_times.append(t_end - t_start)

        pca = PCA(n_components=2, svd_solver='auto', random_state=42)
        t_start = time.time()
        pca.fit(X)
        t_end = time.time()
        pca_times.append(t_end - t_start)

    plt.plot(feature_sizes, rpca_times,
             color='blue', ls='solid', lw=2, marker='o',
             label='Randomized PCA')
    plt.plot(feature_sizes, pca_times,
             color='red', ls='solid', lw=2, marker='s',
             label='PCA')
    plt.legend()
    plt.xlabel('# of features')
    plt.ylabel('time')
    plt.show()

