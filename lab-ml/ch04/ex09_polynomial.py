import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.preprocessing import PolynomialFeatures

if __name__ == '__main__':
    np.random.seed(1)

    # 특성(독립 변수)가 여러개인 선형 회귀(Linear Regression)
    m = 100
    income = 10 * np.random.rand(m, 1)  # 0 <= income < 10
    room = 3 * np.random.rand(m, 1)  # 0 <= room < 3
    X = np.c_[income, room]  # (100, 2) 2d array
    print(X[:5])

    y = 3 + 2 * income + 5 * room + np.random.randn(m, 1)
    # y = 3 + 2 * x_1 + 5 * x_2 + error

    lin_reg = LinearRegression()  # 모델(알고리즘) 선택
    lin_reg.fit(X, y)  # 모델 학습 - 선형 회귀식의 계수들을 찾음.
    # y = theta0 + theta1 * income + theta2 * room 선형 회귀식(가설)의
    # MSE(Mean Squared Errors)가 최소가 되는 계수들을 찾음.
    print(f'bias: {lin_reg.intercept_}, weight: {lin_reg.coef_}')

    X_new = [[5.5, 2.5]]  # 새로운 데이터 -> 예측값
    y_predict = lin_reg.predict(X_new)
    print('predict =', y_predict)
    print(lin_reg.intercept_
          + lin_reg.coef_[0, 0] * 5.5
          + lin_reg.coef_[0, 1] * 2.5)

    sgd_reg = SGDRegressor(penalty=None)
    sgd_reg.fit(X, y.ravel())
    print(f'bias: {sgd_reg.intercept_}, weight: {sgd_reg.coef_}')

    # 다항 회귀(polynomial regression)
    # 여러개의 특성(독립 변수)들에 대해서 다차항(2차 이상인 항)을 갖는 회귀 식
    # y = theta0 + theta1 * X + theta2 * X**2 + ...
    # y = theta1 + theta1 * X1 + theta2 * X1**2 + theta3 * X2 + theta4 * X2**2 + theta5 * X1 * X2

    X = 6 * np.random.rand(m, 1) - 3  # -3 <= X < 3인 난수 100개
    y = 2 + 0.5 * X**2 + X + np.random.randn(m, 1)

    # plt.scatter(X, y)
    # plt.show()

    # 선형 회귀: y = theta0 + theta1 * X
    # 다항 회귀: y = theta0 + theta1 * X + theta2 * X**2
    X_poly = np.c_[X, X**2]  # (100, 2)인 2d array
    lin_reg = LinearRegression()
    lin_reg.fit(X_poly, y)
    print(lin_reg.intercept_, lin_reg.coef_)

    # 예측
    X_new = np.linspace(-3, 3, 1000)
    y_pred = lin_reg.predict(np.c_[X_new, X_new**2])
    plt.plot(X_new, y_pred, 'r-')  # 'r-': color='red', linestyle='solid'
    plt.scatter(X, y)
    plt.show()

    # 다차항(2차항 이상)들을 추가해서 모델 훈련
    poly_features = PolynomialFeatures(degree=2, include_bias=False)
    X_poly2 = poly_features.fit_transform(X)
    print(X_poly2[:5])

    sgd_reg = SGDRegressor()
    sgd_reg.fit(X_poly2, y.ravel())
    theta0 = sgd_reg.intercept_[0]
    theta1, theta2 = sgd_reg.coef_
    print(theta0, theta1, theta2)

    y_pred = theta0 + theta1 * X_new + theta2 * X_new**2
    plt.plot(X_new, y_pred, 'r-', linewidth=2)
    plt.scatter(X, y)
    plt.show()


