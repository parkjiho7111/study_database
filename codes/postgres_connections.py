import psycopg2
import os
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
print("PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.")

with conn.cursor() as cursor :
    # cursor.execute("INSERT INTO users_uuid_name (name) VALUES ('from code')")

        # cursor.execute("""UPDATE users_uuid_name
        #                SET name = 'code name'
        #                WHERE id_name = 'cbdddaca-c7a9-42ff-b0ed-8f00dbcd8377';""")
        # cursor.execute("""DELETE FROM users_uuid_name
        #                WHERE id_name = '92ad55b7-94bf-4e1d-9de2-bbdd54833475';""")
        cursor.execute("SELECT * FROM users_uuid_name;")
        records = cursor.fetchall()
        for record in records:
            print(record)
            print(f'ID: {record[0]}, Name: {record[1]}')       
conn.commit()
