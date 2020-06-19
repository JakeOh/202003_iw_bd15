'''
앙상블 학습(Ensemble Learning) 방법:
1. Voting(투표): 여러개 모델(알고리즘). 한개의 훈련 셋. hard/soft 투표.
2. Bagging(Bootstrap Aggregating): 한개 모델. 훈련 셋을 여러개의 서브셋. 투표.
    서브셋: 중복 허용/불허
3. Random Forest: Bagging을 적용한 Decision Tree 앙상블 학습 방법.
4. Boosting: 약한 학습기 여러개를 순차적으로(sequentially) 연결해서 강한 학습기를
만드는 방법.
    1) AdaBoost(Adaptive Boosting):
    이전 학습에서 underfit된 샘플들에 가중치를 높게 줘서 다음 학습에서 사용하는 방법.
    2) Gradient Boost:
    이전 학습에서 발생한 오차(residual error)를 다음 훈련에서 학습.
    Boosting 방식의 단점: 훈련을 병렬적으로 시킬 수가 없어서 시간이 오래 걸릴 수 있음.
'''
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def plot_decision_boundary(clf, X, y, axes=[-1.5, 2.5, -1, 1.5]):
    class_0, class_1 = (y == 0), (y == 1)
    plt.scatter(X[class_0, 0], X[class_0, 1], c='green',
                marker='s', alpha=0.8)
    plt.scatter(X[class_1, 0], X[class_1, 1], c='blue',
                marker='^', alpha=0.8)

    x_min, x_max, y_min, y_max = axes
    x_pts = np.linspace(x_min, x_max, 100)
    y_pts = np.linspace(y_min, y_max, 100)
    x, y = np.meshgrid(x_pts, y_pts)
    X_new = np.c_[x.ravel(), y.ravel()]
    predicts = clf.predict(X_new).reshape(x.shape)
    color_map = ListedColormap(['lemonchiffon', 'lavender', 'lightcyan'])
    plt.contourf(x, y, predicts, cmap=color_map, alpha=0.8)
    plt.axis(axes)


if __name__ == '__main__':
    X, y = datasets.make_moons(n_samples=500, noise=0.3, random_state=42)
    X_train, X_test, y_train, y_test =\
        train_test_split(X, y, test_size=0.2, random_state=42)

    for lr in (0.1, 0.2, 0.3, 0.5):
        ada_clf = AdaBoostClassifier(
            base_estimator=DecisionTreeClassifier(max_depth=2),
            n_estimators=50,
            learning_rate=lr,
            algorithm='SAMME.R',  # underfit된 샘플들에게 가중치를 주는 알고리즘.
            random_state=42
        )
        ada_clf.fit(X_train, y_train)
        train_score = ada_clf.score(X_train, y_train)  # 정확도
        test_score = ada_clf.score(X_test, y_test)
        print(f'===== Learning Rate = {lr} =====')
        print('Train Score:', train_score)
        print('Test Score:', test_score)
        plot_decision_boundary(ada_clf, X_train, y_train)
        plt.show()









