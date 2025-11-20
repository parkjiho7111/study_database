-- 📌 문제 2 — 웹사이트 링크 수집 테이블
-- 테이블명: web_links
--  컬럼:
-- link_text

-- link_url

-- category

-- 데이터:
-- "네이버", "https://naver.com", "portal"

-- "구글", "https://google.com", "portal"

-- "깃허브", "https://github.com", "dev"

-- 👉 요구:
-- 데이터 3개를 생성하는 INSERT문 작성

CREATE TABLE web_links (
    link_text VARCHAR(500),
    link_url VARCHAR(500),
    category VARCHAR(500)
);

INSERT INTO web_links (link_text, link_url, category) VALUES 
('네이버', 'https://naver.com', 'portal'),
('구글', 'https://google.com', 'portal'),
('깃허브', 'https://github.com', 'dev');

-- category가 "portal"인 링크만 조회
SELECT link_text, link_url, category
FROM web_links
where category= 'protal';

-- "깃허브"의 category를 "code" 로 수정
UPDATE web_links
SET category = 'code'
WHERE link_text = '깃허브';

-- "네이버" 데이터 삭제
DELETE FROM web_links where link_text = '네이버';
