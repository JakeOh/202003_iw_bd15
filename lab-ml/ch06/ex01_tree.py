# Decision Tree(의사 결정 나무) - 분류, 회귀

import matplotlib.pyplot as plt
import numpy as np
import pydotplus
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier, export_graphviz


def plot_decision_boundary(clf, X, y, axes=[0, 7.5, 0, 3]):
    # Data를 scatter plot: x축(petal length), y축(petal width)
    plt.scatter(X[y == 0, 0], X[y == 0, 1], c='r')
    plt.scatter(X[y == 1, 0], X[y == 1, 1], c='b')
    plt.scatter(X[y == 2, 0], X[y == 2, 1], c='g')
    # decision boundary(결정 경계)
    x_pts = np.linspace(axes[0], axes[1], 100)
    y_pts = np.linspace(axes[2], axes[3], 100)
    X_pts, Y_pts = np.meshgrid(x_pts, y_pts)
    X_new = np.c_[X_pts.ravel(), Y_pts.ravel()]  # 예측할 때 사용할 데이터
    predicts = clf.predict(X_new).reshape(X_pts.shape)  # ML 모델의 예측값
    cust_cmap = ListedColormap(['pink', 'aqua', 'greenyellow'])
    plt.contourf(X_pts, Y_pts, predicts, cmap=cust_cmap, alpha=0.3)


if __name__ == '__main__':
    # 데이터 준비
    iris = datasets.load_iris()
    X = iris.data[:, (2, 3)]  # petal length, width 특성 선택
    y = iris.target

    # 모델 선택, 생성
    tree_clf = DecisionTreeClassifier(random_state=1)
    # 모델을 학습 데이터에 fitting - 훈련(학습)
    tree_clf.fit(X, y)
    # 평가
    tree_score = tree_clf.score(X, y)  # 정확도(accuracy)
    print('tree score:', tree_score)

    y_pred = tree_clf.predict(X)  # 예측값
    conf_mat = confusion_matrix(y, y_pred)
    print(conf_mat)
    report = classification_report(y, y_pred,
                                   target_names=iris.target_names)
    print(report)

    # Decision Tree의 내용을 그래프로 만들고 저장하기 위해 필요한 패키지
    # graphviz - decision tree를 그래프 객체로 만듦.
    # pydotplus - graphviz가 만든 객체를 파일, 이미지로 저장.
    # 설치방법 1)
    #   conda install 패키지이름
    # 설치방법 2)
    #   PyCharm -> File -> Settings -> Project -> Project Interpreter
    # -> +버튼 -> 패키지 이름 검색, 설치
    # 패키지 설치 이후에 graphviz가 설치된 폴더를 환경 설정 경로(path)에 추가
    # 환경 설정 변경 이후에는 PyCharm을 다시 실행

    export_graphviz(tree_clf,
                    out_file='iris.dot',
                    feature_names=iris.feature_names[2:],
                    class_names=iris.target_names,
                    filled=True)
    graph = pydotplus.graph_from_dot_file('iris.dot')
    graph.write_png('iris.png')

    tree_clf2 = DecisionTreeClassifier(random_state=1, max_depth=2)
    tree_clf2.fit(X, y)
    print('tree_clf2 score:', tree_clf2.score(X, y))
    export_graphviz(tree_clf2,
                    out_file='iris_depth2.dot',
                    feature_names=iris.feature_names[2:],
                    class_names=iris.target_names,
                    filled=True)
    g = pydotplus.graph_from_dot_file('iris_depth2.dot')
    g.write_png('iris_depth2.png')

    print('g0 =', 1 - (1/3)**2 * 3)

    tree_clf3 = DecisionTreeClassifier(random_state=42,
                                       max_depth=2)
    tree_clf3.fit(X, y)
    print('tree_clf3 score:', tree_clf3.score(X, y))
    export_graphviz(tree_clf3,
                    out_file='iris_depth2_42.dot',
                    feature_names=iris.feature_names[2:],
                    class_names=iris.target_names,
                    filled=True)
    g = pydotplus.graph_from_dot_file('iris_depth2_42.dot')
    g.write_png('iris_depth2_42.png')

    plot_decision_boundary(tree_clf2, X, y)
    plt.show()

    plot_decision_boundary(tree_clf3, X, y)
    plt.show()

    plot_decision_boundary(tree_clf, X, y)
    plt.show()

