# PCA(Principal Component Analysis, 주성분 분해)
# SVD(Singularity Value Decomposition, 특잇값 분해) 행렬 방정식 품(solve).
# PCA 매개변수 svd_solver를 지정하면, 풀이 방식을 변경.
# full: 선형 대수(행렬식), randomized: 근사값
import pickle
import time

import numpy as np
from sklearn.decomposition import PCA, IncrementalPCA
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    with open('../ch03/mnist.pkl', mode='rb') as file:
        mnist = pickle.load(file)

    X = mnist['data']
    y = mnist['target'].astype(np.int)

    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=0.2, random_state=1)

    # 주성분 분석에 사용할 PCA 객체들을 생성
    n_pc = 500
    auto_pca = PCA(n_components=n_pc, svd_solver='auto')  # auto: 기본값
    rand_pca = PCA(n_components=n_pc, svd_solver='randomized')  # 근사값
    full_pca = PCA(n_components=n_pc, svd_solver='full')  # 선형 대수
    inc_pca = IncrementalPCA(n_components=n_pc, batch_size=560)
    for pca in (auto_pca, rand_pca, full_pca, inc_pca):
        t_start = time.time()  # fit 시작 시간 측정
        pca.fit(X_train)
        t_end = time.time()  # fit 종료 시간 측정
        print('경과 시간:', (t_end - t_start))

