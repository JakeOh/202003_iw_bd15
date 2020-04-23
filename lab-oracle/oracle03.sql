-- hr 계정으로 접속

-- hr 계정이 가지고 있는 테이블 이름들
select table_name from user_tables;
desc user_tables;  -- 테이블을 관리하는 테이블

-- employees 테이블의 구조
desc employees;
-- departments 테이블의 구조
desc departments;

-- empolyees 테이블의 전체 레코드 검색
select * from employees;
-- departments 테이블의 전체 레코드 검색
select * from departments;

-- 2) 이름이 'J'로 시작하는 직원들의 사번, 이름(first_name), 성(last_name)을 출력
select employee_id, first_name, last_name
from employees
where first_name like 'J%';

-- 3) 전화번호가 '011'로 시작하는 직원들의 사번, 이름, 전화번호를 출력
select employee_id, first_name, phone_number
from employees
where phone_number like '011%';

-- 4) 매니저의 사번이 120인 직원들의 사번, 이름, 매니저 사번, 부서번호를 출력
select employee_id, first_name, manager_id, department_id
from employees
where manager_id = 120;

-- 5) 사번이 120번인 직원의 모든 정보를 출력
select * from employees where employee_id = 120;

-- 6) 급여가 3000 이상, 5000 이하인 직원들의 사번, 이름, 급여를 출력
select employee_id, first_name, salary
from employees
where salary between 3000 and 5000;
--where salary >= 3000 and salary <= 5000;

-- 7) 수당을 지급받는 직원들의 사번, 이름, 급여, 수당 퍼센트, 1년 급여를 출력
-- Hint: annual salary = (salary * 12) * (1 + commission_pct)
select employee_id, first_name, salary, commission_pct, 
    (salary * 12) * (1 + commission_pct) as annual_sal
from employees
where commission_pct is not null;



