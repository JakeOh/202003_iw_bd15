'''
앙상블 학습 방법: 다양한(여러개의) 분류기/회귀 모델을 만들어서 학습하는 방법
다양한 모델을 만드는 방법:
    1) 여러개의 다른 알고리즘을 생성, 학습. -> Voting
    2) 같은 알고리즘을 사용하되, 학습 셋을 무작위로 부분집합으로 나눠서 학습.
    -> Bagging, Pasting
학습 셋을 부분집합으로 무작위하게 나누는 방법:
    1) 학습 셋에서 샘플링할 때마다 중복을 허용하는 경우 - Bagging(Boost Aggregation)
    2) 학습 셋에서 샘플링할 때마다 중복을 허용하지 않는 경우 - Pasting
'''

from sklearn import datasets
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

if __name__ == '__main__':
    X, y = datasets.make_moons(n_samples=500, noise=0.3, random_state=42)
    X_train, X_test, y_train, y_test =\
        train_test_split(X, y, test_size=0.2, random_state=42)

    # 결정 트리 분류기 생성, X_train 학습 -> X_test의 score 계산
    tree_clf = DecisionTreeClassifier(random_state=42)
    tree_clf.fit(X_train, y_train)
    acc = tree_clf.score(X_test, y_test)
    print('Decision Tree 정확도:', acc)

    # Bagging(Bootstrap Aggregating) 분류기
    bagging_clf = BaggingClassifier(
        base_estimator=DecisionTreeClassifier(random_state=42),
        # base_estimator: 기본 추정기(예측기). 알고리즘. 모델.
        n_estimators=500,  # 추정기 개수. 학습 셋의 부분집합 개수. 학습 횟수.
        max_samples=100,  # 학습 셋 부분집합의 최대 원소 개수.
        # max_samples: 정수(원소 개수), 실수(전체 학습 셋에서 부분집합의 비율)
        bootstrap=True,  # 샘플링할 때 중복 허용(True), 중복 불허(False)
        n_jobs=-1,  # 멀티 태스크 개수. -1: CPU 허용하는 모든 코어 사용.
        random_state=42
    )
    # bagging 분류기 훈련(학습)
    bagging_clf.fit(X_train, y_train)
    # 검증 세트에서 예측 점수 계산
    acc = bagging_clf.score(X_test, y_test)
    print('Bagging 정확도:', acc)

    # OOB(out-of-bagging) 인스턴스:
    # 학습 셋에서 무작위하게 부분집합을 만들 때, 한번도 부분집합에 포함되지 않은
    # 샘플들.
    # -> 모든 부분집합 어디에도 포함되지 않는 oob 인스턴스를
    # 검증(validation) 데이터로 사용할 수 있음.
    # oob_score=True로 설정하면, fitting 후 oob 인스턴스로 계산한 점수를
    # 얻을 수 있음.

    bagging_clf2 = BaggingClassifier(
        base_estimator=DecisionTreeClassifier(random_state=42),
        n_estimators=500,
        max_samples=100,
        bootstrap=True,
        oob_score=True,
        n_jobs=-1,
        random_state=42
    )
    bagging_clf2.fit(X_train, y_train)
    print('Bagging oob score:', bagging_clf2.oob_score_)
    acc = bagging_clf2.score(X_test, y_test)
    print('Bagging 정확도:', acc)
