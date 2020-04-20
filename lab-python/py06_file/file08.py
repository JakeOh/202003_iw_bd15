import pickle

# 객체(object)를 문자열(text)가 아닌 이진 데이터(binary data) 형태로
# 파일 읽기/쓰기

person = {'name': '오쌤',
          'age': 16,
          'phone': ['010-1111-2222', '02-1234-5678'],
          'email': {'company': 'jake@itwill.co.kr',
                    'personal': 'jake@gmail.com'}}

with open('person.pickle', mode='wb') as f:
    # mode='wb': write binary
    pickle.dump(person, f)  # 바이너리 데이터를 파일에 쓰기(serialize)

with open('person.pickle', mode='rb') as f:
    # mode='rb': read binary
    contact = pickle.load(f)  # 파일에서 바이너리 데이터를 읽기(de-serialize)
    print(contact)
