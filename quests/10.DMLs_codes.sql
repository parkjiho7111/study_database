-- 📌 문제 1 — 테이블 생성 (PRIMARY KEY 기초)
-- 아래 요구사항에 맞는 CREATE TABLE 문을 작성하시오.
-- ✔ 요구사항
-- 테이블명: students
-- 컬럼:
-- id (UUID PRIMARY KEY DEFAULT uuid_generate_v4())
-- name (VARCHAR(50))
-- age (INT)

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE students (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50),
    age INT
);



-- 📌 문제 2 — CREATE (INSERT) 기초
-- ✔ 요구사항
-- 위 students 테이블에 다음 데이터를 INSERT 하시오.
-- id
-- name
-- age
-- 1
-- 홍길동
-- 23
-- 2
-- 이영희
-- 21
-- 3
-- 박철수
-- 26

INSERT INTO students (id, name, age) VALUES
(1, '홍길동', 23),
(2, '이영희', 21),
(3, '박철수', 26);


-- 📌 문제 3 — READ (SELECT) 기본 조회
-- 다음 조건들을 만족하는 SELECT 쿼리를 작성하시오.
-- students 테이블의 전체 데이터를 조회
SELECT id, name, age FROM students;
-- 나이가 22세 이상인 학생만 조회

SELECT id, name, age FROM students WHERE age >= 22;


-- name 이 “홍길동”인 학생만 조회

SELECT id, name, age FROM students WHERE name = '홍길동';


-- 📌 문제 4 — UPDATE 연습
-- ✔ 요구사항
-- id = 2 인 학생의 나이를 25로 수정하시오.
-- Option : select 통한 UUID id 가져와서 삭제

UPDATE students
SET age = 25
WHERE id = (SELECT id FROM students WHERE name = '이영희');


-- 📌 문제 5 — DELETE 연습
-- ✔ 요구사항
-- id = 3 번 학생 데이터를 삭제하는 DELETE 문을 작성하시오.
-- Option : select 통한 UUID id 가져와서 삭제

DELETE FROM students
WHERE id = (SELECT id FROM students WHERE name = '박철수');

-- 📌 문제 6 — PRIMARY KEY 이해 문제
-- 다음과 같은 테이블을 가정하시오:
-- CREATE TABLE books (
--     book_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
--     title VARCHAR(100),
--     price INT
-- );



-- 아래 데이터 INSERT 시 발생할 문제를 설명하시오.
-- INSERT INTO books (book_id, title, price)
-- VALUES (1, '책 A', 10000);

-- INSERT INTO books (book_id, title, price)
-- VALUES (1, '책 B', 15000);

-- 📌 질문:
-- 어떤 에러가 발생하는가?

 첫 번째 INSERT 시도에서, book_id 컬럼은 UUID 타입인데 숫자 1이 입력되어 
 **invalid input syntax for type uuid**와 같은 타입 변환 오류가 발생할 가능성이 높습니다.

-- 왜 발생하는가?
book_id가 UUID 타입임에도 불구하고 
숫자 1을 문자열(따옴표 없이)로 삽입하여 데이터 타입 충돌이 일어납니다

-- PRIMARY KEY 의 규칙을 쓰시오.
PRIMARY KEY (기본 키)는 데이터베이스 테이블의 각 행을 고유하게 식별하는 제약 조건입니다.
고유성 (Uniqueness): 키 값은 테이블 내에서 중복될 수 없습니다.
NULL 불허 (Non-NULL): 키 값은 NULL 값을 가질 수 없습니다. (반드시 값이 존재해야 합니다.)