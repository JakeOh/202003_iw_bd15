-- hr 계정

-- 1) employee_id가 179인 사원의 모든 정보를 출력
select * from employees where employee_id = 179;

-- 2) employee_id가 179의 job title을 출력
select job_title from jobs where job_id = 'SA_REP';

-- 3) 사번 179인 직원이 근무하는 부서의 정보를 출력
select * from departments where department_id = 80;
select * from locations where location_id = 2500;

-- 4) 사번 179인 직원의 매니저 정보를 출력
select * from employees where employee_id = 149;

-- 5) 부서 번호 20번인 부서의 모든 정보 출력
select * from departments where department_id = 20;

-- 6) 20번 부서의 관리자 정보를 출력
select * from employees where employee_id = 201;

-- 7) 20번 부서의 위치 정보를 출력
select * from locations where location_id = 1800;

