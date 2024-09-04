from mysql.connector import MySQLConnection, Error
from config import read_config

def delete_book(book_id):
    # 데이터베이스 설정을 읽어옴
    config = read_config()

    # 쿼리와 데이터를 준비
    query = "DELETE FROM books WHERE id = %s"

    data = (book_id, ) 

    affected_rows = 0  # 영향을 받은 행의 수를 저장할 변수를 초기화

    try:
        # 데이터베이스에 연결
        with MySQLConnection(**config) as conn:
            # 책을 삭제
            with conn.cursor() as cursor:
                cursor.execute(query, data)

                # 영향을 받은 행의 수를 가져옴
                affected_rows = cursor.rowcount

            # 변경 사항을 커밋
            conn.commit()

    except Error as error:
        # 오류가 발생하면 오류 메시지를 출력
        print(error)

   
