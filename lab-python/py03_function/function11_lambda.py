"""
람다 표현식(lambda expression):
함수의 이름 없이, 함수의 parameter 선언과 리턴 값 만으로 함수를 표현하는 방법.
람다 표현식은 이름 없는 함수(anonymous function)임.
lambda [param1, param2, ...]: expression(식)
"""

plus = lambda x, y: x + y
print(plus, type(plus))
print(plus(1, 2))


def calculator(x, y, operation):
    return operation(x, y)


# lambda 표현식을 함수의 argument로 전달
print(calculator(1, 2, lambda x, y: x + y))
print(calculator(1, 2, lambda x, y: x / y))
print(calculator(1, 2, lambda x, y: (x - y) ** 2))


# lambda expression을 사용하는 함수 예
def my_filter(array, func):
    """
    리스트를 argument로 전달받아서, 그 원소들 중 필터링 조건을 만족하는
    원소들로 이루어진 새로운 리스트를 생성하고 리턴함.

    :param array: 리스트
    :param func: True/False를 리턴하는 함수
    :return: func의 호출 결과가 True인 원소들로만 이루어진 새로운 리스트
    """
    # result = []  # empty list
    # for value in array:  # array에 포함된 모든 값들에 대해서 반복
    #     if func(value):  # 필터링 조건을 만족(True)하면
    #         result.append(value)  # 리턴할 리스트에 추가

    # line 33 ~ 36의 내용은 list comprehension으로 대체할 수 있음.
    result = [value for value in array if func(value)]

    return result


numbers = [1, -2, 3, -4, 5, -6, -7, 8]
result = my_filter(numbers, lambda x: x > 0)
print(result)

result = my_filter(numbers, lambda x: x % 2 == 0)
print(result)

languages = ['python', 'r', 'java', 'c/c++', 'kotlin', 'pl/sql']
result = my_filter(languages, lambda x: len(x) >= 6)
print(result)


def my_mapper(array, func):
    """
    array의 원소들을 함수 func의 argument로 전달해서,
    array의 원소를 key로, func의 리턴 값을 value로 하는 dict를 생성, 리턴.

    :param array: 리스트
    :param func: 파라미터가 1개인 함수.
    :return: dict
    """
    result = dict()  # empty dict
    for item in array:  # 리스트의 모든 원소들에 대해서 반복
        result[item] = func(item)  # 원소를 key, 리턴값 value

    return result


result = my_mapper(languages, lambda x: len(x))
print(result)

result = my_mapper(languages, lambda x: x.upper())
print(result)
