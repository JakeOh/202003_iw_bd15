import matplotlib.pyplot as plt
import numpy as np
from sklearn import clone
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

if __name__ == '__main__':
    np.random.seed(1)

    m = 100
    X = 6 * np.random.rand(m, 1) - 3  # -3 <= X < 3
    y = 2 + X + 0.5 * X**2 + np.random.randn(m, 1)

    # plt.scatter(X, y)
    # plt.show()

    # Train/Test 분리
    # 데이터의 개수를 줄이고, 테스트 세트의 비율을 늘리면
    # 학습에 사용되는 데이터 수가 작아지기 때문에, 학습 성능이 매우 안 좋아짐.
    X_train, X_test, y_train, y_test = train_test_split(X[:50],
                                                        y[:50],
                                                        test_size=0.5,
                                                        random_state=40)

    # 다항 회귀 - 고차항(2차항 이상) 추가, 스케일링
    # Pipeline 생성
    poly_scaler = Pipeline([
        ('poly_features', PolynomialFeatures(degree=100,
                                             include_bias=False)),
        ('std_scaler', StandardScaler())
    ])
    # 학습/검증 세트를 변환
    X_train_scaled = poly_scaler.fit_transform(X_train)
    X_test_scaled = poly_scaler.transform(X_test)

    sgd_reg = SGDRegressor(penalty=None,  # 규제(l1, l2, elasticnet) 없음
                           max_iter=1,  # 전체 훈련 샘플을 1회 반복
                           tol=-np.inf,
                           learning_rate='constant',  # 학습률 고정
                           eta0=0.0005,  # 학습률 초깃값
                           warm_start=True,  # 이전 에포크(반복)의 결과를 사용해서 다음 에포크(반복)을 진행.
                           random_state=1)

    max_iterations = 500  # 반복 횟수
    train_errors, test_errors = [], []  # 반복할 때마다 측정한 RMSE를 저장

    t = 0  # epoch를 반복할 때마다 1씩 증가. 더 작은 RMSE 값을 찾은 경우 0으로 리셋.
    rmse_minimum = np.inf  # 무한대
    best_epoch = 0  # 테스트 세트에서 RMSE가 최소가 되는 반복 횟수
    best_model = None  # 테스트 세트에서 가장 좋은 성능을 보이는 모델
    for epoch in range(max_iterations):
        t += 1
        # 모델 학습 - 계수들(theta0, theta1, ...)을 찾음.
        sgd_reg.fit(X_train_scaled, y_train.ravel())
        # 학습 세트의 예측값
        train_pred = sgd_reg.predict(X_train_scaled)
        # 학습 세트의 Root Mean Squared Errors
        train_rmse = np.sqrt(mean_squared_error(y_train, train_pred))
        # RMSE를 저장
        train_errors.append(train_rmse)
        # 검증 세트에서 예측값 계산
        test_pred = sgd_reg.predict(X_test_scaled)
        test_rmse = np.sqrt(mean_squared_error(y_test, test_pred))
        test_errors.append(test_rmse)
        # 더 작은 테스트 세트의 RMSE를 찾았는 지 검사
        if test_rmse < rmse_minimum:
            rmse_minimum = test_rmse
            best_epoch = epoch
            best_model = clone(sgd_reg)
            t = 0  # t를 0으로 리셋.
        if t >= 10:
            # 테스트 세트의 RMSE 최솟값을 찾은 후 10번 반복하는 동안
            # 더 작은 RMSE를 못 찾은 경우 -> 반복(epoch)을 종로
            break

    # 매 epoch에서의 RMSE들의 이력을 그래프로 그림
    plt.plot(train_errors, color='blue', label='Train RMSE')
    plt.plot(test_errors, color='red', label='Test RMSE')
    plt.legend()
    plt.show()

    # 반복 횟수(epoch)가 많아질 수록(같은 훈련 샘플들을 여러번 훈련시킬 수록)
    # 학습 세트(train set)에서의 성능은 좋아짐(RMSE는 낮아짐)
    # 하지만, 검증 세트(validation set)에서의 성능은 처음에는 좋아지다가,
    # 어느순간부터 다시 나빠지기 시작하는 것이 보통.
    # (RMSE가 작아지다가 다시 커지는 순간이 생김)
    # 이 지점이 모델이 훈련 세트에 과적합(overfitting)되는 시점.
    # max_iteratoins 값에 상관 없이 overfitting되는 시점에 훈련을 멈추는 방법
    # -> early stopping(조기 종료)

    # 검증 세트(X_test)의 최솟값 위치
    scores = np.random.randint(0, 100, 10)
    print(scores)
    # numpy array에서 최댓값, 최소값의 위치(인덱스)
    print('argmax:', np.argmax(scores))
    print('argmin:', np.argmin(scores))

    print('test set min arg:', np.argmin(test_errors))
    print('test set min:', test_errors[np.argmin(test_errors)])

    print('best epoch:', best_epoch)