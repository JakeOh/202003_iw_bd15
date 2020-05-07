# hr 계정 사용
# employees, departments, locations 테이블 사용
# first_name의 일부만 입력받아서
# 입력받은 문자열이 first_name에 포함되어 있는 직원들의
# 아이디, 이름(first/last), 급여, 부서이름, 근무 도시를 출력

import cx_Oracle

user = 'hr'
pwd = 'hr'
dsn = 'localhost:1521/orcl'

with cx_Oracle.connect(user, pwd, dsn) as conn:
    with conn.cursor() as cursor:
        sql = '''
        select 
            e.employee_id, e.first_name, e.last_name, e.salary,
            d.department_name, l.city
        from employees e, departments d, locations l
        where lower(e.first_name) like lower(:name)
            and e.department_id = d.department_id
            and d.location_id = l.location_id'''

        name = input('검색할 사원 이름>>> ')
        name = '%' + name + '%'  # ''.join(['%', name, '%'])

        cursor.execute(sql, name=name)
        for row in cursor:
            print(row)
