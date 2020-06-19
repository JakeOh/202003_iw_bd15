import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeRegressor


def plot_prediction(regressors, X, y, axes):
    # 데이터 시각화
    plt.scatter(X, y, c='blue')
    # 예측 곡선 시각화
    x_min, x_max = axes[0], axes[1]
    X_test = np.linspace(x_min, x_max, 100).reshape((-1, 1))
    y_pred = sum(reg.predict(X_test) for reg in regressors)
    plt.plot(X_test, y_pred, 'r-', lw=2)  # 색깔:red, 모양:solid, 두께:2
    plt.axis(axes)


if __name__ == '__main__':
    np.random.seed(42)
    m = 100  # 샘플 개수
    # -0.5 <= X < 0.5 범위의 난수 100개
    X = np.random.rand(m, 1) - 0.5
    # y = 3 * X**2 + error
    y = 3 * X[:, 0]**2 + 0.05 * np.random.randn(m)

    # plot_prediction(None, X, y, None)
    # plt.show()
    axes = [-0.5, 0.5, -0.1, 0.8]

    # Gradient Boost
    # 1) 모델 선택, 모델을 학습 셋에 fitting(훈련)
    tree_reg1 = DecisionTreeRegressor(max_depth=2, random_state=42)
    tree_reg1.fit(X, y)
    plot_prediction([tree_reg1], X, y, axes)
    plt.show()

    # 2) 첫번째 학습에서의 예측값과 실제값의 차이(residual error)에 모델을 학습
    y2 = y - tree_reg1.predict(X)  # residual error(잔차)
    tree_reg2 = DecisionTreeRegressor(max_depth=2, random_state=42)
    tree_reg2.fit(X, y2)

    axes_residual = [-0.5, 0.5, -0.5, 0.5]
    plot_prediction([tree_reg2], X, y2, axes_residual)
    plt.show()

    plot_prediction([tree_reg1, tree_reg2], X, y, axes)
    plt.show()

    # 3) 두번째 학습에서의 예측값과 (두번째 학습에서의) 실제값의 차이에 모델을 학습
    y3 = y2 - tree_reg2.predict(X)
    tree_reg3 = DecisionTreeRegressor(max_depth=2, random_state=42)
    tree_reg3.fit(X, y3)

    plot_prediction([tree_reg3], X, y3, axes_residual)
    plt.show()

    plot_prediction([tree_reg1, tree_reg2, tree_reg3],
                    X, y, axes)
    plt.show()

    # 4) 훈련되지 않은 테스트 데이터에 대한 예측값을 계산:
    # 위에서 훈련된 모든 예측기(모델)가 각각 예측하는 값들을 모두 더함.
    X_test = np.array([[0.3]])
    tree_regressors = (tree_reg1, tree_reg2, tree_reg3)
    y_pred = sum(reg.predict(X_test) for reg in tree_regressors)
    print('y_pred:', y_pred)
