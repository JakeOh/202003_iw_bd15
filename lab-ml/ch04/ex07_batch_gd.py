# Batch Gradient Descent(배치 경사 하강법)
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import SGDRegressor


def learning_schedule(t, t0=10, t1=100):
    return t0 / (t + t1)


if __name__ == '__main__':
    np.random.seed(1)

    # y = 4 + 3x + e, 0 <= X < 2, 100개 샘플
    m = 100  # 샘플 개수(데이터 프레임의 row 개수)
    X = 2 * np.random.rand(m, 1)  # (100, 1) 행렬 - 데이터
    # print(X)
    y = 4 + 3 * X + np.random.randn(m, 1)  # (100, 1) 행렬 - 레이블

    plt.scatter(X, y)
    plt.show()

    X_b = np.c_[np.ones((m, 1)), X]  # bias를 포함한 X

    # 선형 회귀(linear regression)의 목적:
    # 예측값 y_hat = theta0 + theta1 * X (y_hat = X_b @ theta)
    # MSE(Mean Squared Errors)를 최소로 만드는 theta0와 theta1을 찾는 것.

    # theta0와 theta1의 초깃값을 임의로 선택
    theta = np.random.randn(2, 1)
    print(theta)

    # 하이퍼 파라미터(hyper-parameter) 설정
    learning_rate = 0.1  # 학습률: gradient에 곱해주는 비율
    max_iterations = 1_000  # 최대 반복 횟수
    for iteration in range(max_iterations):
        # gradient를 계산할 때 전체 샘플(X_b)를 사용해서 계산하기 때문에
        # 배치 경사 하강법이라고 부름.
        gradients = (2/m) * X_b.T.dot(X_b.dot(theta) - y)
        # gradinet를 이용해서 parameter(theta0, theta1)을 갱신.
        theta = theta - learning_rate * gradients
        if (iteration + 1) % 100 == 0:  # 매 100번 반복 때마다
            print(f'=== iteration {iteration + 1} ===')
            print(theta)

    print()
    print('best theta:')
    print(theta)

    # Stochastic Gradient Descent(확률적 경사 하강법)
    # Batch GD는 gradient를 계산할 때 전체 샘플(X_b)을 이용해서 계산
    # Btach GD의 단점: gradient를 한번 계산할 때마다 시간이 오래 걸림.
    # Batch GD의 단점을 해결하기 위해서,
    # 샘플을 랜덤하게 하나만 선택해서 gradient를 계산

    theta_sgd = np.random.randn(2, 1)  # 랜덤 초기화
    max_epochs = 50  # 샘플 전체를 훈련시키는 횟수
    for epoch in range(max_epochs):
        for _ in range(m):  # 전체 샘플 개수만큼 반복
            # 0 <= i < 100 사이에 있는 임의의 인덱스를 선택
            random_index = np.random.randint(m)
            x_i = X_b[random_index:(random_index + 1)]  # (2, 1) 2d 행렬
            y_i = y[random_index:(random_index + 1)]  # (1, 1) 2d 행렬
            # 샘플을 한개만 선택 -> m = 1
            gradients = 2 * x_i.T.dot(x_i.dot(theta) - y_i)
            theta = theta - learning_rate * gradients

    print('Stochastic GD theta')
    print(theta)

    # SGD(Stochastic Gradient Descent)
    theta_sgd2 = np.random.randn(2, 1)  # 랜덤 초기화
    max_epochs = 1000
    t = 0
    for epoch in range(max_epochs):  # 전체 훈련 샘플 1000번 반복
        theta_init = theta_sgd2  # 훈련 샘플 학습이 끝난 후 비교
        # 0 ~ 99 사이의 숫자들을 임의의 순서로 섞음.
        shuffled_indices = np.random.permutation(m)
        for index in shuffled_indices:
            x_i = X_b[index:(index + 1)]  # 랜덤 샘플 추출
            y_i = y[index:(index + 1)]
            gradients = 2 * x_i.T.dot(x_i.dot(theta_sgd2) - y_i)
            lr = learning_schedule(t)
            theta_sgd2 = theta_sgd2 - lr * gradients
            t += 1  # 반복할 때마다 학습률을 줄이기 위해서
        if np.linalg.norm(theta_init - theta_sgd2) < 0.001:
            # tolerance 0.0001 미만이면
            print('epoch:', epoch)
            break  # epoch 종료

    print(theta_sgd2)

    # scikit-learn 패키지의 SGD 회귀 클래스
    sgd_reg = SGDRegressor(max_iter=1000, tol=0.001, penalty=None, eta0=0.1)
    sgd_reg.fit(X, y.ravel())
    print(f'절편(bias): {sgd_reg.intercept_}, 기울기(weight): {sgd_reg.coef_}')
