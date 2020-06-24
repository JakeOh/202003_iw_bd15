import numpy as np
from sklearn.datasets import make_swiss_roll
from sklearn.decomposition import KernelPCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

if __name__ == '__main__':
    # Kernel PCA를 사용할 때 kernel='rbf' 또는 'sigmoid'인 경우,
    # gamma 값을 설정하기 위한 GridSearchCV 방법
    X, y = make_swiss_roll(n_samples=1000, noise=0.2, random_state=1)
    # 분류 문제라고 가정 -
    # y가 원래는 연속적인 값인데, y를 레이블(클래스)로 변환
    y = (y > 7.0).astype(np.int)
    print(y[:5])

    # 차원 축소 -> 분류/회귀 알고리즘 적용(fit, predict, score)
    clf = Pipeline([
        ('pca', KernelPCA(n_components=2, random_state=1)),
        ('classifier', LogisticRegression(random_state=1))
    ])

    # GridSearchCV를 하이퍼 파라미터 튜닝: kernel, gamma
    param_grid = [{
        'pca__kernel': ['rbg', 'sigmoid'],
        'pca__gamma': np.linspace(0.1, 0.5, 20)
    }]

    grid_search = GridSearchCV(estimator=clf,
                               param_grid=param_grid,
                               cv=3)
    grid_search.fit(X, y)
    print(grid_search.best_estimator_)
    print(grid_search.best_params_)


