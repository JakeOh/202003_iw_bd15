"""
코드 실행 중에 발생할 수 있는 에러(error, exception)를 처리하는 방법
try:
    실행할 코드들
except:
    에러가 발생했을 때 처리할 코드
"""

try:
    numbers = [1, 2, 3]
    # print(numbers[3])
    print('end of try')
except:
    print('에러를 except 구문에서 처리')

"""
try:
    실행할 코드들
except 처리할 에러 종류 as 변수:
    에러 처리 코드
"""

try:
    numbers = [1, 2, 3]
    print(numbers[3])
except IndexError as e:
    print(e)

print('end of process')
