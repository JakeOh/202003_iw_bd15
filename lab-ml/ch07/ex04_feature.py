import pickle

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    # RandomForest의 장점 중 하나는,
    # 특성(features, 변수)들의 중요도를 계산해 줌.
    iris = datasets.load_iris()  # dict
    X, y = iris['data'], iris['target']
    X_train, X_test, y_train, y_test =\
        train_test_split(X, y, test_size=0.2, random_state=42)

    # 모델 생성
    rand_forest = RandomForestClassifier(n_estimators=500,
                                         n_jobs=-1,
                                         random_state=42)

    # 모델 학습 - 학습 데이터에 fitting
    rand_forest.fit(X_train, y_train)

    # 학습 데이터 특성들의 중요도
    print(rand_forest.feature_importances_)
    # feature_name:feature_importance 함께 출력 - for문 사용
    for f_name, f_imp in zip(iris.feature_names,
                             rand_forest.feature_importances_):
        print(f_name, ':', f_imp)

    # MNIST 데이터(28x28 pixel = 784 features)의 중요도
    with open('../ch03/mnist.pkl', mode='rb') as file:
        mnist = pickle.load(file)
    X, y = mnist['data'], mnist['target']
    print(X.shape, y.shape)

    # RandomForestClassifier를 생성, 데이터 X를 학습
    clf = RandomForestClassifier(n_estimators=10, n_jobs=-1,
                                 random_state=42)
    clf.fit(X, y)
    print(clf.feature_importances_.shape)
    img = clf.feature_importances_.reshape((28, 28))
    plt.imshow(img, cmap=plt.cm.hot)
    plt.show()







