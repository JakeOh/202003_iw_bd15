# emp, dept 테이블을 join,
# 부서 번호를 입력받아서, 해당 부서 직원들의 사번, 이름, 위치를 출력

import cx_Oracle
import py07_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
    with conn.cursor() as cursor:
        sql = '''select e.empno, e.ename, d.loc
        from emp e, dept d
        where d.deptno = :deptno
            and
            e.deptno = d.deptno'''

        deptno = int(input('사원을 검색할 부서 번호 입력>>> '))

        cursor.execute(sql, deptno=deptno)
        for row in cursor:
            print(row)
