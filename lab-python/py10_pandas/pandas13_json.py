"""
JSON(JavaScript Object Notation, 자바스크립트 객체 표현법):
    데이터를 저장할 때 key-value 쌍으로 저장.
    {
        "key1": data1,
        "key2": data2,
        ...
    }

JavaScript의 데이터 타입 vs Python의 데이터 타입
object - dict
array - list
string - str
number - int, float
true/false - True/False
null - None
"""

import json  # 파이썬 기본 모듈: Python 객체 <--> JSON 문자열

# Python dict 객체
person = {
    'name': '홍길동',
    'age': 16,
    'height': 199.5,
    'marriage': False,
    'children': None,
    'phone': ['123-4567', '010-4567'],
    'email': {'personal': 'hgd@gmail.com', 'company': 'hgd@itwill.co.kr'}
}
print(type(person), person)


# json.dumps(obj): 파이썬의 객체(obj)를 JSON 형식의 문자열(str)로 변환해서 반환.
person_str = json.dumps(person)
print(type(person_str), person_str)

# json.dump(obj, fp):
# 파이썬 객체(obj)를 JSON 형식의 문자열로 변환해서 파일(fp)에 씀(write).
with open('person.json', mode='w') as f:  # 쓰기모드(w)로 파일을 오픈.
    json.dump(person, f)  # 파일에 문자열을 씀.

# json.load(fp):
# JSON 형식의 문자열이 저장된 파일을 읽어서 파이썬 객체를 생성함.
with open('person.json', mode='r') as f:  # 읽기모드(r)로 파일을 오픈.
    hgd = json.load(f)  # 파일의 내용(문자열)을 파이썬 객체로 변환.
print(type(hgd), hgd)

# json.loads(str)
# JSON 형식으로 작성된 문자열(str)을 파이썬 객체 타입으로 변환해서 반환.
with open('person.json', mode='r') as f:
    for line in f:
        print(line)  # 파일의 한 줄을 그대로 출력
        print(json.loads(line))  # 파일의 한 줄을 파이썬 객체로 변환해서 출력.

# Python object -> JSON-formatted 파일/문자열 변환:
#   json.dump(obj, fp), json.dumps(obj)
# JSON-formatted 파일/문자열 -> Python object 변환:
#   json.load(fp), json.loads(str)



