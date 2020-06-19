import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    np.random.seed(42)
    m = 100
    X = np.random.rand(m, 1) - 0.5
    y = 3 * X[:, 0]**2 + 0.05 * np.random.randn(m)

    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=0.2, random_state=49)

    gbr = GradientBoostingRegressor(learning_rate=0.1,
                                    max_depth=2,
                                    warm_start=True,
                                    random_state=42)
    # GBR에서 n_estimators의 개수를 바꿔가면서 fit
    # mean_squared_error를 계산
    # MSE가 작아지다가 다시 커지는 순간을 찾아서 반복 멈춤 - Early Stopping
    min_error = float('inf')  # infinity(무한대) - 초깃값
    going_up = 0  # MSE가 커지는 횟수
    for n_estimator in range(1, 200):
        gbr.n_estimators = n_estimator  # Tree 개수(반복 횟수) 증가
        gbr.fit(X_train, y_train)  # 학습 데이터에 fitting - 훈련
        y_pred = gbr.predict(X_test)  # 검증 데이터의 예측값을 찾음.
        test_error = mean_squared_error(y_test, y_pred)  # 검증 데이터의 MSE
        if test_error < min_error:  # 새로 찾은 MSE가 기존 최솟값보다 작다면
            min_error = test_error
            best_estimator = n_estimator
            going_up = 0  # MSE가 증가한 횟수를 0으로 리셋
            print(f'[{n_estimator}] MSE = {test_error}')
        else:  # 새로 찾은 에러가 기존 최솟값보다 크거나 같은 경우
            going_up += 1  # MSE가 증가한 횟수를 1 증가
            print(f'[{n_estimator}] \t MSE = {test_error}')
            if going_up >= 5:
                break  # 반복문 멈춤 - Early stopping

    print('best # of estimators:', best_estimator)
