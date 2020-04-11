"""
Python 기본 데이터 타입(data type)
숫자: int(정수), float(실수), complex(복소수)
문자열: str
논릿값: bool

list(리스트): 여러개의 값을 저장할 수 있는,
저장한 값(원소)들을 변경 가능한(mutable) 데이터 타입.
"""

numbers = [1, 2, 3, 4, 5]
print(numbers)

# list의 원소 값을 읽거나 변경할 때는 인덱스(index)를 이용.
# Python에서 index는 0부터 시작!
# list의 가장 마지막 원소의 인덱스는 (리스트 길이 - 1)
print(numbers[0], numbers[4])
# print(numbers[5])  # IndexError 발생

# 범위 연산자(:)
# start:end - start <= index < end
# start를 쓰지 않으면 기본값은 0
# end를 쓰지 않으면 기본값은 리스트의 마지막 인덱스
print(numbers[0:3])
print(numbers[2:4])
print(numbers[:], numbers[:3], numbers[3:])
print(numbers[-2:])
print(numbers[-4:-2])

# list는 다른 타입의 값들을 저장할 수 있음.
person = ['오쌤', 123, True, ['a', 'b', 'c']]
print(person)
print(person[3], person[3][1])

# 빈 리스트(empty list) 생성
numbers2 = []
print(type(numbers2), len(numbers2))

# list에 원소를 추가
# extend(리스트와 같이 여러개의 원소를 저장할 수 있는 타입)
# argument에 전달된 리스트의 원소들을 하나씩 추가함.
numbers2.extend([1, 2, 3])
print(numbers2)

# append(객체):
# argument로 전달받은 객체를 리스트에 추가.
numbers2.append(4)
print(numbers2)

numbers2.append([5, 6, 7])
print(numbers2)

# insert(index, element): index 위치에 element를 삽입
numbers2.insert(0, 100)
print(numbers2)

numbers2.insert(len(numbers2), 123)  # append()와 같은 기능
print(numbers2)

# list의 원소 삭제
# remove(value): list에서 맨 처음에 나오는 value을 삭제
numbers2.remove(100)
print(numbers2)

# del list[index]: list의 index 위치에 있는 원소를 삭제
del numbers2[4]
print(numbers2)

# list decomposition(unpack)
x, y = [1, 2]
print(x, y)

