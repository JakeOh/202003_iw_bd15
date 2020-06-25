import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline

if __name__ == '__main__':
    # digits 데이터: 0 ~ 9 손글씨 숫자 이미지 데이터
    # digits = load_digits()
    # print(digits.keys())
    # print(digits.DESCR)
    X, y = load_digits(return_X_y=True)
    print(X.shape, y.shape)

    for i in range(9):
        # print(y[i])
        plt.subplot(3, 3, 1 + i)  # nrow, ncol, index
        image = X[i].reshape((8, 8))
        plt.imshow(image, cmap=plt.cm.binary)
        plt.axis('off')  # x축, y축을 제거
    plt.show()

    # 분류(classification) - Logistic Regression, SGDClassifier, SVC, RFC, ...
    # 전처리 없이, Train/Test 분리, Logistic Regression 훈련, Test 셋 점수
    X_train, X_test, y_train, y_test =\
        train_test_split(X, y, test_size=0.2, random_state=1)
    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

    log_reg = LogisticRegression(random_state=1,
                                 multi_class='ovr',
                                 max_iter=3_000,
                                 n_jobs=-1)
    log_reg.fit(X_train, y_train)
    score = log_reg.score(X_test, y_test)
    print('score:', round(score, 4))  # 97.5%

    # 군집(Clustering) 알고리즘 - 데이터 전처리(preprocessing)
    # KMeans와 LogisticRegression을 pipeline으로 연결해서 훈련.
    model = Pipeline([
        ('clusterer', KMeans(n_clusters=100, random_state=1)),
        ('regressor', LogisticRegression(random_state=1,
                                         multi_class='ovr',
                                         max_iter=5_000, n_jobs=-1))
    ])
    model.fit(X_train, y_train)  # 지도 학습 알고리즘 훈련
    score = model.score(X_test, y_test)
    print('KMeans 전처리 후 score:', score)
    # n_cluster=50: 98.06%, n_cluster=100: 97.5%

    # 적절한 k값을 찾기 위한 GridSearchCV을 수행
    grid_params = {'clusterer__n_clusters': range(10, 200, 10)}
    grid_search = GridSearchCV(estimator=model,
                               param_grid=grid_params,
                               cv=3,
                               verbose=2)
    grid_search.fit(X_train, y_train)
    print('best parameter:', grid_search.best_params_)
    print('best score:', grid_search.best_score_)
    # 훈련되지 않은 테스트 셋의 점수 계산
    print('GridSearchCV score:', grid_search.score(X_test, y_test))
    # best k = 70, 98.06%

    # KMeans 전처리 전/후 개선 효과
    print((1 - 0.975) / (1 - 0.9806))
