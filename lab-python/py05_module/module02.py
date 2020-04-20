# py03_function 패키지(폴더)에 포함된 function02 모듈(파일)을 임포트
# 모듈의 full name은 패키지 이름을 포함.
# import package_name.module_name
# import package_name.module_name as 별명
import py03_function.function02 as fn02

print('-' * 20)
# 모듈이 가지고 있는 함수, 변수 등을 사용할 때는
# package_name.module_name.func_name()
# package_name.module_name.var_name

# 별명을 사용하지 않은 경우 함수 호출
# py03_function.function02.say_hello()

# 별명을 사용한 경우 함수 호출
fn02.say_hello()
