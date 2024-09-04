from mysql.connector import MySQLConnection, Error
from config import read_config

def insert_book(title, isbn):
    # 책 정보를 삽입하기 위한 SQL 쿼리
    query = "INSERT INTO books(title,isbn) " \
            "VALUES(%s,%s)"

    # 쿼리에서 사용할 값들
    args = (title, isbn)
    book_id = None
    try:
        # 데이터베이스 설정을 읽어옴
        config = read_config()
        
        # 데이터베이스에 연결
        with MySQLConnection(**config) as conn:
            # 커서를 생성하여 쿼리 실행
            with conn.cursor() as cursor:
                # 삽입된 행의 마지막 ID를 가져옴
                cursor.execute(query, args)
                book_id =  cursor.lastrowid
             
            # 트랜잭션을 커밋하여 변경 사항을 저장
            conn.commit()
        # 삽입된 책의 ID를 반환
        return book_id
    except Error as error:
        # 오류가 발생하면 오류 메시지를 출력
        print(error)

if __name__ == '__main__':
    # 'A Sudden Light' 라는 제목과 '9781439187036'라는 ISBN을 가진 책을 삽입
    insert_book('A Sudden Light', '9781439187036')
