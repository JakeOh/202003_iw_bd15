# 규제(Regularization):
#   모델을 훈련할 때, 비용 함수(cost function, J)에 항을 추가해서
#   일부러 에러를 키우는 방법
#   -> 훈련 세트에 대해서 에러가 커지기 때문에 과적합을 줄일 수 있음.
# 1) Ridge 규제(l2 규제): MSE + alpha * l2-norm
#   l2-norm: theta**2
#   각 계수들을 줄여주는 효과
# 2) Lasso 규제(l1 규제): MSE + alpha * l1-norm
#   l1-norm: | theta |
#   몇 개의 중요한 특성들만 남고, 중요하지 않은 많은 변수들의 계수들은 0이 됨.
# 3) Elastic Net: Ridge(l2)와 Lasso(l1)의 혼합

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import Ridge, Lasso, LinearRegression, SGDRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

if __name__ == '__main__':
    np.random.seed(1)

    m = 50
    X = 3 * np.random.rand(m, 1)
    y = 1 + 2 * X + np.random.randn(m, 1)

    # plt.scatter(X, y)
    # plt.show()

    X_new = np.linspace(0, 3, 1000).reshape((1000, 1))

    # Ridge 규제(l2 규제)
    alphas = (0, 1, 10, 100)  # l2 규제에서 사용할 alpha 값들
    for alpha in alphas:
        model = Ridge(alpha=alpha, random_state=1)  # 모델 선택
        model.fit(X, y)  # 모델 훈련(y = theta0 + theta1 * X)
        print(f'*** alpha = {alpha} ***')
        print(model.intercept_, model.coef_)
        y_new_pred = model.predict(X_new)
        plt.plot(X_new, y_new_pred, label=f'alpha={alpha}')

    print('mean y =', np.mean(y))
    plt.scatter(X, y, color='gray')
    plt.legend()
    plt.show()

    print()
    # alphas = (0, 1e-5, 0.1, 1)  # Ridge
    alphas = (0, 1e-7, 1e-5, 1e-3)  # Lasso
    # PolynomialFeatures를 사용해서 degree=10의 Ridge 결과 그래프
    for alpha in alphas:
        poly_features = PolynomialFeatures(degree=10, include_bias=False)
        scaler = StandardScaler()
        # model = Ridge(alpha=alpha, random_state=1)
        if alpha == 0:
            model = LinearRegression()
        else:
            model = Lasso(alpha=alpha, random_state=1, tol=1)
        poly_model = Pipeline([
            ('poly', poly_features),
            ('scaler', scaler),
            ('regular', model)
        ])
        poly_model.fit(X, y)
        print(f'*** alpha={alpha} ***')
        print(model.coef_)
        y_new_pred = poly_model.predict(X_new)
        plt.plot(X_new, y_new_pred, label=f'alpha={alpha}')

    plt.scatter(X, y, color='darkgray')
    plt.legend()
    plt.show()

    print()
    sgd_reg = SGDRegressor()
