# 모든 파이썬 모듈(py 파일)은 __name__ 변수를 가지고 있음.
# 파이썬 인터프리터(python.exe)가 실행하는 모듈의 __name__ 변수에는
# '__main__'이 저장됨.
# 다른 모듈에서 import되는 모듈의 __name__ 변수에서
# 그 모듈의 이름이 저장됨.
import py03_function.function03 as fn03
import py05_module.test as test

print('module03.py:', __name__)
print(fn03.minus(1, 2))
test.fn_test()
