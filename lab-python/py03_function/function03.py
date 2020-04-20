"""
함수를 호출할 때 argument를 전달하는 방법:
1) positional argument:
    함수에 정의된 parameter 순서대로 argument를 전달.
2) keyword argument:
    paraeter=argument와 같은 형식으로 값을 전달.
"""


def minus(x, y):
    return x - y


print('function03.py:', __name__)
if __name__ == '__main__':
    print(minus(1, 2))  # positional argument
    print(minus(x=1, y=2))  # keyword argument
    print(minus(y=1, x=2))
# keyword argument를 사용할 때는 position을 지키지 않아도 괜찮음.
