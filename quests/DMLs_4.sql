-- 📌 문제 4 — 키워드 검색 로그 테이블
-- 테이블명: keyword_search_logs
--  컬럼:
-- keyword


-- result_count


-- search_time


-- 데이터:
-- "python", 120, "2025-11-19 10:00:00"


-- "chatgpt", 300, "2025-11-19 10:05:00"


-- "docker", 90, "2025-11-19 10:10:00"


-- 👉 요구:
-- 1. 위 3개 데이터를 INSERT


CREATE TABLE keyword_search_logs (
    keyword VARCHAR(500),
    result_count INT,
    search_time VARCHAR(500)
);

insert into keyword_search_logs (keyword, result_count, search_time) values
('python', 120, '2025-11-19 10:00:00'),
('chatgpt', 300, '2025-11-19 10:05:00'),
('docker', 90, '2025-11-19 10:10:00');

-- 2. result_count가 100 이상인 키워드 조회

SELECT keyword, result_count, search_time
FROM keyword_search_logs
WHERE result_count >= 100;



-- 3. "docker" 검색 결과 수를 150으로 UPDATE
UPDATE keyword_search_logs
SET search_time = 150
WHERE keyword = 'docker';



-- 4. "python" 로그 삭제
DELETE FROM keyword_search_logs
WHERE keyword = 'python';