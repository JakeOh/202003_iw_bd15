import random  # 난수 생성
import math  # 수학 함수(sqrt)


def monte_carlo(n):
    """
    Monte Carlo 시뮬레이션을 통해서 1/4 원의 면적을 확률적으로 계산하고,
    pi의 근사값을 리턴.

    :param n: int. 시행 횟수
    :return: pi 근사값
    """
    hit = 0  # 난수로 생성한 점이 원 안에 있게 될 확률을 계산하기 위한 변수.
    for _ in range(n):
        # 0 <= x, y < 1 난수를 생성
        x, y = random.random(), random.random()
        if math.sqrt(x ** 2 + y ** 2) <= 1:
            # (x, y)가 반지름 1인 원의 내부에 속한다면,
            hit += 1  # hit의 개수를 1 증가시킴.

    # hit는 1/4원 안에 있는 점들의 개수이므로, pi의 근사값은 x4를 함.
    return 4 * (hit / n)


if __name__ == '__main__':
    for n in range(1, 7):
        pi = monte_carlo(10 ** n)
        print(f'n = {10 ** n}, pi = {pi}')
