# dict와 함께 사용되는 for 구문

students = {1: 'aa', 2: 'bb', 3: 'cc'}
# for-in 구문에서 dictionary는 key에 대해서 iteration을 수행함.
for k in students:
    print(k, students[k])

print(students.items())
for id, name in students.items():
    print(id, ':', name)
