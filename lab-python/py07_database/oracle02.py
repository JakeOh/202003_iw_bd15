import cx_Oracle

user = 'scott'  # Oracle 11g EE에 접속하기 위한 사용자 계정
pwd = 'tiger'  # Oracle 11g EE에 접속할 때 비밀번호
# DSN(Data Source Name)
dsn = 'localhost:1521/orcl'  # Oracle Database 서버 주소

# 데이터베이스 서버와 연결 설정 - 접속
connection = cx_Oracle.connect(user, pwd, dsn)

print('DB Version:', connection.version)  # 접속한 DB 서버의 버전

# SQL 문장을 실행하려면 cursor 객체를 생성해야 함
cursor = connection.cursor()

sql_select = 'select * from emp'
# 주의: SQL 문장 끝날 때 ;(semi-colon) 사용하지 않음!

# SQL 문장을 DB 서버로 전송해서 실행
cursor.execute(sql_select)  

# DB 서버가 보내준 결과 처리
row = cursor.fetchone()  # 결과를 한줄씩 읽음
while row:
    print(row)
    row = cursor.fetchone()

# cursor 객체의 사용이 모두 끝나면 close함
cursor.close()

# 데이터베이스 서버와 연결 종료
connection.close()
