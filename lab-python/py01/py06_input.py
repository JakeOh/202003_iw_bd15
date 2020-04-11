# console 창에서 사용자 키보드 입력을 받는 방법:

print('이름?')
name = input()
print(f'Hello, {name}!')

print('나이?')
age = int(input())
print(f'내년엔 {age + 1}살이 되겠군요...')

# input(): 키보드에서 엔터가 입력될 때까지의 문자열을 반환(return)
# int(object): object를 int(정수) 타입의 값으로 변환
# float(object): object를 float(실수) 타입의 값으로 변환
