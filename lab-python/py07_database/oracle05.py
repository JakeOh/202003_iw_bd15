# 부서번호를 입력받아서, 해당 부서의 직원들의 사번, 이름, 급여를 출력

import cx_Oracle
import py07_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
    with conn.cursor() as cursor:
        dept_no = int(input('부서번호 입력>>> '))
        sql_select = f"select empno, ename, sal from emp where deptno = {dept_no}"
        print(sql_select)
        cursor.execute(sql_select)
        for row in cursor:
            print(row)
