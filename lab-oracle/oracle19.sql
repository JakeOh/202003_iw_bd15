-- alter

-- emp_copy2 테이블에서 ename 컬럼 이름을 emp_name으로 변경
alter table emp_copy2
    rename column ename to emp_name;
    
desc emp_copy2;

-- emp_name 컬럼의 데이터 타입을 varchar2(20)으로 변경
alter table emp_copy2
    modify emp_name varchar2(20);

-- 컬럼 추가: etc(문자열 100 바이트)
alter table emp_copy2
    add etc varchar2(100 byte);

-- etc 컬럼 삭제
alter table emp_copy2
    drop column etc;
    
-- empno를 PK로 제약조건 추가
alter table emp_copy2
    add constraint pk_emp_cp2 primary key (empno);

-- NN은 add constraint로 할 수 없고, modify를 사용
-- emp_name을 NN로 변경
alter table emp_copy2
    modify emp_name not null;  -- 제약조건 이름 없이 NN

-- job을 NN로 변경. 제약조건 이름을 설정하면서.
alter table emp_copy2
    modify job constraint nn_job not null;

-- nn_job 제약조건 삭제
alter table emp_copy2
    drop constraint nn_job;

desc emp_copy2;

-- emp_copy2 테이블 이름을 emp_cp로 변경
rename emp_copy2 to emp_cp;


-- 테이블 생성시 column-level 제약조건
create table ex8 (
    -- column_name data_type constraint
    col1 number constraint pk_ex8 primary key,
    col2 varchar2(10) constraint nn_col2 not null
);
desc ex8;

-- 테이블 생성시 table-level 제약조건
create table ex9 (
    col1 number,
    col2 varchar2(10),
    col3 varchar2(10) constraint nn_col3 not null,
    -- not null은 column-level만 가능
    -- 다른 제약조건들은 column-level과 table-level이 모두 가능
    constraint pk_ex9 primary key (col1),
    constraint unq_col2 unique (col2)
);
desc ex9;


-- sequence 생성
create sequence seq_ex9;
select seq_ex9.nextval from dual;

insert into ex9
values(seq_ex9.nextval, 'abc', 'b');

select * from ex9;

select * from ex_emp;