-- listagg() 함수
-- 부서별 직원들
select deptno, 
    listagg(ename, ',') within group(order by ename)
from emp
group by deptno;

-- JOB이 같은 직원들을 출력
select job,
    listagg(ename, ',') within group(order by ename)
from emp
group by job;

-- 도시별(loc) 근무하는 직원들
select d.loc,
    listagg(ename, ',') within group(order by ename)
from emp e, dept d
where e.deptno = d.deptno
group by d.loc;

select d.loc,
    listagg(ename, ',') within group(order by ename)
from emp e join dept d
    on e.deptno = d.deptno
group by d.loc;


-- 위 결과에서 근무하는 직원이 없는 도시도 출력
select d.loc,
    listagg(ename, ',') within group(order by ename)
from emp e, dept d
where e.deptno(+) = d.deptno
group by d.loc;

select d.loc,
    listagg(ename, ',') within group(order by ename)
from emp e right join dept d
    on e.deptno = d.deptno
group by d.loc;
