"""
앙상블(ensemble): 학습에 사용되는 일련의 모델(알고리즘)들.
앙상블 학습 방법(Ensemble Method): 앙상블을 사용한 학습 방법.
1) 투표(voting):
    서로 다른 알고리즘을 학습시켜서, 각각의 예측값을 투표(다수결)로 예측하는 방법.
2) Bagging(Bootstrap Aggregating)과 Pasting:
    중복을 허용(bagging)하거나 또는 중복을 허용하지 않고(pasting) 샘플링한
    학습(훈련) 셋의 부분집합들을 하나의 알고리즘에 학습시켜서 예측(다수결, 평균).
3) Random Forest: Bagging 방법을 적용한 Decision Tree 앙상블 학습 방법.
"""

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

if __name__ == '__main__':
    # 데이터 셋 준비
    X, y = datasets.make_moons(n_samples=500, noise=0.3,
                               random_state=42)
    print(X.shape, y.shape)

    # Train/Test 분리
    X_train, X_test, y_train, y_test =\
        train_test_split(X, y, test_size=0.2, random_state=42)

    # 데이터 셋 시각화
    class0 = (y == 0)
    class1 = (y == 1)
    plt.scatter(X[class0, 0], X[class0, 1], c='blue',
                marker='s', label='Class 0')
    plt.scatter(X[class1, 0], X[class1, 1], c='green',
                marker='^', label='Class 1')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.legend()
    plt.show()

    # 분류기(classifier) 모델들 생성
    logistic = LogisticRegression(random_state=42)
    sgd = SGDClassifier(random_state=42, loss='log')
    svc = SVC(random_state=42, probability=True)
    tree_clf = DecisionTreeClassifier(random_state=42)
    rand_forest = RandomForestClassifier(random_state=42)

    classifiers = (logistic, sgd, svc, tree_clf, rand_forest)
    for classifier in classifiers:
        # 각각의 모델을 학습
        classifier.fit(X_train, y_train)
        # 정확도(accuracy) - 각 모델의 score() 메서드 호출
        acc = classifier.score(X_test, y_test)
        print(classifier.__class__.__name__, ':', acc)

    # 앙상블 학습 방법 중에서 hard 투표 방식 - 다수결
    voting_clf = VotingClassifier(
        estimators=[('logistic', logistic),
                    ('sgd', sgd),
                    ('svc', svc),
                    ('tree', tree_clf),
                    ('rf', rand_forest)],
        voting='soft',  # 다수결 투표(hard), 가중치 투표(soft)
        n_jobs=-1
    )
    voting_clf.fit(X_train, y_train)
    acc = voting_clf.score(X_test, y_test)
    # accuracy_score(y_test, voting_clf.predict(X_test))
    print('VotingClassifier:', acc)

    # VotingClassifier의 voting='hard'(기본값), 'soft'
    # hard voting: 다수결 투표. 모든 분류기가 동일하게 1표씩 행사.
    # soft voting: 각 분류기의 예측값에 그 예측의 확률을 가중치로 곱한 값을 사용해서 예측.
    # 확률이 높은 예측값이 더 높은 가중치를 갖고 투표를 하게되는 방식.
    # soft voting을 사용하려면 모든 분류기가 확률을 계산할 수 있어야 함.
    # -> SVC인 경우는 모델을 생성할 때, probability=True로 설정해야 함.
    # -> SGDClassifier인 경우 모델 생성할 때, loss='log'로 설정.


