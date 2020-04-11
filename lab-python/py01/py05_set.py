"""
set(집합): 저장되는 순서가 중요하지 않고, 중복 저장이 되지 않는 데이터 타입.
{1, 2, 3} == {3, 2, 1}, {1, 2, 2} == {1, 2}
합집합(union), 교집합(intersection), 차집합(difference)와 같은
연산을 위해 만들어진 데이터 타입
"""

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}

# Shift + F10: 최근 실행 목록 중 선택된 파일 실행(Run)
# Ctrl + Shift + F10: 현재 열려있는 파일 실행

print(s1, s2)
print(type(s1))

print(s1 | s2)  # 합집합
print(s1.union(s2))

print(s1 & s2)  # 교집합
print(s1.intersection(s2))

print(s1 - s2)  # 차집합
print(s2.difference(s1))
