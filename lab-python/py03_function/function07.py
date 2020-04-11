"""
variable-length keyword argument:
함수를 정의할 때 parameter 이름 앞에 **를 사용.
함수를 호출할 때는 f(param1=value1, param2=value2, ..) 와 같은 형식으로 호출.
함수 내부에서는 argument를 dict처럼 사용.
"""


def fn_test(**kwargs):
    print('kwargs =', kwargs)
    # for param in kwargs:
    #     print(param, kwargs[param])
    for param, val in kwargs.items():
        print(param, val)


fn_test(number=1, name='오쌤')
