# emp, dept 테이블에서
# 사번,이름, 급여, 수당(comm), 연봉, 부서이름, 위치를 검색해서 csv 파일로 저장
# 연봉 = 급여 * 12 + comm

import csv
import cx_Oracle
import py07_database.oracle_config as cfg

with cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn) as conn:
    with conn.cursor() as cursor:
        sql = '''
        select
            e.empno, e.ename, e.sal, e.comm,
            e.sal * 12 + nvl(e.comm, 0) as annual_sal,
            d.dname, d.loc
        from emp e, dept d
        where e.deptno = d.deptno
        '''
        cursor.execute(sql)
        records = [row for row in cursor]
        col_names = [col[0] for col in cursor.description]
        print(col_names)
        print(records[0])

with open('emp2.csv', mode='w', encoding='utf-8', newline='') as f:
    # csv writer(파일 쓰기 기능) 객체를 생성
    writer = csv.writer(f)
    writer.writerow(col_names)
    for rec in records:
        writer.writerow(rec)




