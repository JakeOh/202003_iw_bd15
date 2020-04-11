# 논리 연산자(boolean operator): and, or, not
#   논릿값(True, False) 사이의 연산에 사용
# 비트 연산자(bitwise operator): &, |, ^
#   정수(int) 사이의 연산에 사용

print(1 & 3)  # 0001 & 0011 = 0001
print(1 & 2)  # 0001 & 0010 = 0000

x = 10
print((x > 0) and (x < 100))
print(0 < x < 100)

y = 10
z = 10
print((x == y) and (y == z))
print(x == y == z)

mask = 150  # 남아 있는 마스크 개수
# if 마스크 개수가 50개 이상이면, "약국 찾아감"
# if 마스크 개수가 10 ~ 49개이면, "모험을 한다."
# if 마스크 개수 10개 미만이면, "다른 약국 찾는다."
if mask >= 50:
    print('약국 찾아감.')
elif 10 <= mask < 50:  # (mask >= 10) and (mask < 50)
    print('모험을 한다.')
else:
    print('다른 약국 찾는다.')

languages = ['R', 'Python']
print('Python' in languages)

print('programming language?')
lang = input()
# if lang가 languages 안에 있다면 리스트 내용 출력
# lang가 languages 안에 없다면 리스트의 첫번째 위치에 추가하고 출력
if lang in languages:
    pass
else:
    languages.insert(0, lang)
print(languages)
