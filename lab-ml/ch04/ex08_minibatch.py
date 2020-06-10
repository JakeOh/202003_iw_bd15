import matplotlib.pyplot as plt
import numpy as np

from ch04.ex07_batch_gd import learning_schedule
# 학습률을 반복할 때마다 변화시키는 함수


def gradient_descent(X, y,
                     max_iterations=1_000,  # 최대 에포크 반복 횟수
                     batch_size=20,  # 미니 배치 크기
                     eta0=0.1,  # 학습률 초기값
                     tolerance=1e-3):  # 에포크 중지 조건
    # np.random.seed(1)
    # Batch, Stochastic, Minibatch GD 모두 할 수 있게끔 함수 작성
    theta_paths = []  # 파라미터들(절편, 기울기)의 업데이트 히스토리 -> 리턴
    m = len(X)  # 샘플 개수
    X_b = np.c_[np.ones((m, 1)), X]  # bias 항를 포함한 데이터

    theta = np.random.randn(2, 1)  # 파라미터(theta0, theta1) 랜덤 초기화
    theta_paths.append(theta)
    t = 0  # t가 증가할 때마다 학습률을 감소시키기 위해서
    for epoch in range(max_iterations):
        theta_init = theta  # tolerance 비교하기 위해서
        # 샘플들의 순서를 무작위로 섞음.
        shuffled_indices = np.random.permutation(m)
        X_b_shuffled = X_b[shuffled_indices]
        y_shuffled = y[shuffled_indices]
        for i in range(0, m, batch_size):
            # 미니 배치 크기 만큼 샘플들을 추출
            # batch_size == 1: Stochastic, batch_size == m: Batch
            x_i = X_b_shuffled[i:(i + batch_size)]
            y_i = y_shuffled[i:(i + batch_size)]
            # Gradients 계산
            gradients = (2/batch_size) * x_i.T.dot(x_i.dot(theta) - y_i)
            # 파라미터 업데이트(갱신)
            t0 = 10
            t1 = t0 / eta0
            lr = learning_schedule(t, t0=t0, t1=t1)  # epoch마다 학습률 감소
            t += 1
            theta = theta - lr * gradients
        theta_paths.append(theta)  # 파라미터 업데이트 내역을 저장
        if np.linalg.norm(theta_init - theta) < tolerance:
            break  # 에포크 종료
    return np.array(theta_paths)


if __name__ == '__main__':
    np.random.seed(1)

    m = 100  # 샘플 개수(row 개수)
    X = 2 * np.random.rand(m, 1)  # 0 <= X < 2 범위의 난수 100개
    y = 4 + 3 * X + np.random.randn(m, 1)  # y = 4 + 3x + e

    # dot product를 하기 위해서
    X_b = np.c_[np.ones((m, 1)), X]

    # Mini-batch Gradient Descent(미니 배치 경사 하강법)
    max_iterations = 1_000  # 전체 훈련 샘플 학습 횟수
    minibatch_size = 20  # 파라미터(theta0, theta1)을 갱신할 때 사용할 샘플 개수
    learning_rate = 0.1  # 학습률: gradient에 곱해주는 상수
    tolerance = 0.0001  # 에포크(epoch)를 멈출 조건(임계값)

    theta = np.random.randn(2, 1)  # 파라미터(theta0, theta1) 랜덤 초기화

    t = 0
    for epoch in range(max_iterations):
        # 갱신(update)되기 전의 파라미터를 저장 -> 나중에 epoch 중지 결정
        theta_init = theta
        # 각 에포크마다 훈련 샘플들을 랜덤하게 섞기 위해서
        shuffled_indices = np.random.permutation(m)
        X_b_shuffled = X_b[shuffled_indices]
        y_shuffled = y[shuffled_indices]
        for i in range(0, m, minibatch_size):
            # 미니 배치 크기만큼 샘플 선택
            x_i = X_b_shuffled[i:(i + minibatch_size)]
            y_i = y_shuffled[i:(i + minibatch_size)]
            # 미니 배치 샘플로 gradient 계산
            gradients = (2/minibatch_size) * x_i.T.dot(x_i.dot(theta) - y_i)
            learning_rate = learning_schedule(t)
            t += 1
            # 계산된 gradient로 파라미터 갱신(update)
            theta = theta - learning_rate * gradients
        # 갱신(update)된 파라미터가 임계값(tolerance) 이내에 있는 지 검사
        if np.linalg.norm(theta_init - theta) < tolerance:
            print('epoch:', epoch)
            break  # 에포크(학습) 중지

    print(theta)

    print('\n', '*'*30, '\n')

    print('Batch Gradient Descent')
    batch_thetas = gradient_descent(X, y, batch_size=len(X))
    print(batch_thetas[-1], len(batch_thetas))

    print('Stochastic Gradient Descent')
    stochastic_thetas = gradient_descent(X, y, batch_size=1)
    print(stochastic_thetas[-1], len(stochastic_thetas))

    print('Mini-batch Gradient Descent')
    minibatch_thetas = gradient_descent(X, y, batch_size=20)
    print(minibatch_thetas[-1], len(minibatch_thetas))

    # 세가지 GD 방식을 그래프로 비교
    plt.plot(batch_thetas[:, 0], batch_thetas[:, 1],
             color='blue', marker='o', label='Batch GD')
    plt.plot(stochastic_thetas[:, 0], stochastic_thetas[:, 1],
             color='red', marker='^', label='Stochastic GD')
    plt.plot(minibatch_thetas[:, 0], minibatch_thetas[:, 1],
             color='green', marker='+', label='Mini-batch GD')
    plt.legend()
    plt.xlabel('theta0')
    plt.ylabel('theta1')
    plt.axis([2, 4.5, 2, 4])
    plt.show()
