import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler


def plot_learning_curve(model, X, y):
    # model: 모델(알고리즘), X: 학습 데이터, y: 레이블(정답)
    # 학습 데이터를 학습 세트와 검증 세트로 나눔.
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2,
                                                        random_state=1)
    # 훈련/검증 세트의 성능(RMSE)을 저장하기 위한 리스트
    train_errors, test_errors = [], []
    # 훈련 세트의 데이터 개수만큼 반복
    for m in range(1, len(X_train)):
        model.fit(X_train[:m], y_train[:m])  # 모델 학습
        # 학습/검증 세트에서의 예측값 계산
        y_train_pred = model.predict(X_train[:m])
        y_test_pred = model.predict(X_test)
        train_mse = mean_squared_error(y_train[:m], y_train_pred)
        train_rmse = np.sqrt(train_mse)
        train_errors.append(train_rmse)
        test_mse = mean_squared_error(y_test, y_test_pred)
        test_rmse = np.sqrt(test_mse)
        test_errors.append(test_rmse)
    plt.plot(train_errors, color='red', label='Train RMSE')
    plt.plot(test_errors, color='blue', label='Test RMSE')
    plt.legend()
    plt.xlabel('Train set size')
    plt.ylabel('RMSE')


if __name__ == '__main__':
    np.random.seed(1)

    m = 100  # sample 개수
    X = 6 * np.random.rand(m, 1) - 3  # -3 <= X < 3
    y = 2 + X + 0.5 * X**2 + np.random.randn(m, 1)

    # plt.scatter(X, y)
    # plt.show()

    # 다항 회귀 곡선을 그리기 위한 X 값들
    X_new = np.linspace(-3, 3, 1000).reshape((1000, 1))
    degrees = (1, 2, 4, 100)
    for d in degrees:
        poly_features = PolynomialFeatures(degree=d, include_bias=False)
        scaler = StandardScaler()
        # 다항 회귀에서는 반드시 표준화를 하는 것이 좋다.
        # 고차항이 너무 큰 영향을 줄 수 있으므로, 고차항과 저차항이 고르게 영향을
        # 줄 수 있게 하기 위해서.
        regressor = LinearRegression()
        poly_model = Pipeline([
            ('poly', poly_features),
            ('scaler', scaler),
            ('reg', regressor)
        ])
        poly_model.fit(X, y)  # 학습 데이터로 모델을 훈련
        if d != 100:
            print(regressor.coef_)
        y_pred = poly_model.predict(X_new)  # 테스트 데이터 예측
        plt.plot(X_new, y_pred, label=f'degree={d}')

    plt.scatter(X, y, color='gray')
    plt.legend()
    plt.axis([-3, 3, -1, 10])
    plt.show()

    # overfitting(과적합, 과대적합):
    #   훈련 데이터에서는 성능이 좋지만, 검증 데이터에서는 성능이 좋지 않은 경우
    # underfitting(과소적합):
    #   훈련 데이터, 검증 데이터 모두 성능이 좋지 않은 경우
    # 학습 곡선(learning curve)
    #   훈련 데이터의 크기에 따른 훈련/검증 데이터의 성능을 그린 그래프
    # 선형 회귀의 학습 곡선 vs 다항 회귀의 학습 곡선
    plot_learning_curve(LinearRegression(), X, y)
    plt.show()

    poly_model = Pipeline([
        ('poly_features', PolynomialFeatures(degree=10, include_bias=False)),
        ('scaler', StandardScaler()),
        ('regressor', LinearRegression())
    ])
    plot_learning_curve(poly_model, X, y)
    plt.axis([0, 80, 0, 3])
    plt.show()
