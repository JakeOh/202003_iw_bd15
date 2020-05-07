# with ~ as 구문을 사용한 DB 연결

import cx_Oracle
import py07_database.oracle_config as cfg

# DB와 연결(접속)
with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
    # cursor 객체 생성
    with conn.cursor() as cursor:
        cursor.execute('select * from dept2')
        for row in cursor:
            print(row)

