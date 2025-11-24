## prompts
```
제미니야 너는 20년차 풀스텍 전문개발자야. 나는 아래의 문제를 풀어야해. 각 문제마다 조건이 있어.
조건을 이용하여 아래의 문제풀어줘.

조건

-프롬프트(json형식)으로 풀고, 검증하기

- 각 문제마다 if '__name__' == '__main__' 이 코드 실행으로 확인하기

-study_databases/prompt/02_DMLs_functions.py 저장하기. 

-import psycopg2
import os
def create_books_table():
    """PostgreSQL 데이터베이스에 연결합니다."""
    db_host = "db_postgresql"
    db_port = "5432"
    db_name = "main_db"
    db_user = "admin"
    db_password = "admin123"
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    ```