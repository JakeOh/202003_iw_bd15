# emp 테이블 사용
# 이름을 입력받아서 사번, 이름, 급여, 부서번호를 출력
# 이름의 일부만 입력하더라도 검색되도록.

# emp, dept 테이블 사용
# 사번(empno)을 입력받아서, 사번, 이름, 급여, 부서이름, 위치를 출력

import cx_Oracle
import py07_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
    with conn.cursor() as cursor:
        sql = '''select empno, ename, sal, deptno
        from emp
        where upper(ename) like upper(:name)'''

        name = input('검색할 사원 이름>>> ')
        name = ''.join(['%', name, '%'])  # '%' + name + '%'
        cursor.execute(sql, name=name)

        for row in cursor:
            print(row)

        print()  # 줄바꿈(new line)

        sql2 = '''select e.empno, e.ename, e.sal, d.dname, d.loc
        from emp e, dept d
        where e.deptno = d.deptno
            and e.empno = :empno'''

        emp_no = int(input('검색할 사번>>> '))

        cursor.execute(sql2, empno=emp_no)
        for row in cursor:
            print(row)



