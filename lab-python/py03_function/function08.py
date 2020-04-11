# 1 x 2 x 3 x ... x n-1 x n = n!을 계산해서 리턴하는 함수
def factorial1(n):
    result = None
    if n == 0:
        result = 1  # 0! = 1
    elif n > 0:
        result = 1
        for x in range(1, n + 1):
            result *= x

    return result


# 재귀 함수(recursive function):
# 함수 내부에서 자기 자신을 다시 호출하는 것
def factorial2(n):
    result = None
    if n == 0:
        result = 1
    elif n > 0:
        result = n * factorial2(n - 1)

    return result


# S(n) = 1 + 2 + 3 + ... + (n-1) + n = S(n-1) + n
def sum_to_n(n):
    return n * (n + 1) / 2


def sum_to_n2(n):
    if n < 0:
        total = None

    total = 0
    for x in range(n + 1):
        total += x

    return total


def sum_to_n3(n):
    total = None
    if n == 0:
        total = 0
    elif n > 0:
        total = sum_to_n3(n - 1) + n

    return total


if __name__ == '__main__':
    print(factorial1(-3))
    for n in range(6):
        print(f'{n}! = {factorial1(n)}')

    print('-' * 20)

    print(factorial2(-3))
    for n in range(6):
        print(f'{n}! = {factorial2(n)}')

    print('sum from 1 to 10 =', sum_to_n3(10))
    print('sum from 1 to 100 =', sum_to_n3(100))
