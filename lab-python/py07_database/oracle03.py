import cx_Oracle
import py07_database.oracle_config as cfg

# 1) DB 서버 연결
conn = cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn)

# 2) cursor 객체 생성 <- SQL 문장 실행, 결과 처리
cursor = conn.cursor()

# SQL 문장 실행
sql_select = 'select * from emp2'
cursor.execute(sql_select)

# 결과 처리: for x in cursor 구문을 사용하면, fetchone() 함수가 자동 호출됨.
for row in cursor:
    print(row)

# cursor 객체 닫기
cursor.close()

# 연결 끊기
conn.close()
