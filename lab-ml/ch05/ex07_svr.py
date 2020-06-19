# SVM(Support Vector Machine)
# 회귀(Regression, 수치 예측): LinearSVR, SVR
# 분류(Classification): LinearSVC, SVC(kernel=linear/poly/rbf)

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.svm import LinearSVR, SVR


def plot_data(X, y):
    plt.scatter(X, y, c='gray')


def plot_svm_regression(model, axes, label):
    # model: 회귀 모델(LinearSVR, SVR, ...)
    # axes: [x_min, x_max]
    X = np.linspace(axes[0], axes[1], 100).reshape((-1, 1))  # (100,1)
    y = model.predict(X)
    plt.plot(X, y, label=label, lw=2)  # lw(linewidth)
    plt.legend()


if __name__ == '__main__':
    np.random.seed(1)

    m = 100  # 데이터 샘플 개수
    X = 2 * np.random.rand(m, 1)  # 0 <= X < 2의 (100, 1) shape의 난수
    y = (4 + 3 * X + np.random.randn(m, 1)).ravel()  # (100,) 1차원 배열
    # plot_data(X, y)
    # plt.show()

    reg1 = LinearSVR(random_state=1)
    reg1.fit(X, y)
    print(reg1.intercept_, reg1.coef_)
    y_pred = reg1.predict(X)
    reg1_mse = mean_squared_error(y_true=y, y_pred=y_pred)
    reg1_rmse = np.sqrt(reg1_mse)
    reg1_r2 = reg1.score(X, y)  # R2 score
    print(reg1_rmse, reg1_r2)

    # 데이터, 회귀 직선 그래프
    axes = [0, 2]
    plot_data(X, y)
    plot_svm_regression(reg1, axes, label='LinearSVR(e=0)')

    for e in [0.5, 1.0, 1.5]:
        reg2 = LinearSVR(random_state=1, epsilon=e)
        reg2.fit(X, y)
        plot_svm_regression(reg2, axes,
                            label=f'LinearSVR(e={e})')

    reg3 = SVR(kernel='linear')
    reg3.fit(X, y)
    plot_svm_regression(reg3, axes, label='SVR(e=0.1)')
    plt.show()

    # 다항 회귀(Polynomial Regression): LinearSVR, SVR
    axes = [-1, 1]
    X = 2 * np.random.rand(m, 1) - 1
    y = (0.2 + 0.1 * X + X**2 + np.random.randn(m, 1) / 10).ravel()
    plot_data(X, y)

    poly_reg1 = Pipeline([
        ('poly_features', PolynomialFeatures(degree=2, include_bias=False)),
        ('scaler', StandardScaler()),
        ('regressor', LinearSVR(random_state=1))
    ])
    poly_reg1.fit(X, y)
    plot_svm_regression(poly_reg1, axes, label='LinearSVR + PolyFeature')

    poly_reg2 = Pipeline([
        ('scaler', StandardScaler()),
        ('regressor', SVR(kernel='poly', degree=2))
    ])
    poly_reg2.fit(X, y)
    plot_svm_regression(poly_reg2, axes, label='SVR(kernel=poly)')

    plt.show()
