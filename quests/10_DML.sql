-- 📌 문제 1 — 테이블 생성 (PRIMARY KEY 기초)
-- 아래 요구사항에 맞는 CREATE TABLE 문을 작성하시오.
-- ✔ 요구사항
-- 테이블명: students
-- 컬럼:
-- id (INT, PRIMARY KEY)
-- name (VARCHAR(50))
-- age (INT)

CREATE TABLE students (
    id INT PRIMARY KEY,
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

SELECT * FROM students;
-- 나이가 22세 이상인 학생만 조회
SELECT * FROM students WHERE age >= 22;

-- name 이 “홍길동”인 학생만 조회
SELECT * FROM students WHERE name = '홍길동';


-- 📌 문제 4 — UPDATE 연습
-- ✔ 요구사항
-- id = 2 인 학생의 나이를 25로 수정하시오.
UPDATE students
SET age = 25
WHERE id = 2;

-- 📌 문제 5 — DELETE 연습
-- ✔ 요구사항
-- id = 3 번 학생 데이터를 삭제하는 DELETE 문을 작성하시오.
DELETE FROM students
WHERE id = 3;

-- 📌 문제 6 — PRIMARY KEY 이해 문제
-- 다음과 같은 테이블을 가정하시오:
-- CREATE TABLE books (
--     book_id INT PRIMARY KEY,
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
두 번째 INSERT 문 실행 시 Duplicate entry error 또는 **Primary Key violation error**가 발생합니다.


-- 왜 발생하는가?
첫 번째 쿼리 INSERT INTO books (book_id, title, price) VALUES (1, '책 A', 10000);는 성공적으로 book_id가 1인 레코드를 테이블에 추가합니다.

두 번째 쿼리 INSERT INTO books (book_id, title, price) VALUES (1, '책 B', 15000);는 이미 존재하는 book_id 값인 1을 다시 사용하려고 시도합니다.

book_id 컬럼은 PRIMARY KEY로 지정되어 있기 때문에, 이 컬럼은 **고유성(Uniqueness)**을 가져야 합니다. 즉, 같은 값을 두 번 이상 허용하지 않습니다.

따라서 데이터베이스 시스템은 이 중복 삽입을 거부하고 에러를 발생시킵니다.

-- PRIMARY KEY 의 규칙을 쓰시오.
PRIMARY KEY는 테이블의 각 행을 고유하게 식별하는 데 사용되는 핵심 제약 조건입니다. 반드시 지켜야 할 두 가지 규칙은 다음과 같습니다.

고유성 (Uniqueness):

PRIMARY KEY 컬럼에 저장되는 값은 테이블 내에서 중복될 수 없습니다.

이는 테이블의 모든 레코드(행)가 고유하게 구분되도록 보장합니다.

NULL 불허 (Non-NULL):

PRIMARY KEY 컬럼은 NULL 값을 가질 수 없습니다.

모든 레코드는 반드시 고유한 식별자(키)를 가지고 있어야 합니다.