import matplotlib.pyplot as plt
import numpy as np
import pydotplus
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor, export_graphviz

if __name__ == '__main__':
    np.random.seed(1)

    m = 200  # 샘플 개수(row 개수)
    X = np.random.rand(m, 1)  # 0 <= X < 1 범위의 (200, 1) shape의 난수들
    y = (4 * (X - 0.5)**2 + np.random.randn(m, 1) / 10).ravel()  # (200,)

    # plt.scatter(X, y)
    # plt.show()

    # 결정 트리 회귀(Decision Tree Regression)
    tree_reg = DecisionTreeRegressor(random_state=1,
                                     max_depth=3)
    tree_reg.fit(X, y)
    # 회귀 평가 지표:
    #   1) R2 점수: 1에 가까울 수록 좋은 점수
    #   2) RMSE, MSE: 0에 가까울 수록 좋은 점수
    print('R2 score:', tree_reg.score(X, y))

    y_pred = tree_reg.predict(X)
    tree_mse = mean_squared_error(y, y_pred)
    tree_rmse = np.sqrt(tree_mse)
    print('RMSE:', tree_rmse)

    export_graphviz(tree_reg, out_file='test.dot', filled=True)
    g = pydotplus.graph_from_dot_file('test.dot')
    g.write_png('test.png')
