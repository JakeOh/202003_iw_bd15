import random

# 1**2 + 2**2 + 3**2 + ... + n**2의 값을 리턴하는 함수
def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) / 6


def sum_of_squares2(n):
    sum = 0
    for x in range(1, n + 1):
        sum += x ** 2

    return sum


def sum_of_squares3(n):
    numbers = [x ** 2 for x in range(1, n + 1)]
    return sum(numbers)


def my_median(numbers):
    """

    :param numbers: 숫자들의 리스트
    :return: 중앙값(median)
    """
    # 1) 정렬
    sorted_numbers = sorted(numbers)

    length = len(sorted_numbers)  # 리스트의 원소의 개수
    mid = length // 2  # 리스트의 중간 위치

    # 2) numbers의 원소의 개수가 홀수인 경우, 중앙값을 리턴
    if length % 2:  # 2로 나눈 나머지가 있으면(홀수)
        median = sorted_numbers[mid]
    else:  # 2로 나눈 나머지가 없으면(짝수)
    # 3) numbers의 원소의 개수가 짝수인 경우, 2개의 중앙값의 평균을 리턴
        left = mid - 1
        median = (sorted_numbers[left] + sorted_numbers[mid]) / 2

    return median


# 숫자들의 리스트에서 최댓값의 인덱스를 리턴하는 함수
def find_index_of_max(numbers):
    max_id, max = 0, numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max:
            max_id, max = i, numbers[i]

    return max_id


def find_index_of_max2(numbers):
    max_id, max = 0, numbers[0]
    for i, val in enumerate(numbers):
        if val > max:
            max_id, max = i, val

    return max_id


if __name__ == '__main__':
    print(sum_of_squares(3))
    print(sum_of_squares2(3))
    print(sum_of_squares3(3))

    scores = [random.randint(0, 5) for _ in range(9)]
    print(scores)
    # sorted(list): list를 오름차순 정렬한 새로운 리스트를 생성해서 리턴.
    sorted_scores = sorted(scores)
    print(sorted_scores)
    print(my_median(scores))

    print(find_index_of_max2(scores))
