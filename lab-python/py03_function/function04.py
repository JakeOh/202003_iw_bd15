import random
import math


def calc_sum(numbers):
    """
    숫자들의 리스트를 argument로 전달받아서, 모든 원소들의 합을 리턴.

    :param numbers: 숫자들의 리스트(list)
    :return: 리스트 안의 모든 숫자들의 합
    """
    total = 0
    for x in numbers:
        total += x
    return total


def calc_mean(numbers):
    """
    평균 = 합계 / 원소 개수

    :param numbers: 숫자들의 리스트
    :return: 리스트의 모든 원소들의 평균
    """
    return calc_sum(numbers) / len(numbers)


def calc_var(numbers):
    """
    숫자 리스트를 argument로 전달받아서, 그 원소들의 분산을 계산해서 리턴.

    :param numbers: 숫자들의 리스트
    :return: 리스트의 원소들의 분산(variance)
    """
    mu = calc_mean(numbers)  # 평균
    sum_of_squares = 0
    for x in numbers:
        sum_of_squares += (x - mu) ** 2
    var = sum_of_squares / (len(numbers) - 1)
    return var


def calc_stddev(numbers):
    """
    숫자 리스트를 argument로 전달받아서, 그 원소들의 표준편차를 계산해서 리턴.

    :param numbers: 숫자들의 리스트
    :return: 리스트의 원소들의 표준편차(standard deviation)
    """
    return math.sqrt(calc_var(numbers))


def find_min_and_max(numbers):
    """
    숫자들의 리스트에서 최솟값과 최댓값을 찾아서 리턴.

    :param numbers: 숫자들의 리스트
    :return: 최솟값, 최댓값
    """
    min, max = numbers[0], numbers[0]
    for x in numbers:
        if x < min:
            min = x
        if x > max:
            max = x
    return min, max


if __name__ == '__main__':
    scores = [random.randint(0, 10) for _ in range(10)]
    print(scores)
    total = calc_sum(scores)
    print('total =', total)
    print('mean =', calc_mean(scores))
    print('variance =', calc_var(scores))
    print('standard deviation =', calc_stddev(scores))
    print(f'min, max = {find_min_and_max(scores)}')
