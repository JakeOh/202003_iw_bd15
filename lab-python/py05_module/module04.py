# 모듈에 포함된 모든 속성(변수, 함수, 클래스, ...)을 import할 때는
# import module_full_name [as alias]
# import py03_function.function04 as fn04
# fn04.calc_stddev([1, 2, 3])

# 모듈에 포함된 속성들 중 하나 또는 일부만 import할 때
# from module_full_name import attr_name1, attr_name2
from py03_function.function04 import calc_stddev, calc_mean
print(calc_stddev([1, 2, 3]))
print(calc_mean([1, 2, 3]))
