# Decision Tree - depth, leaf
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier

from ch06.ex01_tree import plot_decision_boundary

if __name__ == '__main__':
    X, y = datasets.make_moons(n_samples=100, noise=0.25, random_state=1)
    print(X.shape, y.shape)
    print(np.max(X, axis=0), np.min(X, axis=0))
    axes = [-1.5, 2.5, -1.5, 1.5]

    for depth in (2, 4, 8):
        clf1 = DecisionTreeClassifier(random_state=42,
                                      max_depth=depth)
        clf1.fit(X, y)
        plot_decision_boundary(clf1, X, y, axes)
        plt.show()

    for leaf in (1, 2, 4):
        clf2 = DecisionTreeClassifier(random_state=42,
                                      min_samples_leaf=leaf)
        # min_samples_leaf: 최종 노드(leaf)이 가져야할 가장 작은 샘플 개수
        clf2.fit(X, y)
        plot_decision_boundary(clf2, X, y, axes)
        plt.title(f'Leaf {leaf}')
        plt.show()





