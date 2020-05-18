import json
import pandas as pd

# Python dict 객체
p1 = {'name': 'Aaa', 'age': 19, 'marriage': False}
p2 = {'name': 'Bbb', 'age': 29, 'marriage': True}
p3 = {'name': 'Ccc', 'age': 35, 'marriage': False}

# Python list 객체
persons = [p1, p2, p3]
print(persons)

# Python list를 JSON 형식의 문자열로 변환
persons_json = json.dumps(persons)  # JavaScript의 배열(array)
print(persons_json)

# Python list를 JSON 형식의 파일로 저장
with open('persons.json', mode='w') as f:
    json.dump(persons, f)

# pandas.read_json(file_path) 함수를 사용한 JSON 파일 읽기
persons_df = pd.read_json('persons.json')
print(persons_df)

# ../examples/example.json 파일을 읽어서 DataFrame을 생성
example_df = pd.read_json('../examples/example.json')
print(example_df)

# ./contacts.json 파일을 읽어서 DataFrame을 생성
contacts_df = pd.read_json('contacts.json')
print(contacts_df)  # 비정형 데이터를 정형 데이터로 만들어줌.

# ./contacts.txt 파일은 JSON 배열 또는 객체 형식에 맞지 않음.
# df = pd.read_json('contacts.txt')  # 에러 발생

# 파일 전체는 JSON 포맷에 맞지 않지만, 각각의 라인은 JSON 포맷임
contacts_list = []
with open('contacts.txt', mode='r') as f:  # 파일을 읽기 모드로 열기.
    for line in f:  # 파일에서 한 줄씩 읽으면서,
        contact = json.loads(line)  # JSON 형식의 문자열을 Python 객체로 변환
        contacts_list.append(contact)  # list에 추가
df = pd.DataFrame(contacts_list)
print(df)

# list comprehension
with open('contacts.txt', mode='r') as f:
    contacts_list = [json.loads(line) for line in f]
df = pd.DataFrame(contacts_list)
print(df)

# ../datasets/bitly_usagov/exmple.txt을 읽어서 DataFrame을 생성
# info, columns, shape, ...
with open('../datasets/bitly_usagov/example.txt',
          mode='r', encoding='utf-8') as f:
    # Python dict 객체들의 list
    records = [json.loads(line) for line in f]
df = pd.DataFrame(records)  # list를 DataFrame으로 변환
print(df.shape)
print(df.columns)
df.info()
