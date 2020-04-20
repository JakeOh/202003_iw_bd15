with open('email.txt', mode='w', encoding='utf-8') as f:
    f.write('hgd@gmail.com\n')
    f.write('gildong@naver.com\n')
    f.write('gil-dong@itwill.co.kr\n')

# email.txt 파일을 읽기 모드로 오픈한 후,
# email domain들의 리스트를 작성.
texts = '    abc def     ghijk    lmn    '
print(texts)
stripped = texts.strip()
print(stripped)
texts = 'abc-def-ghi-12345'
print(texts.split('-'))

domains = []
with open('email.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        # print(line.strip().split('@'))
        email = line.strip().split('@')
        domains.append(email[1])
print(domains)
