"""
함수(function): 기능을 수행해서 값을 반환(return)하는 코드 블록
인수(argument): 함수를 호출(call, invoke)할 때 전달하는 값
매개변수(parameter): argument를 저장하기 위해서,
함수를 정의할 때 선언하는 지역 변수(local variable)
"""

result = print('Hello, Python!')
print('result =', result)
# print() 함수는 반환하는 값이 없는(None) 함수

result = sum([1, 2, 3, 4, 5])
print('result =', result)

# Ctrl + Q: 함수의 문서(documentation) 보기
# MacOS: Ctrl+J

result = pow(2, 3)  # 2 ** 3
print(result)
