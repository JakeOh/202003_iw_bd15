"""
가변 길이 인수(variable-length argument):
함수를 호출할 때 전달하는 argument의 개수가 변할 수 있는 것.
함수 parameter를 선언할 때, parameter 이름 앞에 *를 사용하면,
variable-length argument를 사용할 수 있음.
함수 내부에서 variable-length argument는 tuple처럼 사용하면 됨.
"""

# variable-length argument를 갖는 함수의 예: print
print('hello')  # no. of args = 1
print()  # no. of args = 0
print('hello', 'python', '안녕하세요')  # no. of args = 3
print(1, 2, 3, sep=':')  # no. of args = 4


def fn_test1(*args):
    print('args =', args)
    for arg in args:
        print(arg)


fn_test1()
fn_test1('abc')
fn_test1('abc', 'def')


def summation(*args):
    """

    :param args: (개수가 정해져 있지 않은) 숫자들
    :return: 모든 숫자들의 합
    """
    total = 0
    for x in args:
        total += x

    return total


print(summation())
print(summation(1, 3, 5))


def fn_test2(a, *b):
    print('a =', a)
    print('b =', b)


# fn_test2()  # parameter a에 값을 전달하지 않아서 에러 발생.
fn_test2(100)  # variable-length인 b에는 값을 전달하지 않아도 됨.
fn_test2(100, 200)


def fn_test3(*a, b):
    print('a =', a)
    print('b =', b)


# fn_test3(1, 2)
# argument 1과 2는 a에 전달되고, b에 전달되는 값이 없어서 에러가 발생
# variable-length argument 뒤에 선언된 파라미터들은 keyword 방식으로만
# 호출이 가능함.
fn_test3(1, 2, b=100)


def calculate(*values, operator):
    """

    :param values: (개수가 정해져 있지 않은) 숫자들
    :param operator: '+', '*'
    :return: operator == '+'인 경우에는 모든 숫자들의 합,
    operator == '*'인 경우에는 모든 숫자들의 곱.
    알 수 없는 operator인 경우에는 None을 리턴.
    """
    result = None
    if operator == '+':
        result = 0
        for x in values:
            result += x  # result = result + x
    elif operator == '*':
        result = 1
        for x in values:
            result *= x  # result = result * x

    return result


print(calculate(1, 2, 3, 4, 5, operator='+'))
print(calculate(1, 2, 3, 4, 5, operator='*'))
print(calculate(1, 2, 3, 4, 5, operator='-'))
