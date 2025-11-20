-- 📌 문제 1 — 뉴스 스크래핑 테이블
-- 테이블명: news_articles
--  컬럼:
-- title
-- url

-- author

-- published_at


-- 데이터:
-- "AI 시대 도래", "https://news.com/ai", "홍길동", "2025-01-01"

-- "경제 성장률 상승", "https://news.com/economy", "이영희", "2025-01-05"


-- 👉 요구:

-- 두 번째 뉴스를 삭제하는 DELETE문 작성

-- 위 데이터를 테이블에 추가하라
CREATE TABLE news_articles (
    title varchar(500),
    url varchar(500),
    author varchar(500),
    published_at VARCHAR(500)
);

INSERT INTO news_articles (title, url, author, published_at) 
VALUES ('AI 시대 도래', 'https://news.com/ai', '홍길동', '2025-01-01'),
        ('경제 성장률 상승', 'https://news.com/economy', '이영희', '2025-01-05');

-- author가 "홍길동"인 데이터만 조회하는 쿼리를 작성하라

SELECT title, url, author, published_at
FROM news_articles
WHERE author = '홍길동';

-- 첫 번째 뉴스 제목을 새로운 문자열로 변경하는 UPDATE문 작성

UPDATE news_articles
SET title = '새로운 세상의 등장'
WHERE title = 'AI 시대 도래';

-- 두 번째 뉴스를 삭제하는 DELETE문 작성

DELETE from news_articles 
where title = '경제 성장률 상승'