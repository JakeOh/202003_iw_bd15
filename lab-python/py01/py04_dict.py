"""
dict: dictionary(사전)
원소들을 key-value 쌍으로 저장하는 데이터 타입.
다른 프로그래밍 언어에서 Map(HashMap)과 비슷한 구조.
key는 중복되지 않는 값이어야 함. value는 중복되도 됨.
"""

students = {1: '고영주', 2: '김나영', 3: '김민기'}
print(students, type(students))

# dict의 값(value)을 읽거나 변경할 때는 key를 사용.
print(students[3])
students[3] = 'Kim Min-Ki'
print(students)

# dict에 새로운 key-value 쌍을 추가
students[4] = '김보수'
print(students)

# dict의 유용한 함수들: keys(), values(), items()
print(students.keys())
print(students.values())
print(students.items())

book = {'title': 'Python for Data Analysis',
        'authors': ['웨스 매키니', '김영근'],
        'isbn': 123456789}
print(book['authors'][0])
