-- 관계형 데이터베이스(Relational Database)
-- scott 계정 테이블

-- 1) 이름이 ALLEN인 직원의 모든 정보 출력
select * from emp where ename = 'ALLEN';

-- 2) 1에서 찾은 정보를 이용해서, ALLEN이 근무하는 부서에 대한 정보를 출력
select * from dept where deptno = 30;

-- 3) 1에서 찾은 정보를 이용해서, ALLEN의 급여 등급을 출력
select grade from salgrade
where losal <= 1600 and 1600 <= hisal;
