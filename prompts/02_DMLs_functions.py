import psycopg2
import os
import uuid

# -- 데이터베이스 연결 함수 --
def get_db_connection():
    """PostgreSQL 데이터베이스 연결 객체를 반환합니다."""
    db_host = "db_postgresql"
    db_port = "5432"
    db_name = "main_db"
    db_user = "admin"
    db_password = "admin123"
    try:
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"데이터베이스 연결에 실패했습니다: {e}")
        return None

# 📌 문제 1 — 테이블 생성 함수 만들기
def create_books_table():
    """books 테이블을 생성합니다."""
    conn = get_db_connection()
    if conn is None:
        return

    try:
        with conn.cursor() as cur:
            # UUID 생성을 위한 확장 기능 활성화
            cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
            # 기존 테이블이 있다면 삭제 (테스트를 위해)
            cur.execute("DROP TABLE IF EXISTS books;")
            # 테이블 생성
            cur.execute("""
                CREATE TABLE books (
                    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
                    title VARCHAR(100) NOT NULL,
                    price INT NOT NULL,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()
            print("books 테이블이 생성되었습니다.")
    except psycopg2.Error as e:
        print(f"테이블 생성 중 오류 발생: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

# 📌 문제 2 — INSERT 함수 만들기
def insert_books():
    """books 테이블에 여러 도서 데이터를 삽입합니다."""
    conn = get_db_connection()
    if conn is None:
        return

    books_to_insert = [
        ('파이썬 입문', 19000),
        ('알고리즘 기초', 25000),
        ('네트워크 이해', 30000)
    ]
    
    try:
        with conn.cursor() as cur:
            # executemany를 사용하여 여러 데이터 삽입
            sql = "INSERT INTO books (title, price) VALUES (%s, %s);"
            cur.executemany(sql, books_to_insert)
            conn.commit()
            print(f"{cur.rowcount}개 도서가 삽입되었습니다.")
    except psycopg2.Error as e:
        print(f"데이터 삽입 중 오류 발생: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

# 📌 문제 3 — SELECT 함수 만들기
def get_all_books():
    """모든 도서 정보를 조회합니다."""
    conn = get_db_connection()
    if conn is None:
        return
    
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, title, price FROM books ORDER BY created_at;")
            books = cur.fetchall()
            print("\n--- 전체 도서 목록 ---")
            for book in books:
                print(book)
            return books
    except psycopg2.Error as e:
        print(f"데이터 조회 중 오류 발생: {e}")
        return []
    finally:
        if conn:
            conn.close()

def get_expensive_books():
    """가격이 25000원 이상인 도서를 조회합니다."""
    conn = get_db_connection()
    if conn is None:
        return

    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, title, price FROM books WHERE price >= 25000 ORDER BY created_at;")
            books = cur.fetchall()
            print("\n--- 가격이 25000원 이상인 도서 ---")
            for book in books:
                print(book)
    except psycopg2.Error as e:
        print(f"데이터 조회 중 오류 발생: {e}")
    finally:
        if conn:
            conn.close()

def get_book_by_title(title: str):
    """제목으로 특정 도서를 조회합니다."""
    conn = get_db_connection()
    if conn is None:
        return

    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, title, price FROM books WHERE title = %s;", (title,))
            book = cur.fetchone()
            print(f"\n--- 제목이 '{title}'인 도서 ---")
            if book:
                print(book)
            else:
                print("해당 제목의 도서를 찾을 수 없습니다.")
    except psycopg2.Error as e:
        print(f"데이터 조회 중 오류 발생: {e}")
    finally:
        if conn:
            conn.close()

# 📌 문제 4 — UPDATE 함수 만들기
def update_second_book_price(new_price: int):
    """두 번째로 삽입된 도서의 가격을 수정합니다."""
    conn = get_db_connection()
    if conn is None:
        return

    try:
        with conn.cursor() as cur:
            # 두 번째 도서의 UUID 조회 (삽입 순서 기준)
            cur.execute("SELECT id FROM books ORDER BY created_at LIMIT 1 OFFSET 1;")
            book_id_to_update = cur.fetchone()
            
            if book_id_to_update:
                book_id = book_id_to_update[0]
                cur.execute("UPDATE books SET price = %s WHERE id = %s;", (new_price, book_id))
                conn.commit()
                print(f"\n두 번째 도서 가격이 {new_price}으로 수정되었습니다.")
            else:
                print("수정할 두 번째 도서가 없습니다.")
    except psycopg2.Error as e:
        print(f"데이터 수정 중 오류 발생: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

# 📌 문제 5 — DELETE 함수 만들기
def delete_third_book():
    """세 번째로 삽입된 도서를 삭제합니다."""
    conn = get_db_connection()
    if conn is None:
        return

    try:
        with conn.cursor() as cur:
            # 세 번째 도서의 UUID 조회 (삽입 순서 기준)
            cur.execute("SELECT id FROM books ORDER BY created_at LIMIT 1 OFFSET 2;")
            book_id_to_delete = cur.fetchone()

            if book_id_to_delete:
                book_id = book_id_to_delete[0]
                cur.execute("DELETE FROM books WHERE id = %s;", (book_id,))
                conn.commit()
                print("\n세 번째 도서가 삭제되었습니다.")
            else:
                print("삭제할 세 번째 도서가 없습니다.")
    except psycopg2.Error as e:
        print(f"데이터 삭제 중 오류 발생: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

# -- 메인 실행 블록 --
if __name__ == '__main__':
    print("스크립트 실행 시작")
    
    # 1. 테이블 생성
    create_books_table()
    
    # 2. 데이터 삽입
    insert_books()
    
    # 3. 데이터 조회
    all_books = get_all_books()
    get_expensive_books()
    get_book_by_title('파이썬 입문')
    
    # 4. 데이터 수정
    if all_books and len(all_books) >= 2:
        update_second_book_price(27000)
        get_all_books() # 수정 후 전체 목록 확인
    else:
        print("\n수정할 데이터가 충분하지 않습니다.")

    # 5. 데이터 삭제
    if all_books and len(all_books) >= 3:
        delete_third_book()
        get_all_books() # 삭제 후 전체 목록 확인
    else:
        print("\n삭제할 데이터가 충분하지 않습니다.")
        
    print("\n스크립트 실행 완료")