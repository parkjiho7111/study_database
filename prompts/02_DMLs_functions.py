import psycopg2
import os
from psycopg2 import extras

# --- 데이터베이스 연결 정보 ---
DB_HOST = "db_postgresql"
DB_PORT = "5432"
DB_NAME = "main_db"
DB_USER = "admin"
DB_PASSWORD = "admin123"

def get_db_connection():
    """PostgreSQL 데이터베이스에 연결하고 connection 객체를 반환합니다."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"데이터베이스 연결 오류: {e}")
        return None

# --- 문제 1: 테이블 생성 함수 ---
def create_books_table():
    """
    books 테이블을 생성합니다.
    - uuid-ossp 확장 기능 활성화
    - 이미 테이블이 존재하면 삭제 후 재생성하여 초기 상태 보장
    """
    conn = get_db_connection()
    if not conn:
        return

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
                cur.execute("DROP TABLE IF EXISTS books;")
                cur.execute("""
                    CREATE TABLE books (
                        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                        title VARCHAR(100) NOT NULL,
                        price INT NOT NULL
                    );
                """)
                print("books 테이블이 생성되었습니다.")
    except psycopg2.Error as e:
        print(f"테이블 생성 중 오류 발생: {e}")
    finally:
        if conn:
            conn.close()

# --- 문제 2: 데이터 삽입 함수 ---
def insert_books():
    """지정된 3개의 도서 데이터를 books 테이블에 삽입합니다."""
    conn = get_db_connection()
    if not conn:
        return
        
    books_to_insert = [
        ('파이썬 입문', 19000),
        ('알고리즘 기초', 25000),
        ('네트워크 이해', 30000)
    ]
    
    try:
        with conn:
            with conn.cursor() as cur:
                extras.execute_values(
                    cur,
                    "INSERT INTO books (title, price) VALUES %s",
                    books_to_insert
                )
                print(f"{cur.rowcount}개 도서가 삽입되었습니다.")
    except psycopg2.Error as e:
        print(f"데이터 삽입 중 오류 발생: {e}")
    finally:
        if conn:
            conn.close()

# --- 문제 3: 데이터 조회 함수 ---
def get_all_books():
    """books 테이블의 모든 데이터를 조회하여 출력합니다."""
    conn = get_db_connection()
    if not conn:
        return []
    
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, title, price FROM books ORDER BY price ASC;")
            books = cur.fetchall()
            print("\n--- 전체 도서 목록 ---")
            for book in books:
                print(book)
            return books
    except psycopg2.Error as e:
        print(f"전체 조회 중 오류 발생: {e}")
        return []
    finally:
        if conn:
            conn.close()

def get_expensive_books():
    """가격이 25000원 이상인 도서를 조회하여 출력합니다."""
    conn = get_db_connection()
    if not conn:
        return []
        
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, title, price FROM books WHERE price >= 25000 ORDER BY price ASC;")
            books = cur.fetchall()
            print("\n--- 가격이 25000원 이상인 도서 ---")
            for book in books:
                print(book)
            return books
    except psycopg2.Error as e:
        print(f"고가 도서 조회 중 오류 발생: {e}")
        return []
    finally:
        if conn:
            conn.close()

def get_book_by_title(title: str):
    """제목으로 특정 도서를 조회하여 출력합니다."""
    conn = get_db_connection()
    if not conn:
        return None
        
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, title, price FROM books WHERE title = %s;", (title,))
            book = cur.fetchone()
            print(f"\n--- '{title}' 검색 결과 ---")
            print(book if book else "해당 제목의 도서를 찾을 수 없습니다.")
            return book
    except psycopg2.Error as e:
        print(f"제목으로 조회 중 오류 발생: {e}")
        return None
    finally:
        if conn:
            conn.close()

# --- 문제 4: 데이터 수정 함수 ---
def update_second_book_price():
    """저장된 순서상 두 번째 도서의 가격을 27000으로 변경합니다."""
    conn = get_db_connection()
    if not conn:
        return

    try:
        with conn:
            with conn.cursor() as cur:
                # 저장 순서를 가격 오름차순으로 가정하고 두 번째 도서의 id 조회
                cur.execute("SELECT id FROM books ORDER BY price ASC LIMIT 1 OFFSET 1;")
                book_id_to_update = cur.fetchone()

                if book_id_to_update:
                    # 조회한 id를 이용해 가격 수정
                    cur.execute("UPDATE books SET price = %s WHERE id = %s;", (27000, book_id_to_update[0]))
                    print("두 번째 도서 가격이 27000으로 수정되었습니다.")
                else:
                    print("두 번째 도서를 찾을 수 없습니다.")
    except psycopg2.Error as e:
        print(f"가격 업데이트 중 오류 발생: {e}")
    finally:
        if conn:
            conn.close()

# --- 문제 5: 데이터 삭제 함수 ---
def delete_third_book():
    """저장된 순서상 세 번째 도서 데이터를 삭제합니다."""
    conn = get_db_connection()
    if not conn:
        return
        
    try:
        with conn:
            with conn.cursor() as cur:
                # 저장 순서를 가격 오름차순으로 가정하고 세 번째 도서의 id 조회
                cur.execute("SELECT id FROM books ORDER BY price ASC LIMIT 1 OFFSET 2;")
                book_id_to_delete = cur.fetchone()

                if book_id_to_delete:
                    # 조회한 id를 이용해 데이터 삭제
                    cur.execute("DELETE FROM books WHERE id = %s;", (book_id_to_delete[0],))
                    print("세 번째 도서가 삭제되었습니다.")
                else:
                    print("세 번째 도서를 찾을 수 없습니다.")
    except psycopg2.Error as e:
        print(f"삭제 중 오류 발생: {e}")
    finally:
        if conn:
            conn.close()

# --- 메인 실행 블록 ---
if __name__ == '__main__':
    print("===== 데이터베이스 작업 시퀀스 시작 =====")
    
    # 문제 1: 테이블 생성
    create_books_table()
    
    # 문제 2: 데이터 삽입
    insert_books()
    
    # 문제 3: 데이터 조회 (삽입 결과 확인)
    get_all_books()
    get_expensive_books()
    get_book_by_title("파이썬 입문")
    
    # 문제 4: 데이터 수정
    print("\n===== 수정 테스트 =====")
    update_second_book_price()
    # 수정 결과 확인
    get_all_books()

    # 문제 5: 데이터 삭제
    print("\n===== 삭제 테스트 =====")
    delete_third_book()
    # 삭제 결과 확인
    get_all_books()
    
    print("\n===== 모든 작업 완료 =====")
