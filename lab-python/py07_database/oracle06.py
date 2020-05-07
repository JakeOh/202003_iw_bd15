# insert

import cx_Oracle
import py07_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
    with conn.cursor() as cursor:
        empno = int(input('empno 입력>>> '))
        ename = input('ename 입력>>> ')
        deptno = int(input('deptno 입력>>> '))

        sql_insert = f"insert into ex_emp (empno, ename, deptno) values ({empno}, '{ename}', {deptno})"
        # ename 문자열에 따옴표('')가 포함된 경우에는 SQL 에러 발생
        # -> 해결하는 방안으로 cx_Oracle에서 data-binding 기법이 사용됨
        print(sql_insert)
        cursor.execute(sql_insert)
        # insert, update, delete는 commit을 해야 DB에 반영됨!
        conn.commit()

