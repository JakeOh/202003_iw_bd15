-- 사번, 이름, 성, job_id, job_title, job 시작일, job 종료일을 출력.
select e.employee_id, e.first_name, e.last_name,
    to_char(jh.start_date, 'YYYY/MM/DD') as START_DATE, 
    to_char(jh.end_date, 'YYYY/MM/DD') as END_DATE, 
    jh.job_id, j.job_title
from employees e, job_history jh, jobs j
where e.employee_id = jh.employee_id
    and jh.job_id = j.job_id
order by e.employee_id, START_DATE;

select e.employee_id, e.first_name, e.last_name,
    to_char(jh.start_date, 'YYYY/MM/DD') as START_DATE, 
    to_char(jh.end_date, 'YYYY/MM/DD') as END_DATE, 
    jh.job_id, j.job_title
from employees e 
    join job_history jh on e.employee_id = jh.employee_id
    join jobs j on jh.job_id = j.job_id
order by e.employee_id, START_DATE;


-- 부서번호, 부서이름, 매니저 아이디, 매니저 이름/성을 출력.
-- 단, 부서 테이블의 모든 부서 이름이 출력되도록.
select d.department_id, d.department_name, d.manager_id,
    e.first_name, e.last_name
from departments d, employees e
where d.manager_id = e.employee_id(+)
order by d.department_id;

select d.department_id, d.department_name, d.manager_id,
    e.first_name, e.last_name
from departments d left join employees e
    on d.manager_id = e.employee_id
order by d.department_id;

-- 사번 100인 직원의 이름/성, 도시를 출력
select e.first_name, e.last_name, l.city
from employees e, departments d, locations l
where e.employee_id = 100
    and e.department_id = d.department_id
    and d.location_id = l.location_id;

select e.first_name, e.last_name, l.city
from employees e 
    join departments d on e.department_id = d.department_id
    join locations l on d.location_id = l.location_id
where e.employee_id = 100;

-- 모든 직원들이 일하는 도시
select e.first_name, e.last_name, l.city
from employees e, departments d, locations l
where e.department_id = d.department_id
    and d.location_id = l.location_id;

select e.first_name, e.last_name, l.city
from employees e 
    join departments d on e.department_id = d.department_id
    join locations l on d.location_id = l.location_id;


-- 부서별 급여 평균 출력
select department_id,
    round(avg(salary), 1) as AVG_SAL
from employees
group by department_id;

-- 부서 이름과 그 부서의 급여 평균
select e.department_id, d.department_name,
    round(avg(e.salary), 1) as AVG_SAL
from employees e, departments d
where e.department_id = d.department_id
group by e.department_id, d.department_name
order by e.department_id;

select e.department_id, d.department_name,
    round(avg(e.salary), 1) as AVG_SAL
from employees e join departments d
    on e.department_id = d.department_id
group by e.department_id, d.department_name
order by e.department_id;

-- 위 결과에 부서의 위치(city)를 추가
select e.department_id, d.department_name, l.city,
    round(avg(e.salary), 1) as AVG_SAL
from employees e, departments d, locations l
where e.department_id = d.department_id
    and d.location_id = l.location_id
group by e.department_id, d.department_name, l.city
order by e.department_id;

select e.department_id, d.department_name, l.city,
    round(avg(e.salary), 1) as AVG_SAL
from employees e 
    join departments d on e.department_id = d.department_id
    join locations l on d.location_id = l.location_id
group by e.department_id, d.department_name, l.city
order by e.department_id;

-- 위 결과에서 위치가 Seattle에 있는 부서들만 출력
-- Seattle에 있는 부서 이름, 부서 위치(city), 평균 급여를 출력
select e.department_id, d.department_name, l.city,
    round(avg(e.salary), 1) as AVG_SAL
from employees e, departments d, locations l
where e.department_id = d.department_id
    and d.location_id = l.location_id
    and l.city = 'Seattle'
group by e.department_id, d.department_name, l.city
order by e.department_id;

select e.department_id, d.department_name, l.city,
    round(avg(e.salary), 1) as AVG_SAL
from employees e
    join departments d on e.department_id = d.department_id
    join locations l on d.location_id = l.location_id
where l.city = 'Seattle'
group by e.department_id, d.department_name, l.city
order by e.department_id;
    
-- 평균 급여가 7000 이상인 부서의 부서 이름과 위치(city), 평균 급여 출력
select e.department_id, d.department_name, l.city,
    round(avg(e.salary), 1) as AVG_SAL
from employees e, departments d, locations l
where e.department_id = d.department_id
    and d.location_id = l.location_id
group by e.department_id, d.department_name, l.city
having avg(e.salary) >= 7000
order by e.department_id;

select e.department_id, d.department_name, l.city,
    round(avg(e.salary), 1) as AVG_SAL
from employees e
    join departments d on e.department_id = d.department_id
    join locations l on d.location_id = l.location_id
group by e.department_id, d.department_name, l.city
having avg(e.salary) > = 7000
order by e.department_id;

-- Seattle에 있는 부서들 중에서
-- 부서 급여 평균이 전체 직원의 급여 평균보다 높은 부서들의
-- 부서 번호, 부서이름, city, 평균 급여 출력
select e.department_id, d.department_name, l.city,
    round(avg(e.salary), 1) as AVG_SAL
from employees e, departments d, locations l
where e.department_id = d.department_id
    and d.location_id = l.location_id
    and l.city = 'Seattle'
group by e.department_id, d.department_name, l.city
having avg(e.salary) > (select avg(salary) from employees)
order by e.department_id;

select e.department_id, d.department_name, l.city,
    round(avg(e.salary), 1) as AVG_SAL
from employees e
    join departments d on e.department_id = d.department_id
    join locations l on d.location_id = l.location_id
where l.city = 'Seattle'
group by e.department_id, d.department_name, l.city
having avg(e.salary) > (select avg(salary) from employees)
order by e.department_id;