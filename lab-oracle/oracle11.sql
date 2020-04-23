-- JOIN
-- 두 개 이상의 테이블에서 조회한 결과를 하나로 합치는 것

-- emp, dept 테이블에서 사번, 이름, 부서번호, 부서이름 출력
-- Oracle 방식
select e.empno, e.ename, e.deptno, d.dname
from emp e, dept d
where e.deptno = d.deptno;

-- ANSI 표준 방식
select e.empno, e.ename, e.deptno, d.dname
from emp e join dept d
    on e.deptno = d.deptno;
-- inner join에서 inner는 생략 가능


-- emp, dept 테이블에서
-- 사번, 이름, 급여, 부서번호, 부서이름을 출력
-- 급여가 2000 이상인 직원만 선택
-- 1) Oracle
select e.empno, e.ename, e.sal, e.deptno, d.dname
from emp e, dept d
where e.deptno = d.deptno
    and
    e.sal >= 2000;
-- 2) ANSI
select e.empno, e.ename, e.sal, e.deptno, d.dname
from emp e join dept d 
    on e.deptno = d.deptno 
where e.sal >= 2000;


-- emp, salgrade 테이블에서 
-- 사번, 이름, 급여, 급여등급을 출력
select e.empno, e.ename, e.sal, s.grade
from emp e, salgrade s
where e.sal between s.losal and s.hisal;
-- where e.sal >= s.losal and e.sal <= s.hisal;

select e.empno, e.ename, e.sal, s.grade
from emp e join salgrade s
    on e.sal between s.losal and s.hisal;

-- emp, dept, salgrade 테이블에서
-- 사번, 이름, 부서이름, 급여, 급여등급을 출력
select e.empno, e.ename, d.dname, e.sal, s.grade
from emp e, dept d, salgrade s
where e.deptno = d.deptno
    and 
    e.sal between s.losal and s.hisal;
    
select e.empno, e.ename, d.dname, e.sal, s.grade
from emp e join dept d
        on e.deptno = d.deptno
    join salgrade s
        on e.sal between s.losal and s.hisal;

-- emp 테이블에서
-- 사번, 이름, 매니저 사번, 매니저 이름을 출력
select e1.empno, e1.ename as 사원, e1.mgr, e2.ename as 매니저
from emp e1, emp e2
where e1.mgr = e2.empno
order by e1.empno;

select e1.empno, e1.ename as 사원, e1.mgr, e2.ename as 매니저
from emp e1 join emp e2
    on e1.mgr = e2.empno
order by e1.empno;

-- emp 테이블에서 부서 번호 출력(중복 제외)
select distinct deptno from emp;
-- dept 테이블에서 부서 번호
select deptno from dept;

-- emp, dept 테이블에서 사원 이름, 부서 번호, 부서 이름을 출력
-- 모든 부서의 번호와 이름을 출력
select e.ename, d.deptno, d.dname
from emp e, dept d
where e.deptno(+) = d.deptno;  -- right join

select e.ename, d.deptno, d.dname
from emp e right join dept d
    on e.deptno = d.deptno;


select e.ename, d.deptno, d.dname
from emp e, dept d
where e.deptno = d.deptno(+);  -- left join

select e.ename, d.deptno, d.dname
from emp e left join dept d
    on e.deptno = d.deptno;


-- emp 테이블에서, 사번, 이름, 매니저 번호, 매니저 이름 출력
-- left join -> King 출력
select e1.empno, e1.ename, e1.mgr, e2.ename as 매니저
from emp e1, emp e2
where e1.mgr = e2.empno(+);

select e1.empno, e1.ename, e1.mgr, e2.ename as 매니저
from emp e1 left join emp e2
    on e1.mgr = e2.empno;

-- right join: 매니저가 아닌 직원들 정보도 함께 출력
select e1.empno, e1.ename, e1.mgr, e2.ename as 매니저
from emp e1, emp e2
where e1.mgr(+) = e2.empno;

select e1.empno, e1.ename, e1.mgr, e2.ename as 매니저
from emp e1 right join emp e2
    on e1.mgr = e2.empno;
    
-- full (outer) join
select e1.empno, e1.ename, e1.mgr, e2.ename as 매니저
from emp e1 full join emp e2
    on e1.mgr = e2.empno
order by e1.empno;

-- full outer join은 Oracle 만의 문법이 없음
-- left join의 결과와 right join의 결과를 합집합(union) 할 수는 있음.
select e1.empno, e1.ename, e1.mgr, e2.ename as 매니저
from emp e1, emp e2 where e1.mgr = e2.empno(+)
union
select e1.empno, e1.ename, e1.mgr, e2.ename as 매니저
from emp e1, emp e2 where e1.mgr(+) = e2.empno;


-- 부서번호, 부서이름, 각 부서 직원들의 급여 평균, 최댓값, 최솟값, 직원수를 출력.
select e.deptno, d.dname,
    round(avg(e.sal), 1) as AVG_SAL, 
    max(e.sal) as MAX_SAL, 
    min(e.sal) as MIN_SAL, 
    count(*) as COUNT
from emp e, dept d
where e.deptno = d.deptno
group by e.deptno, d.dname;

select e.deptno, d.dname,
    round(avg(e.sal), 1) as AVG_SAL, 
    max(e.sal) as MAX_SAL, 
    min(e.sal) as MIN_SAL, 
    count(*) as COUNT
from emp e inner join dept d
    on e.deptno = d.deptno
group by e.deptno, d.dname;

-- 위 결과에서 40번 부서까지 출력
select d.deptno, d.dname,
    round(avg(e.sal), 1) as AVG_SAL, 
    max(e.sal) as MAX_SAL, 
    min(e.sal) as MIN_SAL, 
    count(e.deptno) as COUNT
from emp e, dept d
where e.deptno(+) = d.deptno
group by d.deptno, d.dname
order by d.deptno;


-- 부서번호, 부서이름, 사번, 이름, 직책(job), 급여를 출력.
-- 단, 모든 부서가 출력되어야 함.
select d.deptno, d.dname, e.empno, e.ename, e.job, e.sal
from dept d, emp e
where d.deptno = e.deptno(+);

select d.deptno, d.dname, e.empno, e.ename, e.job, e.sal
from dept d left join emp e
    on d.deptno = e.deptno;
    
select d.deptno, d.dname, e.empno, e.ename, e.job, e.sal
from emp e right join dept d
    on d.deptno = e.deptno;


-- 부서번호, 부서이름, 사번, 이름, 매니저사번, 매니저 이름, 급여, 급여 등급을 출력.
-- 단, 모든 부서와 모든 사원이 출력되어야 함. 부서번호 오름차순 출력.
select d.deptno, d.dname, e1.empno, e1.ename, e1.mgr,
    e2.ename,
    e1.sal, s.grade
from dept d, emp e1, emp e2, salgrade s
where d.deptno = e1.deptno(+)
    and e1.mgr = e2.empno(+)
    and e1.sal between s.losal(+) and s.hisal(+)
order by deptno;

select d.deptno, d.dname, e1.empno, e1.ename, e1.mgr,
    e2.ename,
    e1.sal, s.grade
from dept d 
    left join emp e1 on d.deptno = e1.deptno
    left join emp e2 on e1.mgr = e2.empno
    left join salgrade s on e1.sal between s.losal and s.hisal
order by d.deptno;


