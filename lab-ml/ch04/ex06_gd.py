# Gradient Descent(경사 하강법)
import numpy as np

from ch04.ex05_differentiate import square, derivative

if __name__ == '__main__':
    # y = x ** 2을 최소로 하는 x의 값 ?
    learning_rate = 0.2  # 학습률
    # 학습률을 0.1, 0.2, 0.5, 1.0, 1.1 바꿔가면서 테스트
    # 학습률이 작을 때는 최솟값 위치에 도달하는 데 오래 걸림.
    # 학습률이 클 때는 최솟값 위치에 빠르게 도달할 수 있음.
    # 학습률이 너무 커지게 되면, 최솟값 위치로 가지 못하고 발산할 수도 있음.

    tolerance = 0.0001  # 반복문을 멈추기 위한 조건
    

    x = 5  # 임의로 선택한 x
    print(f'x = {x}, y = {square(x)}')
    for n in range(100_000):
        # learning_rate = 0.9 * learning_rate
        x_new = x - learning_rate * derivative(square, x)
        if abs(x_new - x) < tolerance:
            break
        x = x_new
        print(f'n = {n}, x = {x}, y = {square(x)}')

