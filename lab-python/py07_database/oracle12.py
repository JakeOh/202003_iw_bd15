# scott 계정의 emp 테이블의 모든 레코들을 select해서 emp.csv 파일에 저장

# 1. DB 서버와 connection
# 2. cursor 객체 생성
# 3. SQL 문장 작성
# 4. SQL 문장 실행(execute)
# 5. for ... in cursor 구문을 사용해서 모든 사원 정보를 저장하는 리스트를 생성
# 6. 리스트의 각 원소들을 쉼표(,)로 구분된 문자열로 만듦
# 7. 작성된 문자열을 파일에 씀(write)

# csv 패키지를 사용

import cx_Oracle
import py07_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
    with conn.cursor() as cursor:
        sql = 'select * from emp'
        cursor.execute(sql)
        employees = [row for row in cursor]
        print(employees)

        col_names = [col[0] for col in cursor.description]
        print(col_names)

with open('emp.csv', mode='w', encoding='utf-8') as f:
    line = ','.join(col_names)
    f.write(line)
    f.write('\n')
    for emp in employees:
        line = ','.join(str(x) for x in emp)
        f.write(line)
        f.write('\n')


