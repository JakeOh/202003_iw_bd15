# Random Forest: estimator로 Decision Tree를 사용하는 Bagging 방법.
# RandomForest 클래스는 DecisionTree의 파라미터와 Bagging의 파라미터들을
# 설정할 수 있다.

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    # 데이터 셋 준비
    X, y = datasets.make_moons(n_samples=500, noise=0.3, random_state=42)
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=0.2, random_state=42)

    rand_forest = RandomForestClassifier(
        n_estimators=500, max_samples=100, n_jobs=-1, bootstrap=True,
        oob_score=True,
        # max_depth=3  # decision tree
    )
    rand_forest.fit(X_train, y_train)
    print('Random Forest oob score:', rand_forest.oob_score_)
    acc = rand_forest.score(X_test, y_test)
    print('Random Forest 정확도:', acc)

    # Extremely Randomized Trees Ensemble (Extra-Trees)
    # 랜덤 포레스트 방식에서 트리들을 만들 때,
    # gini 계수 또는 다른 criterion을 이용해서 트리를 만드는 것이 아니라,
    # 완전 무작위하게 만든 트리들로 앙상블 학습을 시키는 방법.
    # Extra-Trees의 장점은 훈련 시간이 랜덤 포레스트보다 작다는 것.
    # 사용 방법은 RandomForest와 동일.
    extra_trees_clf = ExtraTreesClassifier(
        n_estimators=500, max_samples=100, n_jobs=-1, bootstrap=True,
        oob_score=True
    )
    extra_trees_clf.fit(X_train, y_train)
    print('Extra-Trees oob score:', extra_trees_clf.oob_score_)
    acc = extra_trees_clf.score(X_test, y_test)
    print('Extra-Trees 정확도:', acc)








