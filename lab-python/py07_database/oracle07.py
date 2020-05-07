# Data Binding
# 미리 만들어진 SQL 문장에 변수 값을 연결(bind)시키는 방법

import cx_Oracle
import py07_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
    with conn.cursor() as cursor:
        sql_insert = """insert into ex_emp (empno, ename, deptno) 
        values (:emp_no, :emp_name, :dept_no)"""
        # insert into ex_emp (empno, ename, deptno) values (9999, 'gd', 10)

        empno = int(input('사번 입력>>> '))
        ename = input('사원 이름 입력>>> ')
        deptno = int(input('부서 번호 입력>>> '))

        cursor.execute(sql_insert,
                       emp_no=empno,
                       emp_name=ename,
                       dept_no=deptno)
        conn.commit()



